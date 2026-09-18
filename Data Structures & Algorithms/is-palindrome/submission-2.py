class Solution:
    def isPalindrome(self, s: str) -> bool:
        # make string lowercase and remove non-alphanumeric
        result = []
        for letter in s:
            if letter.isalnum():
                result.append(letter.lower())

        # use 2 pointer approach
        left = 0
        right = len(result) - 1

        print(result)

        while left < right:
            if result[left] != result[right]:

                return False
            left += 1
            right -= 1
        
        

        return True
