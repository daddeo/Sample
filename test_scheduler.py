# dependency_injection
# python -m pip install mock
# http://www.voidspace.org.uk/python/articles/introduction-to-unittest.shtml

import time
from unittest import TestCase
from mock import Mock
from scheduler import Scheduler


class DependencyInjectionTest(TestCase):
    def testConstructor(self):
        scheduler = Scheduler()
        self.assertEquals(scheduler.time, time.time, "time not initialized correctly")
        self.assertEquals(
            scheduler.sleep, time.sleep, "sleep not initialized correctly"
        )

    def testSchedule(self):
        mock = Mock()
        mock.time.return_value = 100

        scheduler = Scheduler(mock.time, mock.sleep)

        mock.return_value = "foo"

        result = scheduler.schedule(300, mock)

        self.assertEquals(
            result, "foo", "schedule did not return result of calling function"
        )

        self.assertTrue(mock.time.called)
        self.assertTrue(mock.called)
        mock.sleep.assert_called_with(200)
