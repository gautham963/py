if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        continue
    query_name = input()
    if query_name in student_marks:
        student_scores = student_marks[query_name]
        total_marks = sum(student_scores)
        print(total_marks)
        avg_marks = (total_marks/(len(scores)))
        print(avg_marks)
    else:
        print(f"{query_name}not found in records.")
    
