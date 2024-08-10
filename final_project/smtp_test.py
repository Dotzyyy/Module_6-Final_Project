import smtplib
import ssl
import os



# SMTP Configuration using environment variables
EMAIL_HOST = 'email-smtp.eu-north-1.amazonaws.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")

context = ssl.create_default_context()

try:
    if EMAIL_USE_SSL:
        server = smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT, context=context)
    else:
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        if EMAIL_USE_TLS:
            server.starttls(context=context)
    
    server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    print("Connection successful")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()