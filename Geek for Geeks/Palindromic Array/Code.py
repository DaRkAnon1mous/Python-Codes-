# Your task is to complete this function
# Function should return true/false

def reverse(arrn):
    rev =0
    
    while arrn > 0:
        d = arrn % 10
        rev = rev *10 + d
        arrn = arrn // 10
    return rev

def PalinArray(arr):
    for num in arr:
        if num != reverse(num):
            return False
    return True
           


#{ 
 # Driver Code Starts
# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr):
            print("true")
        else:
            print("false")
# Contributed By: Harshit Sidhwa

# } Driver Code Ends
