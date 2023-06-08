from django.test import TestCase

class DemoTestClass(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_this_will_pass(self):
        self.assertFalse(False)

    def test_this_will_fail(self):
        self.assertTrue(False)

    def test_this_will_also_pass(self):
        self.assertFalse(False)