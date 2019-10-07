# Time: O(nlog(k))
# Space: O(k)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    import heapq
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        min_heap = []

        for index,file in enumerate(lists):
            if file:
                cur_val = file.val
                lists[index] = lists[index].next
                min_heap.append((cur_val, index))

        heapq.heapify(min_heap)

        merged_data = ListNode('#')  # dummy head

        temp_head = merged_data
        while min_heap:
            min_val, index = heapq.heappop(min_heap)
            temp_node = ListNode(min_val)
            temp_head.next = temp_node
            temp_head = temp_head.next
            cur_head = lists[index]
            if cur_head:
                cur_val = cur_head.val
                lists[index] = lists[index].next
                heapq.heappush(min_heap, (cur_val,index))

        return merged_data.next
