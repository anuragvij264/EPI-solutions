from typing import List

from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    # TODO - you fill in here.
    import heapq
#     [0,5,8]  [1,4,5,8] [2,3,4,5,6]
#
# 0,1,2
# -> create a min heap (O(log(k)))
# -> extract min O(1) operation
# -> extract 0, recreate heap or do heapify   --- result = [0]
# ->  0 came from Array1 so push 5 into heap.. heap has 1,2,5
# -> extract min 1 and push 4 --- result = [0,1] ,heap = 2,5,4
# -> extract 2 and push 5 == result = [0,1,2], heap = 5,5,4
# --> extract 5 and push 8 == result  = [0,1,2,5] heap = 5,4,8

    result = list()
    # heap = [(j[0],i) for i,j in enumerate(sorted_arrays)]
    # heapq.heapify(heap)

    # iterators being helpful here to iterate over sorted_arrays
    sorted_array_iters = [iter(i) for i in sorted_arrays]
    heap = [(next(j,None),i)for i,j in enumerate(sorted_array_iters) if j is not None]
    heapq.heapify(heap)

    # result.append(heapq.heappop(heap))

    while heap:
        lowest_item ,arr_index= heapq.heappop(heap)
        try:
            next_element = next(sorted_array_iters[arr_index],None)
            if next_element is not None:
                heapq.heappush(heap, (next_element, arr_index))
            result.append(lowest_item)
        except:
            pass

    return result









if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
