class Solution:
    def isAnagram(self, string1, string2):
        if len(string1) != len(string2):
            return False
        
        count = [0]*26
        for i in range(len(string1)):
            count[ord(string1[i]) - ord('a')] += 1
            count[ord(string2[i]) - ord('a')] -= 1
        
        for i in count:
            if i != 0:
                return False
        
        return True


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        

        output = [[strs[0]]] #put in first string
        for i in range(1, len(strs)):
            word = strs[i]
            
            new = True
            for anagram in output:
                if self.isAnagram(word, anagram[0]):
                    anagram.append(word)
                    new = False
                    break
            if new == True:    
                output.append([word])

        return output
                
            


    