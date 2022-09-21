import string

s = "one4seveneight"

def solution(s):
    
    tmp = ""
    
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    answer = []
    
    for i in s:
        if i in string.ascii_lowercase:
            tmp += i
        
            if tmp in nums:
                n = nums.index(tmp)
                tmp = ""
                answer.append(n)
            
        elif i in string.digits:
            answer.append(i)
    
    answer = ''.join(map(str, answer))
            
    return int(answer)

print(solution(s))