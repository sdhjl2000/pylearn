"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from musicshare import views
from musicshare import models
from random import randint
class SimpleTest(TestCase):
    def test_db_read(self):
        models.Ticket.objects.create(user_id=randint(1,1000),case_number=randint(1000,2000), username='sss')
        resp = self.client.get('/musicshare/all/')
        self.assertEqual(resp.status_code, 200)
        print resp.content
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        str=r"\n\r\t";
        print str
        for i in range(1,10):
            new_model= models.Ticket.objects.create(user_id=i,case_number=randint(1000,2000), username='sss')
            new_model.save()
        print models.Ticket.objects
        self.failUnlessEqual(1 + 1, 2)

__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}

