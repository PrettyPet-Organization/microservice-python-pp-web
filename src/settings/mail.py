# Configurations for sending email, including SMTP server, sender settings and email templates.
import os


SMTP_PORT = int(os.getenv("MAIL_SETTINGS_PORT"))
SMTP_SERVER = os.getenv("MAIL_SETTINGS_SERVER")
# app email address from which we'll send emails looking like this - app@inbox.ru
EMAIL_ADDRESS = os.getenv("MAIL_SETTINGS_EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("MAIL_SETTINGS_EMAIL_PASSWORD")
EMAIL_TIMEOUT = int(os.getenv("MAIL_SETTINGS_EMAIL_TIMEOUT"))
