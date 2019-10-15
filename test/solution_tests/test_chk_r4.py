from collections import Counter

from solutions.CHK import checkout_solution


class TestCheckoutMachine():

    @classmethod
    def setup_class(cls):
        products = checkout_solution.Products()
        discounts = checkout_solution.DiscountStore()
        cls.cm = checkout_solution.CheckoutMachine(products, discounts)

    def test_apply_free_discount_E2F7N3R3U4Q4M2B3A5(self):
        basket = Counter({'E': 2, 'F': 7, 'N': 3, 'R': 3, 'U': 4, 'Q': 4, 'M': 2, 'B': 3, 'A': 5})
        expected_basket = {'E': 2, 'F': 5, 'N': 3, 'R': 3, 'U': 3, 'Q': 3, 'M': 1, 'B': 2, 'A': 5}
        assert self.cm.apply_free_discount(basket) == expected_basket    
        
    def test_get_total_price_E2F7N3R3U4Q4M2B3A5(self):
        basket = Counter({'E': 2, 'F': 7, 'N': 3, 'R': 3, 'U': 4, 'Q': 4, 'M': 2, 'B': 3, 'A': 5})
        # expected_basket = {'E': 2, 'F': 5, 'N': 3, 'R': 3, 'U': 3, 'Q': 3, 'M': 1, 'B': 2, 'A': 5}
        # expected price: 2*40 + 5*10 + 3*40 + 3*50 + 3*40 + 80 (Q3) + 1*15 + 45 (2B) + 200 (A5)
        #                           = 80 + 50    + 120   + 150  + 120   + 80         + 15     + 45        + 200 =
        assert self.cm.get_total_price(basket) == 860
