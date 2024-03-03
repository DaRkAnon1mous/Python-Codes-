if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    scores = list(set(arr))

   
    scores.sort(reverse=True)


    print(scores[1])
