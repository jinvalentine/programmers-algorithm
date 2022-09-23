# s, d, t -> 1, 2, 3 제곱
# *는 바로 전 얻은 점수와 해당 점수 각 2배
# #는 해당 점수 마이너스

# * 첫번쨰에 나오면 해당 점수 2배

def solution(dartResult):
    stack = []
    dartResult = dartResult.replace("10", "A")
    bonus = {'S': 1, 'D': 2, 'T': 3}
    
    for i in dartResult:
        if i. isdigit() or i=="A":
            stack.append(10 if i == "A" else int(i))
        elif i in ('S', 'D', 'T'):
            num = stack.pop()
            stack.append(num ** bonus[i])
        elif i == '#':
            stack[-1] *= -1
        elif i == '*':
            num = stack.pop()
            if len(stack): # 바로 전과 해당 점수 각 2배이기에
                stack[-1] *= 2
            stack.append(2 * num) # 처음에 pop했던 값 2배해서 다시 넣기
    return sum(stack)

