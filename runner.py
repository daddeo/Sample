# tests/runner.py
import unittest

# import your test modules
import test_calc
import test_employee


# alltests = unittest.TestSuite([test_calc.suiteCalc(), test_employee.suiteEmployee()])
# unittest.TextTestRunner(verbosity=2).run(alltests)


# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()


# def load_tests(loader, standard_tests, pattern):
#     # standard_tests.addTests(package_tests)
#     return suite  # standard_tests


# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(test_calc))
suite.addTests(loader.loadTestsFromModule(test_employee))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
