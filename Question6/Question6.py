def get_order(flows, index):
    class_set = [index]
    n = 1
    i =  flows[index] - 1
    while index != i:
        class_set.append(i)
        i = flows[i] - 1
        n += 1

    return n, class_set


def solution(n, flows):
    indices = list(range(n))
    results = [0 for i in range(n)]
    
    while len(indices) != 0:
        index = indices[0]
        power, class_set = get_order(flows, index)
        indices = list(set(indices) - set(class_set))
        for i in class_set:
            results[i] = power
        
    
    results = [str(a) for a in results]
    print(" " . join(results)) 
    return results
"""

def main():
    n = int(input())
    flows = list(map(int, input().split()))
    solution(n, flows)


if __name__ == '__main__':
    main()

"""
print(solution(3, [2,3,1]))
print(solution(5, [1,2,3,4,5]))
print(solution(6, [4,6,1,3,5,2]))
