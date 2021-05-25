from dojo.models import Operator
from django.test import TestCase

# Create your tests here.


class UnitTestCase(TestCase):

    def test_home_page_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'dojo/dojo.html')

    def test_operator(self):
        operator = Operator()
        operator.first_name = 'Bikash'
        operator.last_name = 'Maharjan'
        operator.save()
