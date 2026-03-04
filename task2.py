import os
import string

input_file = os.path.join('data', 'txt_input', 'text.txt')
output_file = os.path.join('data', 'txt_output', 'analysis.txt')

with open(input_file, 'r', encoding='utf-8') as f:
    text = f.read()

sentences_count = text.count('.') + text.count('!') + text.count('?')

translator = str.maketrans('', '', string.punctuation)
clean_text = text.translate(translator)

words = clean_text.split()
words_count = len(words)

if words:
    longest_word = max(words, key=len)
else:
    longest_word = "Текст порожній"

result_text = (
    f"--- Аналіз тексту ---\n"
    f"Кількість слів: {words_count}\n"
    f"Кількість речень: {sentences_count}\n"
    f"Найдовше слово: {longest_word}\n"
)

print(result_text)

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(result_text)
    
print(f"Аналіз збережено у файл '{output_file}'.")