import os

input_file = os.path.join('data', 'txt_input', 'data.txt')
output_file = os.path.join('data', 'txt_output', 'result.txt')

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

good_students = []

for line in lines:
    name, age, score = line.strip().split(";")
    
    if int(score) >= 80:
        good_students.append(name + "\n")

with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(good_students)

print(f"Дані успішно оброблено. Результат збережено у '{output_file}'.")