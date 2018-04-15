import unittest
from .interval_tree import Interval
from .solution import lowest_price_intervals


class SolutionTest(unittest.TestCase):

    def test_get_lowest_price_interval_1(self):
        input_intervals = [Interval(3, 5, 8), Interval(4, 7, 6), Interval(2, 5, 9)]
        output_intervals = lowest_price_intervals(input_intervals)
        assert output_intervals == [Interval(start=2, end=3, price=9),
                                    Interval(start=3, end=4, price=8),
                                    Interval(start=4, end=7, price=6)]

    def test_get_lowest_price_interval_2(self):
        input_intervals = [Interval(3, 5, 8), Interval(4, 7, 6), Interval(1, 3, 4)]
        output_intervals = lowest_price_intervals(input_intervals)
        assert output_intervals == [Interval(start=1, end=3, price=4),
                                    Interval(start=3, end=4, price=8),
                                    Interval(start=4, end=7, price=6)]

    def test_get_lowest_price_interval_3(self):
        input_intervals = [Interval(start=3, end=5, price=8),
                           Interval(start=9, end=13, price=9),
                           Interval(start=9, end=10, price=2),
                           Interval(start=3, end=8, price=8),
                           Interval(start=6, end=7, price=4)]
        output_intervals = lowest_price_intervals(input_intervals)
        assert output_intervals == [Interval(start=3, end=6, price=8),
                                    Interval(start=6, end=7, price=4),
                                    Interval(start=7, end=8, price=8),
                                    Interval(start=9, end=10, price=2),
                                    Interval(start=10, end=13, price=9)]

    def test_get_lowest_price_interval_4(self):
        input_intervals = [Interval(start=8, end=10, price=9),
                           Interval(start=5, end=10, price=10),
                           Interval(start=3, end=4, price=7),
                           Interval(start=4, end=5, price=5),
                           Interval(start=10, end=13, price=3)]
        output_intervals = lowest_price_intervals(input_intervals)
        assert output_intervals == [Interval(start=3, end=4, price=7),
                                    Interval(start=4, end=5, price=5),
                                    Interval(start=5, end=8, price=10),
                                    Interval(start=8, end=10, price=9),
                                    Interval(start=10, end=13, price=3)]


if __name__ == '__main__':
    unittest.main()
