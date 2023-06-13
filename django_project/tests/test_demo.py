from django.test import TestCase

class DemoTestClass(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

# This will pass
    def test_this_will_pass(self):
        self.assertFalse(False)

# Comment this will fail
    # def test_this_will_fail(self):
    #     self.assertTrue(False)