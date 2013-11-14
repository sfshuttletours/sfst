from django.conf import settings as django_settings
from django.core.mail.backends.smtp import EmailBackend


class TestingEmailBackend(EmailBackend):
    """
    Used in dev and qa
    """
    def send_messages(self, email_messages):
        """
        Overrides the to email address. Also if there are tons of messages being sent out then it reduces them to
        1 message.
        """
        if len(email_messages) > 1:
            email_messages = (email_messages[0],)
        email_messages[0].to = [django_settings.DEFAULT_TO_EMAIL,]
        super(TestingEmailBackend, self).send_messages(email_messages)

class SFSTEmailBackend(EmailBackend):
    """
    Used in prod basically to CC the DEFAULT_TO_EMAIL address on all outgoing email (if not already there)
    """
    def send_messages(self, email_messages):
        if not django_settings.DEFAULT_TO_EMAIL in email_messages[0].to:
            email_messages[0].to.append(django_settings.DEFAULT_TO_EMAIL)
        super(SFSTEmailBackend, self).send_messages(email_messages)
