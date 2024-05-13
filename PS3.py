import random
eng_mark = {}

students = ['Harsh', 'Aadi', 'Karunesh', 'Sam']
for student in students:
    eng_mark.update({student:random.randint(1, 100)})
print(eng_mark)

names = ["Harsh", "Aadi", "Karunesh", "Sam"]
marks = [58, 99, 76, 85]

lang_mark = dict(zip(names, marks))
print(lang_mark)
