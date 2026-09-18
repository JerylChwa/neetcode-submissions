class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def max_amount_no_limit(sub_nums: List[int]) -> int:
            # dp[i] = max amount stolen up to house i
            # dp[i] = max(nums[i] + dp[i-2], dp[i-1])
            two_back = 0
            one_back = 0

            for i in range(len(sub_nums)):
                temp = max(
                    sub_nums[i] + two_back,
                    one_back
                )
                two_back, one_back = one_back, temp
                print(two_back, one_back)
            
            return one_back
                
        return max(
            max_amount_no_limit(nums[1:]),
            max_amount_no_limit(nums[:-1])
        )



        
        