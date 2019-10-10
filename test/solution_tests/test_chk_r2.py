
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
        self.cm.apply_free_discount(basket)
        assert basket == expected_basket

    def test_apply_free_discount_B0E2(self):
        basket = Counter({'B': 0, 'E': 2})
        expected_basket = {'B': 0, 'E': 2}
        self.cm.apply_free_discount(basket)
        assert basket == expected_basket   
    
    def test_apply_free_discount_B1E2(self):
        basket = Counter({'B': 1, 'E': 2})
        expected_basket = {'B': 0, 'E': 2}
        self.cm.apply_free_discount(basket)
        assert basket == expected_basket

    def test_apply_free_discount_B2E1(self):
        basket = Counter({'B': 2, 'E': 1})
        expected_basket = {'B': 2, 'E': 1}
        self.cm.apply_free_discount(basket)
        assert basket == expected_basket        

    def test_apply_free_discount_B2E2(self):
        basket = Counter({'B': 2, 'E': 2})
        expected_basket = {'B': 1, 'E': 2}
        self.cm.apply_free_discount(basket)
        assert basket == expected_basket

    def test_apply_free_discount_E2(self):
        basket = Counter({'E': 2})
        expected_basket = {'E': 2}
        self.cm.apply_free_discount(basket)
        assert basket == expected_basket        
