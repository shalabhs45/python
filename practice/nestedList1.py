def calc_marks():
    if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    marks = student_marks[query_name]
    
    #add = reduce (lambda x,y: x + y, marks)
    add = sum(marks)
    result= float(add / len(marks))
    print("{0:.2f}".format(result))