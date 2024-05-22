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

actual_marks = []
actual_marks.append(eng_mark)
actual_marks.append(lang_mark)
print(actual_marks)

totalMarks = []
for marks in actual_marks:
    total_marks_dict ={}
    for keys in marks:
        total_marks_dict[keys] = eng_mark[keys] + lang_mark[keys]
totalMarks.append(total_marks_dict)
print(totalMarks)

class_marks1 = {}
list_of_names_sub_tot = [("Harsh","Eng", "Lang", "Tot"), ("Aadi", "Eng", "Lang", "Tot"), ("Karunesh", "Eng", "Lang", "Tot"), ("Sam", "Eng", "Lang", "Tot") ]
for i in list_of_names_sub_tot:
    class_marks1.update({i : None})
print(class_marks1)


values = []
values.append(eng_mark)
values.append(lang_mark)
values.append(totalMarks)
    
print(values)

