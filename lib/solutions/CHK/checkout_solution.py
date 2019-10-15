
from collections import Counter



# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not skus:
        return 0
    if not str.isalpha(skus) or not str.isupper(skus):
        return -1
    
    skus = skus.upper()
    
    basket = Counter(skus)
    cm = CheckoutMachine(Products(), DiscountStore())
    total_price = cm.get_total_price(basket)
    return total_price

class Products():
    PRODUCT_PRICES = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G': 20,
                                    'H': 10, 'I': 35, 'J': 60, 'K': 70, 'L': 90, 'M': 15, 'N': 40,
                                    'O': 10, 'P': 50, 'Q': 30, 'R': 50, 'S': 20, 'T': 20, 'U': 40,
                                    'V': 50, 'W': 20, 'X': 17, 'Y': 20, 'Z': 21}

    def get_price(self, sku):
        return self.PRODUCT_PRICES.get(sku, 0)

    def get_skus(self):
        return self.PRODUCT_PRICES.keys()


class DiscountStore():
    n_for_price = {'A': {3: 130, 5: 200},  # 3A for 130, 5A for 200
                            'B': {2: 45},
                            'H': {5: 45, 10: 80},  # 5Hfor 45, 10H for 80
                            'K': {2: 120},  # 2K for 120
                            'P': {5: 200},  # 5P for 200
                            'Q': {3: 80},  # 3Q for 80
                            'V': {2: 90, 3: 130}  # 2V for 90, 3V for 130
                   }
    n_for_price_keys = n_for_price.keys()

    xfree_for_y = {'E': {2: {'B': 1}},  # 2E get one B free
                            'F': {2: {'F': 1}},  # 2F get one F free
                            'N': {3: {'M': 1}},  # 3N get one M free
                            'R': {3: {'Q': 1}},  # 3R get one Q free
                            'U': {3: {'U': 1}},  # 3U get one U free
                   }

    any_for_price = {('S', 'T', 'X', 'Y', 'Z'): {3: 45}}  # buy any 3 of (S, T, X, Y, Z) for 45
    #any_for_price_keys = any_for_price.keys()

class CheckoutMachine():
    
    def __init__(self, products, discounts):
        self.products = products
        self.discounts = discounts

    def count_price(self, checkout_item):
        # checkout_item - tuple of (item, count)
        item = checkout_item[0]
        item_count = checkout_item[1]
        if item not in self.products.get_skus():
            return 0
        total_price = 0
        promotion_price = 0
        remainder = item_count
        if item in self.discounts.n_for_price_keys:
            for item_quantity in sorted(self.discounts.n_for_price[item].keys(), reverse=True):
                if remainder >= item_quantity:
                    promotion_price += int(remainder / item_quantity) * self.discounts.n_for_price[item][item_quantity]
                    remainder = remainder % item_quantity
        total_price = promotion_price + self.products.get_price(item) * remainder
        return total_price    

    def apply_free_discount(self, basket):
        products = set(basket.keys())
        all_free_discount_prods = set(self.discounts.xfree_for_y.keys())
        free_discount_prods = products & all_free_discount_prods
        actual_discounts = {}
        for discount_prod in free_discount_prods:
            free_discount_for_product = self.get_free_discount_for_product(discount_prod, basket)
            if free_discount_for_product:
                actual_discounts.update(free_discount_for_product)
        actual_discounts = Counter(actual_discounts)
        return basket - actual_discounts

    def get_free_discount_for_product(self, discount_prod, basket):
        discount = self.discounts.xfree_for_y[discount_prod]
        for discount_quantity in discount.keys():
            if basket[discount_prod] >= discount_quantity:
                free_discount_item = discount[discount_quantity].copy().popitem()
                if discount_prod != free_discount_item[0]:
                    return self.free_discount_for_other_product(discount_quantity, basket, discount_prod, discount, free_discount_item)
                else:
                    return self.free_discount_for_self_product(discount_quantity, basket, discount_prod, discount, free_discount_item)

    def free_discount_for_other_product(self, discount_quantity, basket, discount_prod, discount, free_discount_item):
        multiple = int(basket[discount_prod] / discount_quantity)
        return {free_discount_item[0]: free_discount_item[1] * multiple}

    def free_discount_for_self_product(self, discount_quantity, basket, discount_prod, discount, free_discount_item):
        discount_quantity += free_discount_item[1]
        multiple = int(basket[discount_prod] / discount_quantity)
        return {free_discount_item[0]: free_discount_item[1] * multiple}        

    def apply_group_discount(self, basket):
        products = set(basket.keys())
        all_group_discount_prods = set(self.discounts.any_for_price.keys())
        discount_prods = products & all_group_discount_prods
        actual_discounts = {}
        return basket - actual_discounts

    def get_total_price(self, basket):
        # internal basket for discounts and other operations
        cm_basket = basket.copy()
        cm_basket = self.apply_free_discount(cm_basket)
        cm_basket = self.apply_group_discount(cm_basket)
        total_price = sum(map(self.count_price, cm_basket.items()), 0)
        return total_price


