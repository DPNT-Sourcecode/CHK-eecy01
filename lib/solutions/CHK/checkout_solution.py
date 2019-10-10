
from collections import Counter



# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not skus:
        return 0
    if not str.isalpha(skus) or not str.isupper(skus):
        return -1
    skus = skus.upper()
    
    skus_counter = Counter(skus)
    skus_sum = sum(map(count_price, skus_counter.items()), 0)
    return skus_sum

def count_price(checkout_item):
    # checkout_item - tuple of (item, count)
    item = checkout_item[0]
    item_count = checkout_item[1]
    if item not in PRICES.keys():
        return 0
    total_price = 0
    promotion_price = 0
    remainder = item_count
    if item in DiscountStore.n_for_price_keys and item_count >= DiscountStore.n_for_price[item][0]:
        promo_count = DiscountStore.n_for_price[item][0]
        remainder = item_count % promo_count
        promotion_price = int(item_count / promo_count) * DiscountStore.n_for_price[item][promo_count]
    total_price = promotion_price + Products.get_price(item) * remainder
    return total_price

class Products():
    PRODUCT_PRICES = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
    @classmethod
    def get_price(cls, sku):
        return cls.PRODUCT_PRICES[sku]

class DiscountStore():
    n_for_price = {'A': {3: 130},
                            'B': {2: 45},
                   }
    n_for_price_kes = n_for_price.keys()
    SPECIAL_OFFER_KEYS = SPECIAL_OFFER.keys()
    
