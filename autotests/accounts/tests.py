from django.test import TestCase


class SimpleTestCase(TestCase):
    def test_addition(self):
        self.assertEqual(1 + 2, 3)

    def test_subtraction(self):
        self.assertEqual(5 - 2, 3)