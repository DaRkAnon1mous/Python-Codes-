n = int(input().strip())

ar = list(map(int, input().split()[:n]))
var = 0
for num in ar:
    var = num+var
    
print(var)
    
