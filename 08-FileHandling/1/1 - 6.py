
def read_from_file(name):
   with open(name, 'r') as file:
      content = file.read()
   return content
file_content = read_from_file('countries.txt')
file_lines = file_content.splitlines()
file_lines_sorted = sorted(file_lines)
for line in file_lines_sorted:
   print(line)
