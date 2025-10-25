cm = 170
total_inches = cm / 2.54
feet = int(total_inches // 12)
inches = int(total_inches % 12)
print(f'I am {cm} cm tall, i.e. {feet} feet and {inches} inches.')
