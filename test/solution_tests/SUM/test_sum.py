import pytest

from solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_sum_01(self):
        assert sum_solution.compute(0, 1) == 1

    def test_sum_x_eq_0(self):
        assert sum_solution.compute(0, 2) == 2
        
    def test_sum_y_eq_0(self):
        assert sum_solution.compute(1, 0) == 1

    def test_sum_x_lt_0(self):
        with pytest.raises(AssertionError):
            sum_solution.compute(-1, 2)

    def test_sum_x_gt_100(self):
        with pytest.raises(AssertionError):
            sum_solution.compute(101, 2)

    def test_sum_y_lt_0(self):
        with pytest.raises(AssertionError):
            sum_solution.compute(2, -1)

    def test_sum_y_gt_100(self):
        with pytest.raises(AssertionError):
            sum_solution.compute(2, 101)
