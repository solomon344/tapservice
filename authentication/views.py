from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from django.db.models import Q
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from Serializers.serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .utils import create_otp, send_otp_mail, Verify_otp
# from google.auth.transport.requests import Request as GoogleRequest
import requests
from django.conf import settings


User = get_user_model()
# Create your views here.

class EntryPoint(APIView):

    """
    <h3>Introduction </h3>Welcome to the TapService AUTH api. Use the endpoints to manage authentications -> login,token obtain, refresh tokens, logouts.\n
    This view serves as the entry point for the AUTH api, providing a brief overview of available endpoints.
    \n

    <h3 style="color:red"
     
     .> Authentication Endpoints</h3> \n
    - <strong>login</strong>: /login -> sends an otp to user \n
    - <strong>access_token</strong>: /token -> Access Token \n
    - <strong>verify_token</strong>: /token/verify -> Verifies an access token Token \n
    - <strong>refresh_token</strong>: /token/refresh -> Refresh & Access Token \n
    \n
     <h3> Resource Endpoints</h3> \n
     - <strong>Access Token</strong>: BASE_URL/api/ -> For resources \n
    """

    permission_classes = (AllowAny,)
    
    def get(self, request: Request, *args, **kwargs):
        return Response({
            "message": "Welcome to the TapService AUTH api. Use the endpoints to manage authentications -> login,token obtain, refresh tokens, logouts.",
            "endpoints": {
                "login": "/login",
                "access_token": "/token",
                "verify_token": "/token/verify",
                "refresh_token": "/token/refresh",
            }
        })

class MyTokenObtainPairView(APIView):
    permission_classes = (AllowAny,)
    
    
    def post(self, request: Request, *args, **kwargs):
        
        data = request.data
        otp = data.get('otp')
        finder = data.get('finder')
        otpverify = Verify_otp(otp,finder)  

        if otpverify.is_valid():
            refresh = RefreshToken.for_user(otpverify.user)
            otpverify.delete()
            serializer = UserSerializer(otpverify.user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": serializer.data
            })

        else:
            return Response(
                {"message": "Invalid OTP."},
                status=status.HTTP_400_BAD_REQUEST
            )

                
class LoginView(APIView):
    """
    <h3> Introduction </h3> \n Welcome to the Login route of the TapService AUTH api. \n
    \n
    <strong> Args :</strong>
    - finder: str
    - auth_provider: str
    - password: str \n
    <strong> Explaination: </strong>
    - finder: The email or phone number of the user.
    - auth_provider: The authentication provider (e.g., 'google').
    - password: The password of the user. \n
    <strong> returns: </strong>
    - A JSON response containing an access token, refresh token, and <strong style="color:green; text-decoration:underline">type</strong>. \n
    <strong>type:</strong> \n
    if finder is a phone number and associates with many users, then it will return {type:accounts} and a list of all the users associated with the phone number.
    otherwise finder is an email and will return type:otp and sends an otp to the user's email
    otherwise an error will be returned
    """
    permission_classes = (AllowAny,)

    
    def post(self, request: Request, *args, **kwargs):
        data = request.data
        finder = data.get('finder')
        auth_provider = data.get('auth_provider')
        password = data.get('password', None)

        if auth_provider == 'google':
            
            code = data.get('code')
            redirect_uri = data.get('redirect_uri')
            token_url = 'https://oauth2.googleapis.com/token'
            token_data = {
                'client_id': settings.GOOGLE_CLIENT_ID,
                'client_secret': settings.GOOGLE_CLIENT_SECRET,
                'code': code,
                'grant_type': 'authorization_code',
                'redirect_uri': redirect_uri,
            }
            
            token_response = requests.post(token_url, data=token_data)
            token_json = token_response.json()
            
            if token_response.status_code != 200:
                return Response({'error': 'Failed to exchange code for token'}, status=status.HTTP_400_BAD_REQUEST)
            
            access_token = token_json.get('access_token')
        
            # Get user info from Google
            user_info_url = f'https://www.googleapis.com/oauth2/v2/userinfo?access_token={access_token}'
            user_response = requests.get(user_info_url)
            user_data = user_response.json()
            
            if user_response.status_code != 200:
                return Response({'error': 'Failed to get user info'}, status=400)
            
            email = user_data.get('email')
            picture = user_data.get('picture', '')
            user = User.objects.filter(email=email).first()
            if not user:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
            
            access = RefreshToken.for_user(user)
            return Response({
                'access': str(access.access_token),
                'refresh': str(access),
                'user': UserSerializer(user).data               
            },status=status.HTTP_200_OK)
            

        else:
            user = User.objects.filter(
                Q(email=finder) | Q(phone=finder)
            )

            if not user.exists():
                return Response(
                    {"message": "User not found."},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            else:
                if user.count() > 1:
                    serializer = UserSerializer(user, many=True)
                    return Response({
                        'type':'accounts',
                        'accounts': serializer.data,
                        
                    },status=status.HTTP_200_OK)
                else:
                    user = user.first()
                    if user.check_password(password) == False:
                        return Response(
                            {"message": "Invalid Email or Password."},
                            status=status.HTTP_400_BAD_REQUEST
                        )
                    # refresh = RefreshToken.for_user(user)
                    otp = create_otp(user)
                    send_otp_mail(user.email, str(otp))
                    return Response({
                        'message': "OTP sent successfully.",
                        'type:':'otp',
                    },status=status.HTTP_200_OK)
                
    def get(self,request:Request, *args, **kwargs):

        return Response({
            "message": "Welcome to the TapService AUTH api. Use the endpoints to manage authentications -> login,token obtain, refresh tokens, logouts.",
            "endpoints": {
                "login": "/login",
                "access_token": "/token",
                "verify_token": "/token/verify",
                "refresh_token": "/token/refresh",
            }
        })


