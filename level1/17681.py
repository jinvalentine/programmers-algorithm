# https://school.programmers.co.kr/learn/courses/30/lessons/17681

def ten_two(num):
    b = format(num, 'b')
    return b

def solution(n, arr1, arr2):
    
    answer = []
    
    for i in zip(arr1, arr2):
        
        tmp = ""
        
        a, b = i
        a = format(a, 'b') 
        b = format(b, 'b')   
        result = int(a) + int(b)
        
        for i in str(result):

            if i != '0':
                tmp += "#"
            else:
                tmp += " "
        
        while len(tmp) < n:
            tmp = " " + tmp
            
        answer.append(tmp)
        
    return answer
