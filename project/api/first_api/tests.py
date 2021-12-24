from django.test import TestCase
# Create your tests here.e
from django.test import TestCase
from .models import GeeksModel


class SimpleTestCase(TestCase):
    def test(self):
        self.assertTrue(True)


if '__name__'== '__main__':
    TestCase.main()

