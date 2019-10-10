from solutions.CHK import checkout_solution

class TestCheckout():

    def test_skus_none(self):
        assert checkout_solution.checkout(None) == 0
        
    def test_skus_empty(self):
        assert checkout_solution.checkout('') == 0
        
    def test_skus_number(self):
        assert checkout_solution.checkout('AB12CD') == -1
        
    def test_skus_space(self):
        assert checkout_solution.checkout('AB CD') == -1

    def test_skus_comma(self):
        assert checkout_solution.checkout('A;B') == -1

    def test_skus_illegal_a(self):
        assert checkout_solution.checkout('a') == -1

    def test_skus(self):
        assert checkout_solution.checkout('AB') == 80

    def test_skus_lowcase(self):
        assert checkout_solution.checkout('ABCa') == -1

    def test_skus_x(self):
        assert checkout_solution.checkout('AxA') == -1

    def test_skus_special_A(self):
        assert checkout_solution.checkout('AAAAA') == 230
    
    def test_skus_with_special(self):
        # 3A + 2A + 2B + B + D + C + D + C + D + C = 3A + 2A + 2B + B + 3C + 3D
        # = 130 + (2*50) + 45 + 30 + (3*15) + (3*20) =
        assert checkout_solution.checkout('ADABACABABDCDC') == 130 + (2 * 50) + 45 + 30 + (3 * 15) + (3 * 20)
        

class TestCountPrice():

    def test_count_price_special_A(self):
        products = checkout_solution.Products()
        discounts = checkout_solution.DiscountStore()
        assert checkout_solutio.count_price(('A', 5)) == 230

