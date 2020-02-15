#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    # find two items who's weights equal the limit

    # loop thtought the array of items
    for index in range(length):
        dif = limit - weights[index]
        if hash_table_retrieve(ht, dif) is not None:
            x = index
            y = hash_table_retrieve(ht, dif)
            if x > y:
                return (x, y)
            else:
                return (y, x)
        hash_table_insert(ht, weights[index], index)

    return None

    # for w in range(length):
    #     i = weights.index(w)
    #     current = weights[i]
    #     if weights[i+1] is not None:
    #         next_i = weights[i+1]
    #     # Return answer as a tuple, (heavier index, lighter index)
    #         if current + next_i is limit:
    #             return (weights.index(current), weights.index(next_i))


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
