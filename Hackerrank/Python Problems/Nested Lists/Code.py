if __name__ == '__main__':
    n = int(input())
    records = []
    
    for _ in range(n):
        name = input()
        score = float(input())
        records.append([name, score])

   
    records.sort(key=lambda x: (x[1], x[0]))

  
    second_lowest_grade = sorted(set(score for name, score in records))[1]

    
    for name, score in records:
        if score == second_lowest_grade:
            print(name)
