with open('results.txt', 'r') as f:
    data = f.readlines()

students = {}
for line in data:
    name, surname, topic, grade = line.strip().split(':')
    fullname = name + ' ' + surname
    students[fullname] = {'topic': topic, 'grade': int(grade)}

sorted_students = dict(sorted(students.items(), key=lambda x: x[1]['grade'], reverse=True))

for student in list(sorted_students)[:3]:
    print(student, sorted_students[student])

with open('sorted_results.txt', 'w') as f:
    for student in sorted_students:
        f.write(student + ':' + sorted_students[student]['topic'] + ':' + str(sorted_students[student]['grade']) + '\n')

with open('sorted_results.txt', 'r') as f:
    print(f.read())
