def solution(cutoffScore, scoresLength, scores):
    n = scoresLength
    limit = cutoffScore
    first = 0
    last = 0
    result = 0
    sum = scores[0]

    if limit == 0:
        return 0

    while (first < n and last < n) :
        # if the sum is less than the limit we make the subarray bigger 
        # and update the result and sum
        if (sum < limit):
            last += 1

            if (last >= first):
                result += last - first

            # avoid overflow
            if (last < n):
                sum += scores[last]

        # if the sum is bigger than the limit we make the subarray smaller 
        # again and update the sum
        else:
            sum -= scores[first]
            first += 1

    return result


"""
def main():
    cutoffScore = int(input().split()[0])
    scoresLength = int(input().split()[0])
    scores = [int(x) for x in input().split()]
    result = solution(cutoffScore, scoresLength, scores)
    print(result)


if __name__ == '__main__':
    main()
"""


#print(solution(10, 5, [1, 10, 2, 3, 15]))
print(solution(16, 4, [10,5,2,6]))
#print(solution(0, 3, [1,2,3]))