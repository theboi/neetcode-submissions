class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        tab = {}
        for i in range(len(numbers)):
            n = numbers[i]
            if n in tab: return [tab[n]+1, i+1]
            tab[target-n]=i