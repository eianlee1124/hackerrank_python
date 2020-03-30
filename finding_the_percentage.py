if __name__ == "__main__":
    n = int(input())
    student_makrs = {}
    
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_makrs[name] = scores
    
    query_name = input()
    scores = student_makrs[query_name]

    answer = 0
    for score in scores:
        answer += score

    print("%.2f" % (answer / len(scores)))