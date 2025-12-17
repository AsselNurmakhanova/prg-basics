import json
filename = 'voting.json'
try:
    with open(filename, 'r') as f:
        votes = json.load(f)
except FileNotFoundError:
    votes = {}  # если файла нет, создаём пустой словарь
person_name = input("Name of the person you are voting for: ").strip()
if person_name in votes:
    votes[person_name] += 1
else:
    votes[person_name] = 1 
# 4. Сохраняем данные обратно в json
with open(filename, 'w') as f:
    json.dump(votes, f, indent=4)
print(f"Thank you! Current votes: {votes}")
