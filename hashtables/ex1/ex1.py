#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
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

def get_indices_of_item_weights_(weights, length, limit):
    ht = HashTable(16)

    prev_weight = -1
    hash_table_insert(ht, weights[0], (0, limit - weights[0]))
    for i in range(1, length):
        curr_weight = weights[i]
        curr_needed = limit - curr_weight
        hash_table_insert(ht, curr_weight, (i, curr_needed))
        if prev_weight == curr_needed:
            pass

        prev_weight = curr_weight
    pass

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
