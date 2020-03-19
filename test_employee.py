import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("TestEmployee: setupClass")

    @classmethod
    def tearDownClass(cls):
        print("TestEmployee: teardownClass")

    def setUp(self):
        print("TestEmployee: setUp")
        self.emp_1 = Employee("Corey", "Schafer", 50000)
        self.emp_2 = Employee("Sue", "Smith", 60000)

    def tearDown(self):
        print("TestEmployee: tearDown\n")

    def test_email(self):
        self.assertEqual(self.emp_1.email, "Corey.Schafer@email.com")
        self.assertEqual(self.emp_2.email, "Sue.Smith@email.com")

        self.emp_1.first = "John"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.email, "John.Schafer@email.com")
        self.assertEqual(self.emp_2.email, "Jane.Smith@email.com")

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, "Corey Schafer")
        self.assertEqual(self.emp_2.fullname, "Sue Smith")

        self.emp_1.first = "John"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.fullname, "John Schafer")
        self.assertEqual(self.emp_2.fullname, "Jane Smith")

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch("employee.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.emp_1.monthly_schedule("May")
            mocked_get.assert_called_with("http://company.com/Schafer/May")
            self.assertEqual(schedule, "Success")

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule("June")
            mocked_get.assert_called_with("http://company.com/Smith/June")
            self.assertEqual(schedule, "Bad Response!")


def suiteEmployee():
    tests = ["test_email", "test_fullname", "test_apply_raise", "test_monthly_schedule"]

    return unittest.TestSuite(map(TestEmployee, tests))


# def load_tests(loader, standard_tests, pattern):
#     # top level directory cached on loader instance
#     this_dir = os.path.dirname(__file__)
#     print("[Employee] dir: ", this_dir)
#     package_tests = loader.discover(start_dir=this_dir, pattern=pattern)
#     print("[Employee] tests: ", package_tests)
#     standard_tests.addTests(package_tests)
#     return standard_tests


# def load_tests(loader, tests, pattern):
#     suite = unittest.TestSuite()
#     tests = loader.loadTestsFromTestCase(TestEmployee)
#     suite.addTests(tests)
#     return suite


# test_cases = (TestEmployee, TestCase2, TestCase3)
# def load_tests(loader, tests, pattern):
#     suite = TestSuite()
#     for test_class in test_cases:
#         tests = loader.loadTestsFromTestCase(test_class)
#         suite.addTests(tests)
#     return suite

# if __name__ == "__main__":
#     unittest.main()
