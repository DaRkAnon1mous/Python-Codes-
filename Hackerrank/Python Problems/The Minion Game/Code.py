def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    
    kscore = 0
    sscore = 0
    
    for i in range(len(string)):
        if string[i] in vowels:
            kscore += len(string)-i
        else:
            sscore += len(string)-i
            
    if kscore>sscore:
        print(f'Kevin {kscore}')
    elif sscore>kscore:
        print(f'Stuart {sscore}')
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
