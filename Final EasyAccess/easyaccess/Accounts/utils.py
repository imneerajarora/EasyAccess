# utils.py
import random
from django.core.mail import send_mail

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_email(email, otp):
    subject = 'Your OTP for Email Verification'
    message = f'Your One-Time Password (OTP) is {otp}. Use this to verify your email address.'
    email_from = 'neerajchawla345@gmail.com'
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
