with open('results.txt', 'r', encoding='UTF-8') as f:
 data = f.readlines()

students = {}
for line in data:
 name, surname, topic, grade = line.strip().split(':')
 fullname = name + ' ' + surname
 students[fullname] = {'topic': topic, 'grade': int(grade)}

sorted_students = dict(sorted(students.items(), key=lambda x: x[1]['grade'], reverse=True))

for student in list(sorted_students)[:3]:
 print('В Топ 3 лучших входит:', student, sorted_students[student])

with open('sorted_results.txt', 'w', encoding='UTF-8') as f:
 for student in sorted_students:
  f.write(student + ':' + sorted_students[student]['topic'] + ':' + str(sorted_students[student]['grade']) + '\n')

with open('sorted_results.txt', 'r', encoding='UTF-8') as f:
 print(f.read())








