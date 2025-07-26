from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from random import randrange
from .models import OTP
from django.utils import timezone



def create_otp(user):
    code = randrange(1000, 9999)
    otp = OTP(user=user, otp=code)
    otp.save()
    return code

def send_otp_mail(email, otp):
    subject = "OTP"
    text_content = f"Your OTP is {otp}"
    html_content = render_to_string('emails/otp.html', {'otp': otp,'year':timezone.now().year})

    msg = EmailMultiAlternatives(subject, text_content, None, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()



class Verify_otp():
    """
    A class used to verify One-Time Passwords (OTPs).

    Attributes:
    ----------
    code : str
        The OTP code to be verified.
    finder : str
        The email or phone number associated with the OTP.

    Methods:
    -------
    is_valid()
        Returns True if the OTP is valid and False otherwise.
    """

    def __init__(self,code,finder):
        self.code = code
        self.finder = finder
    
    def is_valid(self):
        """
        Returns True if the OTP is valid and False otherwise.

        An OTP is considered valid if it exists in the database, it is associated
        with the given email or phone number, and it is less than 5 minutes old.

        :return: bool
        """
        print('finder is ',self.finder,'code is ',self.code)
        otps =  OTP.objects.filter(otp=self.code)
        otp = otps.first()

        if otp and (otp.user.email == self.finder or otp.user.phone == self.finder):
            if timezone.now() - otp.created_at < timezone.timedelta(minutes=5):
                self.otp = otp
                self.user = otp.user
                return True
            else:
                print("OTP is more than 5 minutes old")
                return False
        else:
            print("OTP does not exist")
            return False
    
    def delete(self):
        self.otp.delete()




