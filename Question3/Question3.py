def solution(N,M,P):
    # check if list is already sorted 
    if sorted(P) == P:
        return 1

    # check if it is impossible to swap any number
    impossible = True 
    for i in range(N-1):
        if P[i] + P[i+1] <= M:
            impossible = False
            break
    if impossible:
        return 0
    
    # check if it possible to swap every number in the list
    if max(P)+ sorted(P)[-2] < M:
        return 1     

    # use a modified bubble sort to decide if any of the previous do not work
    swapped = False
    # Looping from size of array from last index[-1] to index [0]
    for n in range(N-1, 0, -1):
        for i in range(n):
            if P[i] > P[i + 1]:
                if P[i] + P[i + 1] <= M:
                    swapped = True
                    P[i], P[i + 1] = P[i + 1], P[i]
                else:
                    return 0       
        if not swapped:
            # exiting the function if we didn't make a single swap
            # meaning that the array is already sorted.
            return 1
    
    return 1



"""
def main():
    N,M=map(int,input().split())
    P=list(map(int,input().split()))
    print(solution(N,M,P))
  

if __name__ == '__main__':
    main()
"""


print(solution(4, 1, [2,1,3,4]))
print(solution(4, 1, [1,2,3,4]))
print(solution(5, 7, [3,2,2,3,3]))
