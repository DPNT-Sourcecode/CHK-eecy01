from solutions.CHK import checkout_solution

class TestCheckout():

    def test_skus_none(self):
        assert checkout_solution.checkout(None) == -1
        
    def test_skus_empty(self):
        assert checkout_solution.checkout('') == -1
        
    def test_skus_number(self):
        assert checkout_solution.checkout('AB12CD') == -1
        
    def test_skus_space(self):
        assert checkout_solution.checkout('AB CD') == -1

    def test_skus_comma(self):
        assert checkout_solution.checkout('A;B') == -1
        
    #def test_skus_illegal_item(self):
        #assert checkout_solution.checkout('ABE') == -1

    def test_skus(self):
        assert checkout_solution.checkout('AB') == 80

    def test_skus_lowcase(self):
        assert checkout_solution.checkout('ADad') == 130
        
    def test_skus_with_special(self):
        # 3A + 2A + 2B + B + D + C + D + C + D + C = 3A + 2A + 2B + B + 3C + 3D
        # = 130 + (2*50) + 45 + 30 + (3*15) + (3*20)
        assert checkout_solution.checkout('ADABACABABdcDc') == 130 + (2*50) + 45 + 30 + (3*15) + (3*20)