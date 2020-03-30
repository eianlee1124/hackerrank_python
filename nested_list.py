if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        students.append([input(), float(input())])
        
    grades = sorted(set(score for _, score in students))
    
    for name, grade in sorted(students):
        if grade == grades[1]:
            print(name)