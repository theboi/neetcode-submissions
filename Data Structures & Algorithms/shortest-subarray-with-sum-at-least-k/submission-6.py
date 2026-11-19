from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        queue = deque()
        sumnow = 0
        res = -1
        for i in range(len(nums)):
            if i==0 or sumnow<k or (nums[i]>=nums[i-1] or (nums[i]<nums[i-1] and len(queue) <= 1)):
                queue.append(nums[i])
                sumnow += nums[i]
            else:
                while len(queue)>1:
                    val = queue.popleft()
                    sumnow -= val
                    if sumnow>=k: res = min(len(queue), res) if res != -1 else len(queue)
                queue.append(nums[i])
                sumnow += nums[i]
            if sumnow>=k: res = min(len(queue), res) if res != -1 else len(queue)
        while len(queue) != 0:
            val = queue.popleft()
            sumnow -= val
            if sumnow>=k: res = min(len(queue), res) if res != -1 else len(queue)
        return res
#[3,5,7,8,0,-2,1]
#[-10,-5,-3,-7,0]