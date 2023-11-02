import functools

class Solution(object):
    def containsDuplicate(self, nums):
        table = {}
        for num in nums:
            if table.get(num):
                return True
            table.update({num: True})
        return False
    
    def isAnagram(self, s, t):
        d1, d2 = {}, {}
        for c in s:
            d1[c] = d1.get(c, 0) + 1
        for c in t:
            d2[c] = d2.get(c, 0) + 1
        return d1 == d2

    def twoSum(self, nums, target):
        d1 = {}
        for i in range(0, len(nums)):
            val = nums[i]
            required = target - val
            index = d1.get(required, -1)
            if index != -1:
                return [index, i]
            d1.update({val: i})

    def groupAnagrams(self, strs):
        d = {}
        for word in strs:
            key = "".join(sorted(word))
            d[key] = d.get(key, []) + [word]
        
        return d.values()

    def topKFrequent(self, nums, k):
        d ={}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        items = d.items()
        items.sort(key=(lambda elem: elem[1]), reverse=True)
        return map((lambda elem: elem[0]), items[:k])

    def productExceptSelf(self, nums):
        # total = functools.reduce(lambda a,b: a*b, nums)
        # return map(lambda val: total / val, nums)
        l = map(
            lambda i: functools.reduce(
                lambda a,b: a*b, nums[:i], 1
                ) * functools.reduce(
                lambda a,b: a*b, nums[i+1:], 1
                ), list(range(0, len(nums)))
            )
        return l



if __name__ == "__main__":
    sol = Solution()
    # assert(sol.containsDuplicate([1,2,3,1]) == True)
    # assert(sol.containsDuplicate([1,2,3,4]) == False)
    # assert(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True)
    # assert(sol.isAnagram("anagram", "nagaram") == True)
    # assert(sol.isAnagram("vat", "cat") == False)
    # print sol.twoSum([2,7,11,15], 9)
    # assert(sol.twoSum([2,7,11,15], 9) == [0,1])
    # assert(sol.twoSum([3,2,4], 6) == [1,2])
    # assert(sol.twoSum([3,3], 6) == [0,1])
    # assert(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [['ate', 'tea', 'eat'], ['nat', 'tan'], ['bat']])
    # assert(sol.groupAnagrams([""]) == [[""]])
    # assert(sol.groupAnagrams(["a"]) == [["a"]])
    # assert(sol.topKFrequent([1,1,1,2,2,3], 2) == [1,2])
    # assert(sol.topKFrequent([1], 1) == [1])
    print str(sol.productExceptSelf([1,2,3,4]))
    print str(sol.productExceptSelf([-1,1,0,-3,3]))
    