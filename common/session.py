
class SessionManagerBase(object):
    def __init__(self, request):
        self._session = request.session
  
    def _get_or_set(self, key, value):
        if not value is None:
            self._session[key] = value
            return value
        return self._session.get(key)
  
    def reset_keys(self):
        for key in self._SESSION_KEYS:
            if self._session.has_key(key):
                del self._session[key]
