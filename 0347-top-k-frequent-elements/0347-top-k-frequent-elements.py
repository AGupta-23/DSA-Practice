class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Step 1: Count frequency of each number
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Step 2: Create buckets
        # index = frequency
        # bucket[f] = numbers having frequency f
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        # Step 3: Traverse buckets from highest frequency
        result = []

        for f in range(len(buckets) - 1, 0, -1):
            for num in buckets[f]:
                result.append(num)

                # We only need k elements
                if len(result) == k:
                    return result