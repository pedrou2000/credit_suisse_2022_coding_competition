from collections import Counter
import math 

def solution_2(files):
    counts=Counter(files)

    n = 0
    for letter in counts.keys():
        if counts[letter] % 2 == 0:
            n += counts[letter]
        else: 
            n += 2*math.floor(counts[letter]/2)

    return n+1
    
def solution(files):
    counts=Counter(files)

    n = 0
    for letter in counts.keys():
        if counts[letter] % 2 == 0:
            n += counts[letter]
        else: 
            n += 2*math.floor(counts[letter]/2)

    return n+1

"""

def main():
    str = input()
    answer = solution(str)
    print(answer)


if __name__ == '__main__':
    main()
"""
    
print(solution('abccccdd'))
print(solution('a'))
print(solution('abBccccdd'))
print(solution('aaAbbB'))
print(solution('aaabbb'))
