import itertools
import time
from collections import Counter


def read_baskets():
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
        baskets.append(list(map(int, basket)))

    return baskets


def Singleton_count(baskets, s):

    singletons = []

    for basket in baskets:
        for item in basket:
            singletons.append(item)

    singleton_counter = Counter(singletons)

    active = {}

    for (item, count) in singleton_counter.items():
        if count >= s:
            active[item] = count
    return active


def Candidate_count(baskets, candidate_length, items, singletons, support):

    # Generate candidates from previous frequent itemset and singletons
    candidates = {}
    for i in items:
        for singleton in singletons:
            if singleton[0] not in i:
                candidate = tuple(sorted(i + singleton))
                if candidate not in candidates:
                    candidates[candidate] = 0

    for basket in baskets:
        basket_variations = itertools.combinations(basket, candidate_length)
        for combination in basket_variations:
            if combination in candidates:
                candidates[combination] += 1
    x = {}
    for item in candidates:
        if candidates[item] >= support:
            x[item] = candidates[item]

    return x


def main():
    # constants
    support = 1000
    confidence_threshold = 0.5
    assocs = set()
    Itemsets = []

    #####
    # Using A-priori to find frequent itemsets
    #####

    baskets = read_baskets()
    Items = Singleton_count(baskets, support)
    Singletons = {(i, ): Items[i] for i in Items}
    Itemsets.append(Singletons)
    print("Frequent singletons are: {}".format(Singletons))
    k = 1

    # pass through the frequent itemsets and increment number of item in sets
    #stop when there are no frequent itemsets with k items
    while len(Itemsets[k - 1]) > 0:
        itemset = Candidate_count(baskets, k + 1, Itemsets[k - 1], Itemsets[0],
                                  support)
        Itemsets.append(itemset)
        print("Frequent " + str(k + 1) + "-tuples are: {}".format(Itemsets[k]))
        k += 1

    ######
    # Determining Associations
    ######

    for itemset in Itemsets[1:]:
        for k in itemset:
            #check for association for every item in frequent item sets
            for perm in itertools.permutations(k, len(k)):

                for arrow_pos in reversed(range(1, len(perm))):
                    lhs = k[:arrow_pos]

                    # get support for the quota
                    all_support = Itemsets[len(k) - 1][tuple(sorted(k))]
                    individual_support = Itemsets[len(lhs) - 1][tuple(
                        sorted(lhs))]

                    #calculate confidence
                    confidence = all_support / individual_support

                    #filter
                    if confidence >= confidence_threshold:
                        assocs.add(
                            (', '.join(map(str, sorted(perm[:arrow_pos]))) +
                             ' -> ' +
                             ', '.join(map(str, sorted(perm[arrow_pos:]))),
                             confidence))
                    else:
                        break

    print("Associations:", assocs)


start_time = time.time()
main()
print("Time: %s seconds" % (time.time() - start_time))
