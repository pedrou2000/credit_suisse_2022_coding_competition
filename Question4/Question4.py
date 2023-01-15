def solution(n, employees, shifts):
    # dictionary which will hold the important information for printing result
    output = dict()

    # dictionary which will hold the turns of each employee
    turns = dict()
    for i in range(len(employees)):
        turns[employees[i]] = shifts[i]

    # get the decomposition of the range of working hours and save it
    hours_turns = sorted(list(set([x for t in shifts for x in t])))
    output['n_intervals'] = len(hours_turns)-1

    # for each of the intervals (min, max) we check if the employee has to work in this turn 
    # and add them to a list holding the names of employees working in this turn
    for i in range(output['n_intervals']):
        min = hours_turns[i]
        max = hours_turns[i+1]
        output[(min, max)] = list()
        for worker in turns.keys():
            if min >= turns[worker][0] and max <= turns[worker][1]:
                output[(min, max)].append(worker)
        (output[(min, max)]).sort()
                
    # print all the results
    print(output['n_intervals'])

    for i in range(output['n_intervals']):
        min = hours_turns[i]
        max = hours_turns[i+1]
        length = len(output[(min, max)])
        print(str(min), str(max), str(length), " " . join(output[(min, max)]))


    return output


"""
def main():
    n = int(input())
    employees = input().split(" ")
    shifts = []
    for i in range(n):
        line = input().split(" ")
        shifts.append([int(line[0]), int(line[1])])

    solution(n, employees, shifts)


if __name__ == '__main__':
    main()
"""

print(solution(5, ["Alice", "Bob", "Cacey", "Deepak", "Emma"], [
    [10, 14],
    [11, 12],
    [10, 15],
    [12, 16],
    [14, 16],
]))