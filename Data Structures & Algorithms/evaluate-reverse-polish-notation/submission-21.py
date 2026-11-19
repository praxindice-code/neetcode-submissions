class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        debug = []
        queue = []
        ans = 0 
        for i in range(len(tokens)):
            if tokens[i] not in ["+","-","/","*"]:
                queue.append((tokens[i]))

            else:
                if tokens[i] == "+":
                    temp = int(queue[-1]) + int(queue[-2])

                    queue.pop()
                    queue.pop()
                    queue.append(temp)
                elif tokens[i] == "-":
                    temp = int(queue[-2]) - int(queue[-1])

                    queue.pop()
                    queue.pop()
                    queue.append(temp)
                elif tokens[i] == "*":
                    temp = int(queue[-1]) * int(queue[-2])

                    queue.pop()
                    queue.pop()
                    queue.append(temp)
                elif tokens[i] == "/":
                    temp = int(queue[-2]) / int(queue[-1])

                    queue.pop()
                    queue.pop()
                    queue.append(temp)


        return int((queue[0]))