import os

def remove_lines(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            if not line.startswith(',"",,"",'):
                outfile.write(line)

# Укажите входной и выходной файлы
input_file = 'data.csv'
output_file = 'cleaned_data.csv'

if os.path.exists(output_file):
    os.remove(output_file)

remove_lines(input_file, output_file)