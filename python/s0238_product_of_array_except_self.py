class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = 1, 1
        res = [1] * len(nums)

        for i in range(len(nums)): 
            res[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res

    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     prefix = [1]
    #     suffix = 1

    #     # let prefix be the positive multiplication cache 
    #     for i in range(len(nums) - 1): 
    #         prefix.append(prefix[i] * nums[i])

    #     # the suffix multiplication need to get the last answer "result[0]"
    #     # we should make the suffix to do more one loop to make its length to len(nums) + 1
    #     # it won't lead to out of range, because the edge of this loop will be prefix[-len(nums)] == prefix[0]
    #     for i in range(len(nums)): 
    #         prefix[-i - 1] = prefix[-i - 1] * suffix
    #         suffix *= nums[-i - 1]
        
    #     return prefix

    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     prefix = [1]
    #     suffix = [1]
    #     res = []

    #     # multiply "index - 1"th element of prefix list by the "index - 1"th element of nums list
    #     # to get the prefix of "index"th element of nums list
    #     for i in range(len(nums) - 1): 
    #         prefix.append(prefix[i] * nums[i])
    #         suffix.append(suffix[i] * nums[-i - 1])

    #     for i in range(len(nums)):
    #         res.append(prefix[i] * suffix[-i - 1])
        
    #     return res