N = 5

stages = [2, 1, 2, 6, 2, 4, 3, 3]

def solution(N, stages):
    answer = {}
    member = len(stages)

    for stage in range(1, N + 1):
        if member != 0:
            count = stages.count(stage)
            answer[stage] = count / member
            member -= count
        else:
            answer[stage] = 0
            
    return sorted(answer, key= lambda x: answer[x], reverse=True)
    
print(solution(N, stages))


''' 
    정답률 70%로 떴던 풀이
    # N까지 스테이지를 모두 완료했을 경우 N+1 스테이지도 있기 때문에
    dp = [0] * (N + 2)
    
    result = [] # 스테이지별 확률과 순서를 넣는 리스트
    answer = [] # 마지막 순서를 넣는 리스트
    all_mem = len(stages)
    for i in range(all_mem):
        dp[stages[i]] += 1 
    
    for i in range(1, N + 1):
        all_mem = all_mem - dp[i - 1]
        result.append((dp[i] / all_mem , i))
    
    result.sort(key= lambda x : (-x[0], x[1]))
    
    for i in range(len(result)):
        answer.append(result[i][1])
    
    return answer
'''