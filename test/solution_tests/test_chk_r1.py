from solutions.CHK import checkout_solution

class TestCheckout():
    def test_skus_number(self):
        assert checkout_solution.checkout('AB12CD') == -1
        
    def test_skus_space(self):
        assert checkout_solution.checkout('AB CD') == -1

    def test_skus_comma(self):
        assert checkout_solution.checkout('A;B') == -1    