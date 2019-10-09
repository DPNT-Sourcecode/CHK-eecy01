
from collections import Counter

PRICES = {'A': 50, 'B': 30, 'C': 20, 'D': 15}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not skus or not str.isalpha(skus):
        return -1
    skus = skus.upper()
    
    skus_counter = Counter(skus)
    skus_sum = sum(map(count_price, skus_counter))
    return skus_counter

def count_price(item, item_count):
    return PRICES[item] * item_count
