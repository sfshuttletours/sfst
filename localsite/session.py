from datetime import datetime, timedelta

from common.session import SessionManagerBase
from localsite.models import OverbookingAttempt


class SessionManager(SessionManagerBase):
    __KEY_OVERBOOK_ATTEMPTS = 'overbook_attempts_key'
    __KEY_SITE_SKIN = 'site_skin_key'

    _SESSION_KEYS = [__KEY_OVERBOOK_ATTEMPTS, __KEY_SITE_SKIN]

    def do_record_overbook_attempt(self, tour_product):
        """
        Returns a True or False which represents whether an overbooking attempt should be recorded or not for this
        users session
        """
        should_record_overbook = False
        product_id = tour_product.product.id
        current_map = self._get_or_set(self.__KEY_OVERBOOK_ATTEMPTS, None)  # a map of product id to timestamp
        if not current_map:
            current_map = {}

        last_time_attempt = current_map.get(product_id)
        if not last_time_attempt:    # first attempt
            should_record_overbook = True
            current_map[product_id] = datetime.now()    # save current attempt time
        elif last_time_attempt + timedelta(hours=1) < datetime.now():    # 1 hour has elapsed
            should_record_overbook = True
            current_map[product_id] = datetime.now()    # save current attempt time
        self._get_or_set(self.__KEY_OVERBOOK_ATTEMPTS, current_map)    # save current_map
        return should_record_overbook

    def site_skin(self, site_skin=None):
        """
        sets and/or returns the site_skin instance ID for this users session
        """
        return self._get_or_set(self.__KEY_SITE_SKIN, site_skin)
