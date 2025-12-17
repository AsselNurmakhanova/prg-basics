original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt'

with open(original_file, 'r') as file:
   content = file.read()
# (copy)
with open(target_file, 'w') as file:
   contentt = file.write(content)