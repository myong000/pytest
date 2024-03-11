from collections import deque
def solution(nums):
    answer = 0

    a=len(nums)
    
    array = deque()

    for x in range(0,a):
        array.append(nums[x])
        
    while a > 3:
        array.popleft()
        array.popleft()
        array.append(array[0])
        array.popleft()
      
        a -= 2
        
    answer = array[a-1]

    
        
    

    return answer
            
print(solution([3, 1, 4, 5, 2, 6, 7]))
print(solution([10, 8, 3, 1, 4, 5, 2, 6, 7, 9]))
print(solution([10, 8, 3, 11, 12, 1, 4, 5, 2, 6, 7, 9]))
print(solution([10, 8, 3, 1, 4, 5, 2, 11, 13, 6, 7, 12, 9, 14]))
print(solution([1, 8, 6, 10, 4, 7, 2, 5, 3, 9]))
