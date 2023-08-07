n = int(input())
m = int(input())
arr = list(map(int,input().split()))

answer1 = 0

# n = 1 일때,, 시작점 잡아주는 느낌,,
if len(arr) == 1:
    answer1 = max(arr[0] - 0, n - arr[0])
# n > 1 일때
else:
    for i in range(len(arr)):
        # 시작점
        if i == 0:
            answer = arr[i]-0
        # 끝점
        elif i == len(arr)-1:
            answer = n-arr[i]
        # 중간지점(중요)
        else:
            check = (arr[i]-arr[i-1])
            if check%2:
                answer = check // 2 +1
            else:
                answer = check // 2
        answer1 = max(answer,answer1)
print(answer1)

