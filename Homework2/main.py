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

    frequent_singletons = {}

    # between passes

    for (item, count) in singleton_counter.items():
        if count >= s:
            frequent_singletons[item] = count


# print(frequent_singletons)
# second pass
    pair_support = []
    for basket in baskets:

        # print(basket)
        frequent_items_in_basket = []
        for item in basket:
            if item in frequent_singletons.keys():
                frequent_items_in_basket.append(item)

        # generate pairs
        basket_pairs = [i for i in combinations(frequent_items_in_basket, 2)]

        # count how many times pairs occurs in baskets
        for pair in basket_pairs:
            pair_support.append([pair[0], pair[1], 0])

    for pair in pair_support:
        for basket in baskets:
            if pair[0] in basket and pair[1] in basket:
                pair[2] += 1



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

    apriori(500, baskets)


main()
