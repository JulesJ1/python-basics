from pathlib import Path

cwd = Path.cwd()


TEXT_FILE_NAME = [
    'data.txt',
    'output.txt',
    'protected.txt',
    'data.csv',
    'log.txt'
]

# Exercise 1
file_path = cwd / 'demo_files' / TEXT_FILE_NAME[0]
try:
    with open(file_path) as f:
        content = f.read()
        print(content)
except FileNotFoundError as fnf:
    print(f'FileNotFoundError: {fnf}')

# Exercise 2
lines = [
    "Line 1: Hello, world!",
    "Line 2: Python file handling.",
    "Line 3: Goodbye!"]

output_file_path = cwd / 'demo_files' / TEXT_FILE_NAME[1]

with open(output_file_path, mode='w') as output_file:
    for line in lines:
        output_file.write(line + '\n')

with open(output_file_path) as output_file:
    content = output_file.read()
    print(content)

# Exercise 3
try:
    protected_file_path = cwd / 'demo_files' / TEXT_FILE_NAME[2]
    with open(protected_file_path, mode='w') as protected_file:
        protected_file.write('test')
except PermissionError as pe:
    print(f'PermissionError: {pe}')

# Exercise 4
try:
    data_csv_path = cwd / 'demo_files' / TEXT_FILE_NAME[3]
    with open(data_csv_path) as read_file:
        contents = read_file.read()
        print(contents)
except FileNotFoundError as fnf:
    print(f'FileNotFoundError: {fnf}')
except ValueError as ve:
    print(f'ValueError: {ve}')

# Exercise 5

try:
    data_txt_path = cwd / 'demo_files' / TEXT_FILE_NAME[0]
    read_file = open(data_txt_path)
    contents = read_file.read()
    print(contents)
except FileNotFoundError as fnf:
    print(f'FileNotFoundError: {fnf}')
finally:
    if read_file:
        read_file.close()

# read_file.read()

# Exercise 6
log_file_path = cwd / 'demo_files' / TEXT_FILE_NAME[4]
with open(log_file_path, mode='a') as log_file:
    log_file.write('New Entry')

# Exercise 7

try:
    data_txt_path = cwd / 'demo_files' / TEXT_FILE_NAME[0]
    with open(data_txt_path) as read_data:
        contents = read_data.read()
        print(contents)
except FileNotFoundError as fnf:
    print(f'FileNotFoundError: {fnf}')
except PermissionError as pe:
    print(f'PermissionError: {pe}')
