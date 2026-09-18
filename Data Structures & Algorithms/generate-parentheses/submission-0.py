class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(closey, openy):
            if closey == openy == n:
                res.append("".join(stack))
                return


            if openy < n:
                stack.append("(")
                backtrack(closey, openy + 1)
                stack.pop()

            if closey < openy:
                stack.append(")")
                backtrack(closey+1, openy)
                stack.pop()

        backtrack(0,0)

        return res 
