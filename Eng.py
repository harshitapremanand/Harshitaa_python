import random
eng_mark = {}

students = ['Harsh', 'Aadi', 'Karunesh', 'Sam']
for student in students:
    eng_mark.update({student:round(random.uniform(0, 100), 2)})
print(eng_mark)