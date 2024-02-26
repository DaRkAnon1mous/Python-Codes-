def remdup(l):

    result = []
    seen = set()
    for num in l:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result

print(remdup([3,1,3,5]))
print(remdup([7,3,-1,-5]))
print(remdup([3,5,7,5,3,7,10]))
