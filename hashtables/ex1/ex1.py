#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights_(weights, length, limit):
    ht = HashTable(16)

    for i in range(length):
        hash_table_insert(ht, i, (weights[i], limit-weights[i]))

    for i in range(length):
        weight, needed_weight = hash_table_retrieve(ht, i)

        for j in range(i+1, length):
            weight, _ = hash_table_retrieve(ht, j)
            if weight==needed_weight:
                if i > j:
                    return (i, j)
                else:
                    return (j, i)

    return None

def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i in range(length):
        weight = weights[i]
        hash_table_insert(ht, weight, i)

    for i in range(length):
        weight = weights[i]
        idx = hash_table_retrieve(ht, weight)
        needed_weight = limit - weight
        idx2 = hash_table_retrieve(ht, needed_weight)

        if idx2:

            if idx > idx2:
                return (idx, idx2)
            else:
                return (idx2, idx)

    return None

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
