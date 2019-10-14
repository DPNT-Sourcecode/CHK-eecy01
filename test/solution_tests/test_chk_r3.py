from collections import Counter

from solutions.CHK import checkout_solution


class TestCheckoutMachine():

    @classmethod
    def setup_class(cls):
        products = checkout_solution.Products()
        discounts = checkout_solution.DiscountStore()
        cls.cm = checkout_solution.CheckoutMachine(products, discounts)
        
    def test_apply_free_discount_B1E2F3(self):
        basket = Counter({'B': 1, 'E': 2, 'F': 3})
        expected_basket = {'E': 2, 'F': 2}
        assert self.cm.apply_free_discount(basket) == expected_basket

    def test_apply_free_discount_B0E2F3(self):
        basket = Counter({'B': 0, 'E': 2, 'F': 3})
        expected_basket = {'E': 2, 'F': 2}
        assert self.cm.apply_free_discount(basket) == expected_basket    
        
    def test_apply_free_discount_B2E2F1(self):
        basket = Counter({'B': 2, 'E': 2, 'F': 1})
        expected_basket = {'B': 1, 'E': 2, 'F': 1}
        assert self.cm.apply_free_discount(basket) == expected_basket
        
    def test_apply_free_discount_B2E2F2(self):
        basket = Counter({'B': 2, 'E': 2, 'F': 2})
        expected_basket = {'B': 1, 'E': 2, 'F': 2}
        assert self.cm.apply_free_discount(basket) == expected_basket

    def test_apply_free_discount_B2E2F3(self):
        basket = Counter({'B': 2, 'E': 2, 'F': 3})
        expected_basket = {'B': 1, 'E': 2, 'F': 2}
        assert self.cm.apply_free_discount(basket) == expected_basket

    def test_apply_free_discount_F4(self):
        basket = Counter({'F': 4})
        expected_basket = {'F': 3}
        assert self.cm.apply_free_discount(basket) == expected_basket

    def test_apply_free_discount_F5(self):
        basket = Counter({'F': 5})
        expected_basket = {'F': 4}
        assert self.cm.apply_free_discount(basket) == expected_basket

    def test_apply_free_discount_F6(self):
        basket = Counter({'F': 6})
        expected_basket = {'F': 4}
        assert self.cm.apply_free_discount(basket) == expected_basket

    def test_apply_free_discount_F7(self):
        basket = Counter({'F': 7})
        expected_basket = {'F': 5}
        assert self.cm.apply_free_discount(basket) == expected_basket
        
    def test_get_total_price_B1E2F3(self):
        basket = Counter({'B': 1, 'E': 2, 'F': 3})
        assert self.cm.get_total_price(basket) == 100

    def test_get_total_price_B0E2F3(self):
        basket = Counter({'B': 0, 'E': 2, 'F': 3})
        assert self.cm.get_total_price(basket) == 100
        
    def test_get_total_price_B2E2F1(self):
        basket = Counter({'B': 2, 'E': 2, 'F': 1})
        assert self.cm.get_total_price(basket) == 120
        
    def test_get_total_price_B2E2F2(self):
        basket = Counter({'B': 2, 'E': 2, 'F': 2})
        assert self.cm.get_total_price(basket) == 130

    def test_get_total_price_B2E2F3(self):
        basket = Counter({'B': 2, 'E': 2, 'F': 3})
        assert self.cm.get_total_price(basket) == 130

    def test_get_total_price_F4(self):
        basket = Counter({'F': 4})
        assert self.cm.get_total_price(basket) == 30

    def test_get_total_price_F5(self):
        basket = Counter({'F': 5})
        assert self.cm.get_total_price(basket) == 40

    def test_get_total_price_F6(self):
        basket = Counter({'F': 6})
        assert self.cm.get_total_price(basket) == 40

    def test_get_total_price_F7(self):
        basket = Counter({'F': 7})
        assert self.cm.get_total_price(basket) == 50