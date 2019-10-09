
from collections import Counter

PRICES = {'A': 50, 'B': 30, 'C': 20, 'D': 15}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not skus or not str.isalpha(skus):
        return -1
    skus = skus.upper()
    
    skus_counter = Counter(skus)
    skus_sum = sum(map(count_price, skus_counter.items()))
    return skus_counter

def count_price(checkout_item):
    # checkout_item - tuple of (item, count)
    print(checkout_item)
    return PRICES[checkout_item[0]] * checkout_item[1]



