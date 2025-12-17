import queue
stack = queue.LifoQueue()
num = int(input("Enter a number: "))
original = num  # сохраняем исходное число для вывода
while num > 0:
    remainder = num % 2
    stack.put(remainder)
    num = num // 2
binary = ""
while not stack.empty():
    binary += str(stack.get())
print(f"Natural number: {original}")
print(f"Binary number: {binary}")
