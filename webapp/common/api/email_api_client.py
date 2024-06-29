from __future__ import print_function
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
from ChangosRent.settings import SMTP_API_KEY, DEFAULT_CC_EMAIL, DEFAULT_CC_NAME, DEFAULT_FROM_EMAIL
from webapp.forms import SignUpCompanyCustomerForm, SignUpPersonCustomerForm


def notify(form):
    EmailApiClient.client_api().send(EmailMessage.create_message(form))


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

    @staticmethod
    def create_message(form):
        email_message = None
        subject = "Alta Cliente"
        copy_to = [{"name": DEFAULT_CC_NAME, "email": DEFAULT_CC_EMAIL}]
        sender = {"name": "Changos Rent Vehiculos", "email": DEFAULT_FROM_EMAIL}
        if  isinstance(form, SignUpPersonCustomerForm):
            body = EmailMessage.to_body(f"{form.cleaned_data['first_name']}, {form.cleaned_data['last_name']}")
            receiver = [{"email": f"{form.cleaned_data['email']}",
                         "name": f"{form.cleaned_data['first_name']}, {form.cleaned_data['last_name']}"}]
            email_message = EmailMessage.create(sender, receiver, subject, body, copy_to=copy_to,
                                                reply_to_email=None).build()
        if isinstance(form, SignUpCompanyCustomerForm):
            body = EmailMessage.to_body(f"{form.cleaned_data['business_name']}")
            receiver = [{"email": f"{form.cleaned_data['email']}",
                         "name": f"{form.cleaned_data['first_name']}, {form.cleaned_data['last_name']}"}]
            email_message = EmailMessage.create(sender, receiver, subject, body, copy_to=copy_to,
                                                reply_to_email=None).build()
        return email_message

    @staticmethod
    def to_body(name):
        return f"<html><body><h1>El cliente {name} se ha registrado en ChangosRent. Gracias por elegirnos!</h1></body></html>"

    @staticmethod
    def create(source, dest, email_subject, body, reply_to_email, copy_to=None, blind_copy_to=None):
        return EmailMessage(source, dest, email_subject, body, reply_to_email, copy_to, blind_copy_to)

    def build(self):
        return sib_api_v3_sdk.SendSmtpEmail(to=self.to, bcc=self.bcc, cc=self.cc, reply_to=self.reply_to,
                                            headers={"'accept": "application/json", "content-type": "application/json"},
                                            html_content=self.body, sender=self.source, subject=self.subject)


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
            api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(self.configuration))
            api_response = api_instance.send_transac_email(email_message)
            pprint(api_response)
        except ApiException as e:
            print("Exception calling SMTP Api: %s\n" % e)
        except Exception as e:
            print("Exception calling SMTP Api: %s\n" % e)
