"""ASSIGNMENT 2 QUESTION 4"""

#for each line in file, sort them using shell sort
#after sorting, print it out

import sys

def shell_sort(a_list):
    gap = len(a_list) // 2
    while gap > 0:
        for i in range(len(a_list) - gap):
            j = i + gap
            tmp = a_list[j]
            while j >= gap and tmp > a_list[j - gap]:
                a_list[j] = a_list[j - gap]
                j = j - gap
            a_list[j] = tmp

        if gap == 2:
            gap = 1
        else:
            gap = gap // 2
    return a_list

for line in sys.stdin:
    s = line.split() #s is a list which the input is split into
    c = s[0][0] #used for checking alpha or digit

    #TESTING FOR DIGIT OR STRING
    if c.isalpha():
        s = [str(x) for x in s] #turn list into strings
    else:
        s = [int(x) for x in s] #turn list into integers
    shell_sort(s)
    print(*s)

