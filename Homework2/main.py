from collections import Counter
from itertools import combinations

def apriori(s, baskets):

    # storing counts as triplets
    singletons = []

    # first pass
    for basket in baskets:
        for item in basket:
            singletons.append(item)

    singleton_counter = Counter(singletons)

    active = {}

    # between passes
    for (item, count) in singleton_counter.items():
        if count >= s:
            active[item] = count

# second pass
    pair_support = {}
    for basket in baskets:
        frequent_items_in_basket = []
        for item in basket:
            if item in active.keys():
                frequent_items_in_basket.append(item)

        # generate pairs
        basket_pairs = [i for i in combinations(frequent_items_in_basket, 2)]

        # count how many times pairs occurs in baskets
        for pair in basket_pairs:
            pair_support[pair] = pair_support.get(pair, 0) + 1

    print(pair_support)

def main():

    baskets = []

    reader = open('T10I4D100K.dat', 'r', encoding='utf-8', errors='ignore')
    data_file = reader.read()

    lines = data_file.split("\n")

    for line in lines:
        basket = []
        items = line.split(" ")
        for item in items:
            if item != '':
                basket.append(int(item))
        baskets.append(basket)

    apriori(1000, baskets)


main()
