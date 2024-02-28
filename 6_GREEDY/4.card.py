def solution(nums, k):
    answer = 0
    
    total = 0
    sum=0
    #nums.sort(reverse=True)
    #print(nums)
    #for i in nums:
    #    a +=1
    #    if a > k:
    #        break
    #    answer += i     
    n=len(nums)
    
    for i in range (k+1):
        sum=0
        for j in range (i):
            sum+=nums[j]
        for j in range (n-k+i,n) :
            sum+=nums[j]
        
        answer=max(answer,sum)
        
    return answer

print(solution([2, 3, 7, 1, 2, 1, 5], 4))
print(solution([1, 2, 3, 5, 6, 7, 1, 3, 9], 5))
print(solution([1, 30, 3, 5, 6, 7], 3))
print(solution([1, 2, 15, 3, 6, 7, 8, 9], 5))
print(solution([12, 5, 6, 12, 34, 35, 13, 3, 7, 8, 9], 7))