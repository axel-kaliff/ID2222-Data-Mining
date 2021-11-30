



#how do we solve so that the hash function maps to at least log2n bits?

def fm(stream):

    max_trailing_zeroes = 0

    for i in range(0, len(stream)):

       #hash function with form ax + b mod c
       hashed_value = bin((2 * stream[i] + 7) % 32)[2:]

       #count the trailing zeroes
       sum = 0

       for j in reversed(range(0, len(hashed_value)-1)):
            if hashed_value[j] == '0':
                sum += 1
            else:
                break

       if sum > max_trailing_zeroes:
            max_trailing_zeroes = sum

    return max_trailing_zeroes


def main():
    result = fm([1,2,3,4,5,6,76,9])
    print(result)

main()