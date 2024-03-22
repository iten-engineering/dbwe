from flask_mail import Message
from config import Config

class EmailSender():

    def __init__(self, app, mail, enabled=Config.MAIL_ENABLED):
        self.app = app
        self.mail= mail
        self.enabled = enabled
        self.log_config()


    def log_config(self):
        info = self.app.logger.info
        info(f"MAIL_ENABLED = {Config.MAIL_ENABLED}")
        info(f"MAIL_DEFAULT_SENDER = {Config.MAIL_DEFAULT_SENDER}")
        info(f"MAIL_DEFAULT_RECEIPIENT = {Config.MAIL_DEFAULT_RECEIPIENT}")
        info(f"MAIL_SERVER = {Config.MAIL_SERVER}")
        info(f"MAIL_PORT = {Config.MAIL_PORT}")
        info(f"MAIL_USE_TLS = {Config.MAIL_USE_TLS}")
        info(f"MAIL_USERNAME = {Config.MAIL_USERNAME}")
        info( "MAIL_PASSWORD = ***")


    def log_email(self, subject, body, sender, recipients):
        info = self.app.logger.info
        info(f"Send email from: {sender}")
        info(f"to: {recipients}")
        info(f"subject: {subject}")
        info(f"body: {body}")


    def send(self, subject, body, 
             sender=Config.MAIL_DEFAULT_SENDER, 
             recipients=[Config.MAIL_DEFAULT_RECEIPIENT]):

        # init
        self.log_email(subject, body, sender, recipients)

        if not self.enabled:
            self.app.logger.info("Send email is DISABLED.")
            return            

        # create message
        message = Message(subject=subject, body=body, sender=sender, recipients=recipients)
        
        # send email
        try:
            with self.app.app_context():
                self.mail.send(message)
            self.app.logger.info("Send email SUCCESSFULLY done.")

        except Exception as e:
            self.app.error(f"Send email FAILED with error: {str(e)}")
            raise e

    def send_password_reset(self, user):
        self.app.logger.info(f"Send password reset email to: {user.email}")


