import unittest
from datetime import datetime
from django.conf import settings

from sfst.localsite.models import *

class TestProducts(unittest.TestCase):
        
    def test_generate_products(self):
        """
        Test that we generate products correctly
        """
        # import sys
        # print sys.path
        # from localsite.models import *
        # tour_type = TourType(name='test tour type', seats_available=100)
        # tour_type.save()
        # 
        # schedule = TourSchedule(tour_type=tour_type)
        # schedule.save()
        # # schedule.save()
        # schedule.day_of_week.add(DayOfWeek.objects.get(isoweekday=1))
        # schedule.day_of_week.add(DayOfWeek.objects.get(isoweekday=2))
        # schedule.tour_time.add(TourTime.objects.get(time='13:00'))
        # schedule.tour_time.add(TourTime.objects.get(time='9:00'))
        # schedule.save()
        # 
        # tour_type.generate_future_tour_products(days=30)
        
        t = TourType.objects.all()[0]
        t.get_product(datetime.now())
        
        

