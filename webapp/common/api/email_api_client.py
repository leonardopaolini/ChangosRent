from __future__ import print_function
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from ChangosRent.settings import SMTP_API_KEY, DEFAULT_CC_EMAIL, DEFAULT_CC_NAME, DEFAULT_FROM_EMAIL
from django.template.loader import render_to_string
import logging
from abc import abstractmethod

logger = logging.getLogger('webapp')


def notify(message):
    EmailApiClient.client_api().send(message.build())


class EmailMessage(object):
    def __init__(self, source, dest, email_subject, body, reply_to_email=None, copy_to=None,
                 blind_copy_to=None):
        self.source = source
        self.to = dest
        self.cc = copy_to
        self.subject = email_subject
        self.body = body
        self.reply_to = reply_to_email
        self.bcc = blind_copy_to

    def build(self):
        return sib_api_v3_sdk.SendSmtpEmail(to=self.to, bcc=self.bcc, cc=self.cc, reply_to=self.reply_to,
                                            headers={"'accept": "application/json", "content-type": "application/json"},
                                            html_content=self.body, sender=self.source, subject=self.subject)

    @staticmethod
    def create(sender, receiver, subject, body, reply_to_email=None, copy_to=None,
               blind_copy_to=None):
        return EmailMessage(sender, receiver, subject, body, copy_to=copy_to, reply_to_email=reply_to_email,
                            blind_copy_to=blind_copy_to)

    @staticmethod
    def sign_up_person_message_builder():
        return SignUpPersonEmailMessageBuilder()

    @staticmethod
    def sign_up_company_message_builder():
        return SignUpCompanyEmailMessageBuilder()

    @staticmethod
    def reset_password_request_message_builder():
        return ResetPasswordRequestEmailMessageBuilder()


class EmailMessageBuilder(object):
    class Meta:
        abstract = True

    def __init__(self):
        self._user = None
        self._email = None

    @property
    def user(self):
        return self._user

    def set_user(self, user):
        self._user = user
        return self
    
    @property
    def email(self):
        return self._email

    def set_email(self, email):
        self._email = email
        return self

    @abstractmethod
    def build(self):
        pass


class SignUpCompanyEmailMessageBuilder(EmailMessageBuilder):
    def __init__(self):
        super().__init__()
        self._business_name = None

    @property
    def business_name(self):
        return self._business_name

    def set_business_name(self, business_name):
        self._business_name = business_name
        return self

    def build(self):
        email_message = None
        subject = "Alta Cliente"
        copy_to = [{"name": DEFAULT_CC_NAME, "email": DEFAULT_CC_EMAIL}]
        sender = {"name": "Changos Rent Vehiculos", "email": DEFAULT_FROM_EMAIL}
        logger.info("Creating email message for Company Customer")
        body = render_to_string('email_template/signup_customer_email.html', {
            'customer': f"{self.business_name}",
        })

        receiver = [{"email": f"{self.email}",
                     "name": f"{self.business_name}"}]
        email_message = EmailMessage.create(sender, receiver, subject, body, copy_to=copy_to,
                                            reply_to_email=None)
        return email_message


class SignUpPersonEmailMessageBuilder(EmailMessageBuilder):
    def __init__(self):
        super().__init__()
        self._first_name = None
        self._last_name = None

    @property
    def first_name(self):
        return self._first_name

    def set_first_name(self, first_name):
        self._first_name = first_name
        return self

    @property
    def last_name(self):
        return self._last_name

    def set_last_name(self, last_name):
        self._last_name = last_name
        return self

    def build(self):
        subject = "Alta Cliente"
        copy_to = [{"name": DEFAULT_CC_NAME, "email": DEFAULT_CC_EMAIL}]
        sender = {"name": "Changos Rents Vehiculos", "email": DEFAULT_FROM_EMAIL}
        logger.info("Creating email message for Person Customer")
        body = render_to_string('email_template/signup_customer_email.html', {
            'customer': f"{self.first_name}, {self.last_name}",
        })
        receiver = [{"email": f"{self.email}",
                     "name": f"{self.first_name}, {self.last_name}"}]
        return EmailMessage.create(sender, receiver, subject, body, copy_to=copy_to,
                                            reply_to_email=None)


class ResetPasswordRequestEmailMessageBuilder(EmailMessageBuilder):
    def __init__(self):
        super().__init__()
        self._reset_url = None

    @property
    def reset_url(self):
        return self._reset_url

    def set_reset_url(self, reset_url):
        self._reset_url = reset_url
        return self

    def build(self):
        subject = "Reinicio de Contraseña"
        copy_to = [{"name": DEFAULT_CC_NAME, "email": DEFAULT_CC_EMAIL}]
        sender = {"name": "Changos Rents Vehiculos", "email": DEFAULT_FROM_EMAIL}
        logger.info("Creating email message for Password Reset")
        body = render_to_string('email_template/password_reset_email.html', {
            'name': self.email,
            'reset_url': self.reset_url,
        })
        receiver = [{"email": f"{self.email}",
                     "name": f"{self.email}"}]
        return EmailMessage.create(sender, receiver, subject, body, copy_to=copy_to,
                                            reply_to_email=None)


class EmailApiClient(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.configuration = sib_api_v3_sdk.Configuration()
        self.configuration.api_key['api-key'] = api_key
        self.configuration.api_key_prefix['partner-key'] = 'Bearer'

    @staticmethod
    def client_api():
        return EmailApiClient(SMTP_API_KEY)

    def send(self, email_message):
        try:
            logger.info(f"Sending email message to {email_message.to}")
            api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(self.configuration))
            api_response = api_instance.send_transac_email(email_message)
            logging.info(api_response)
        except ApiException as e:
            logger.error(e.body)
            print("ApiException calling SMTP Api: %s\n" % e)
        except Exception as e:
            logger.error(e.__traceback__)
            print("Exception calling SMTP Api: %s\n" % e)
