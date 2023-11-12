#This is a HackerRank problem to find the second lowest marks.
student_dict = {} #initialize dictionary
for _ in range(int(input('Enter the number of students: '))):#for loop takes the number of students
    name = input('Enter the name: ')
    score = float(input('Enter the score: '))

    student_dict[name] = score #name and score will be appended

Scores = sorted(student_dict.values()) #sorted will sort the list in ascending order

Scores = list(set(Scores))#set will remove repeating values

second_lowest_score = Scores[1]#this will get the second lowest value

students_with_second_lowest_score = [name for name,score in student_dict.items() if score == second_lowest_score]#this will get the names with second lowest marks

student_list = []
for i in sorted(students_with_second_lowest_score):
    student_list.append(i)

for student in sorted(student_list):
    print(student)
                                         
    
