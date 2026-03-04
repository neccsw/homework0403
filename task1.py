import os

input_file = os.path.join('data', 'txt_input', 'animals.txt')
output_file = os.path.join('data', 'txt_output', 'young_animals.txt')

with open(input_file, 'r', encoding='utf-8') as file_in, \
     open(output_file, 'w', encoding='utf-8') as file_out:
    
    for line in file_in:
        data = line.strip().split()
        
        if len(data) == 3:
            name, age, breed = data

            if int(age) < 5:
                file_out.write(f"{name} {age} {breed}\n")

print(f"Дані успішно відфільтровано та записано у файл '{output_file}'.")