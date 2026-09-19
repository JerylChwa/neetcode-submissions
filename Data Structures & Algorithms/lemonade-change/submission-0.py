"""
$5 -> No problem
$10 -> Give $5 back
$20 -> Give back $15


$15 
-> $10 + $5
-> $5 + $5 + $5

Try to spend the 10 to maximise the number of 5s we have remaining


"""

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        freq = {
            5 : 0,
            10 : 0,
            20 : 0
        }

        for bill in bills:
            if bill == 5:
                freq[5] += 1
            elif bill == 10:
                if freq[5] == 0:
                    return False
                freq[5] -= 1
                freq[10] += 1
            elif bill == 20:
                # first check 10 + 5, then check 5,5,5
                if freq[10] > 0 and freq[5] >0:
                    freq[10] -= 1
                    freq[5] -= 1                    
                elif freq[5] >= 3:
                    freq[5] -= 3
                else:
                    return False
                    
                freq[20] += 1

        return True
        