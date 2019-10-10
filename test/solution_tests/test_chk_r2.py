
from collections import Counter

from solutions.CHK import checkout_solution


class TestCheckoutMachine():

    @classmethod
    def setup_class(cls):
        products = checkout_solution.Products()
        discounts = checkout_solution.DiscountStore()
        cls.cm = checkout_solution.CheckoutMachine(products, discounts)
        
    def test_apply_free_discount_B1E1(self):
        basket = Counter({'B': 1, 'E': 1})
        expected_basket = {'B': 1, 'E': 1}
        assert self.cm.apply_free_discount(basket) == expected_basket

    def test_apply_free_discount_B0E2(self):
        basket = Counter({'B': 0, 'E': 2})
        expected_basket = {'E': 2}
        assert self.cm.apply_free_discount(basket) == expected_basket
    
    def test_apply_free_discount_B1E2(self):
        basket = Counter({'B': 1, 'E': 2})
        expected_basket = {'E': 2}
        assert self.cm.apply_free_discount(basket) == expected_basket

    def test_apply_free_discount_B2E1(self):
        basket = Counter({'B': 2, 'E': 1})
        expected_basket = {'B': 2, 'E': 1}
        assert self.cm.apply_free_discount(basket) == expected_basket

    def test_apply_free_discount_B2E2(self):
        basket = Counter({'B': 2, 'E': 2})
        expected_basket = {'B': 1, 'E': 2}
        assert self.cm.apply_free_discount(basket) == expected_basket

    def test_apply_free_discount_E2(self):
        basket = Counter({'E': 2})
        expected_basket = {'E': 2}
        assert self.cm.apply_free_discount(basket) == expected_basket

    def test_count_price_A2(self):
        assert self.cm.count_price(('A', 2)) == 100

    def test_count_price_A3(self):
        assert self.cm.count_price(('A', 3)) == 130

    def test_count_price_A4(self):
        assert self.cm.count_price(('A', 4)) == 180

    def test_count_price_A5(self):
        assert self.cm.count_price(('A', 5)) == 200

    def test_count_price_A6(self):
        assert self.cm.count_price(('A', 6)) == 250

    def test_get_total_price_B1E2(self):
        assert self.cm.count_price(Counter({'B', 1}) == 100
