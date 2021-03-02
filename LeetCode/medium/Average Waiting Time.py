class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        waiting_time = 0
        cooked = 0
        for arr, time in customers:
            cooked = max(arr, cooked) + time
            waiting_time += cooked - arr

        return waiting_time / float(len(customers))