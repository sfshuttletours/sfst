from django.conf import settings as django_settings
from django import template


register = template.Library()

class MediaUrlNode(template.Node):
    """
    Template node that renders the media_url tag
    """
    def __init__(self, path):
        self.pathvar = template.Variable(path)
    
    def render(self, context):
        request = context.get('request')
        http_prefix = 'https' if request and request.is_secure() else 'http'
        
        return '%s://%s%s%s?v=%s' % (http_prefix, django_settings.SITE_DOMAIN, django_settings.MEDIA_URL,
                              self.pathvar.resolve(context),
                              django_settings.MEDIA_HASH)

@register.tag
def media_url(parser, token):
    """
    Template node that returns the correct path or absolute URL so that
    requests for media items to secure URLs don't cause some browsers to
    complain.
    """
    try:
        path = token.split_contents()[1]
    except ValueError:
        raise template.TemplateSyntaxError, \
        "%r tag requires exactly two arguments" % token.contents.split()[0]
    return MediaUrlNode(path)
