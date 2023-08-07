
# 하나씩 넣을때마다 갯수 체크할까,,
# n이 총 개수 , k가 허용가능한 개수
# 이게아니었고,, 시작점이 중요한거,, 그 시작점부터 가장 큰 부분수열,,구하는거

# cnt = 0
# max_cnt = 0
# answer_dict = {}
# for i in range(n):
#     if arr[i] in answer_dict:
#         if answer_dict[arr[i]]+1 > k:
#             break
#         else:
#             answer_dict[arr[i]] += 1
#             cnt += 1
#     else:
#         answer_dict[arr[i]] = 1
#         cnt += 1
# max_cnt = (max_cnt,cnt)

n, k = map(int,input().split())
arr = list(map(int,input().split()))

# 투포인터로 풀어볼게요,,
left,right = 0,0 # 처음엔 0부터 시작합시다..
counter = [0]*(max(arr)+1) # 항목 개수세어줄 리스트
answer = 0 # 답

while right < n: # 배열 끝까지 갈때까지할건데,,
    if counter[arr[right]]<k: # k보다 작다면
        counter[arr[right]] += 1
        right += 1
    else: # k보다커져버렸다면,, 이제 left를 한칸땡겨요
        counter[arr[left]] -= 1 # 이건빼줘야겠져
        left += 1
    answer = max(answer, right-left) #이게 답
print(answer)
