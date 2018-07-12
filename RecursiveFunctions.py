def rsum(alist):
    if(len(alist) == 1):
        result = alist[0]
    else:
        result = alist[0] + rsum(alist[1:])
    return result


def rmax(alist):
    if(len(alist) == 2 and alist[0] >= alist[1]):
        result = alist[0]
    elif(len(alist) == 2 and alist[0] < alist[1]):
        result = alist[1]
    elif(len(alist) == 1):
        result = alist[0]
    else:
        rest = rmax(alist[1:])
        if(alist[0] >= rest):
            result = alist[0]
        else:
            result = rest
    return result


def second_smallest(alist):
    if(len(alist) == 2 and alist[0] >= alist[1]):
        result = alist[0]
    elif(len(alist) == 2 and alist[0] < alist[1]):
        result = alist[1]
    else:
        num = alist[0]
        rest = help1(alist[1:])
        if(num < rest[0]):
            result = rest[0]
        elif(num < rest[1]):
            result = num
        else:
            result = rest[1]
    return result


def help1(alist):
    if(len(alist) == 2 and alist[0] <= alist[1]):
        result = (alist[0], alist[1])
    elif(len(alist) == 2 and alist[0] > alist[1]):
        result = (alist[1], alist[0])
    else:
        cur = alist[0]
        rest = help1(alist[1:])
        if(cur < rest[0]):
            rest = (cur, rest[0])
        elif(cur < rest[1]):
            rest = (rest[0], cur)
        result = rest
    return result


def sum_max_min(alist):
    if(len(alist) == 1):
        result = 2 * alist[0]
    elif(len(alist) == 2):
        result = alist[0] + alist[1]
    else:
        num = alist[0]
        rest = help2(alist[1:])
        if(num < rest[0]):
            result = num + rest[1]
        elif(num > rest[1]):
            result = rest[0] + num
        else:
            result = rest[0] + rest[1]
    return result


def help2(alist):
    if(len(alist) == 2 and alist[0] <= alist[1]):
        result = (alist[0], alist[1])
    elif(len(alist) == 2 and alist[0] > alist[1]):
        result = (alist[1], alist[0])
    else:
        cur = alist[0]
        rest = help2(alist[1:])
        if(cur < rest[0]):
            rest = (cur, rest[1])
        elif(cur > rest[1]):
            rest = (rest[0], cur)
        result = rest
    return result
def edit_distance(s1,s2):
    return edit_distance_helper(s1,s2,0)
def edit_distance_helper(s1,s2,distance):
    if len(s1) == 1:
        if s1[0] == s2[0]:
            result =  distance 
        else:
            result = distance + 1
    else: 
        if s1[0] == s2[0]:
            result = edit_distance_helper(s1[1:],s2[1:],distance)
        else:
            result = edit_distance_helper(s1[1:],s2[1:],distance+1)
    return result
def subsequence(s1,s2):
    
    if len(s1) == 0:
        return True
    if(len(s1) > len(s2)):

        return False
 

    if (s1[0] == s2[0]):

        return subsequence(s1[1:], s2[1:])

    return subsequence(s1, s2[1:])

def permutations(s):
    if len(s) == 0:
        result = {''}
    else:
        result = set()
        for i in range(0,len(s)):
            partStr = s[:i] + s[i+1:]
            perm = permutations(partStr)
            for element in perm:
                result.add(s[i] + element)
    return result