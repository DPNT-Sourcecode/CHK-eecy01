import pytest

from solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_sum_x_lt_0(self):
        with pytest.raises(AssertionError):
            sum_solution.compute(-1, 2)