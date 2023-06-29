import log_analyser
import unittest

class TestSuite(unittest.TestCase):

    def setUp(self):
        self.l = log_analyser.Log_analyser("20230629-073433_read_only_1h.txt")

    def test_year(self):
        test_string = "Wed Jun 28 16:21:57 2023: Benchmark  - Read block 2: 3386.9 Mb/s (423.4 MB/s)"
        print(self.l.get_year(test_string))

    def test_day(self):
        test_string = "Wed Jun 28 16:21:57 2023: Benchmark  - Read block 2: 3386.9 Mb/s (423.4 MB/s)"
        print(self.l.get_day(test_string))

    def test_month(self):
        test_string = "Wed Jun 28 16:21:57 2023: Benchmark  - Read block 2: 3386.9 Mb/s (423.4 MB/s)"
        print(self.l.get_month(test_string))

    def test_time(self):
        test_string = "Wed Jun 28 16:21:57 2023: Benchmark  - Read block 2: 3386.9 Mb/s (423.4 MB/s)"
        print(self.l.get_time(test_string))

    def test_xfert_rate(self):
        test_string = "Wed Jun 28 16:21:57 2023: Benchmark  - Read block 2: 3386.9 Mb/s (423.4 MB/s)"
        print(self.l.get_xfert_rate(test_string))

    def test_xfert_direction(self):
        test_string = "Wed Jun 28 16:21:57 2023: Benchmark  - Read block 2: 3386.9 Mb/s (423.4 MB/s)"
        print(self.l.get_xfert_direction(test_string))

