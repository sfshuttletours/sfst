import hashlib
import logging
import os
import threading

import django
from django.template import Context
from django.template.loader import get_template
from django.conf import settings


def start_thread(target, *args, **kwargs):
    t = threading.Thread(target=target, args=args, kwargs=kwargs)
    t.setDaemon(True)
    t.start()


def send_mail(subject, message, from_email, recipient_emails, connection=None):
    import django.core.mail
    try:
        logging.debug('Sending mail to: %s' % recipient_emails)
        logging.debug('Message: %s' % message)
        django.core.mail.send_mail(subject, message, from_email, recipient_emails, connection=connection)
    except Exception, e:
        # TODO:  Raise error again so that more information is included in the logs?
        logging.error('Error sending message [%s] from %s to %s %s' % (subject, from_email, recipient_emails, e))


def send_mail_in_thread(subject, message, from_email, recipient_emails, connection=None):
    start_thread(send_mail, subject, message, from_email, recipient_emails, connection=connection)


def send_mail_using_template(subject,
                            template_name,
                            from_email,
                            recipient_emails,
                            context_map,
                            in_thread=False,
                            connection=None):
    t = get_template(template_name)
    message = t.render(Context(context_map))
    if in_thread:
        return send_mail_in_thread(subject, message, from_email, recipient_emails, connection=connection)
    else:
        return send_mail(subject, message, from_email, recipient_emails, connection=connection)


def md5_hash(image=None, max_length=None):
    # TODO:  Figure out how much entropy is actually needed, and reduce the current number of bytes if possible if doing
    # so will result in a performance improvement.
    if max_length:
        assert max_length > 0

    ret = hashlib.md5(image or os.urandom(224)).hexdigest()
    return ret if not max_length else ret[:max_length]


def send_mail_html(subject, message, from_email, recipient_emails,
    files=None, html=True, reply_to=None, bcc=[],
    connection=None):
    import django.core.mail
    try:
        logging.debug('Sending mail to: %s' % recipient_emails)
        logging.debug('Message: %s' % message)
        email = django.core.mail.EmailMessage(subject, message, from_email,
            recipient_emails, bcc, connection=connection)
        if html:
            email.content_subtype = "html"
        if files:
            for file in files:
                email.attach_file(file)
        if reply_to:
            email.extra_headers = {'Reply-To': reply_to}
        email.send()
    except Exception, e:
        # TODO:  Raise error again so that more information is included in the logs?
        logging.error('Error sending message [%s] from %s to %s %s' % (subject, from_email, recipient_emails, e))
