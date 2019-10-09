
from collections import Counter

PRICES = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
SPECIAL_OFFER = {'A3': 130, 'B2': 45}
SPECIAL_OFFER_KEYS = SPECIAL_OFFER.keys()

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not skus or not str.isalpha(skus):
        return -1
    skus = skus.upper()
    
    skus_counter = Counter(skus)
    skus_sum = sum(map(count_price, skus_counter.items()))
    return skus_sum

def count_price(checkout_item):
    # checkout_item - tuple of (item, count)
    total_price = 0
    promotion_price = 0
    item = checkout_item[0]
    item_count = checkout_item[1]
    if item in SPECIAL_OFFER_KEYS[0] and item_count >= int(SPECIAL_OFFER_KEYS[1:]):
        promo_count = int(SPECIAL_OFFER_KEYS[1:])
        
    total_price = promotion_price + PRICES[item] * remainder
    return total_price

