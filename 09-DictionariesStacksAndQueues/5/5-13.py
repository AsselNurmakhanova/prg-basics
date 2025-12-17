import queue
def evaluate_rpn():
    stack = queue.LifoQueue()
    print("Enter numbers, operators (+ - * /), or '=' to get the result.")
    print("Enter 'q' to quit.")
    while True:
        token = input("Enter token: ").strip()
        if token.lower() == 'q':
            break
        if token == '=':
            if stack.empty():
                print("Stack is empty. No result.")
            else:
                result = stack.get()
                print("Result:", result)
            # очищаем стек для нового выражения
            while not stack.empty():
                stack.get()
            continue
        # если это оператор
        elif token in '+-*/':
            if stack.qsize() < 2:
                print("Not enough operands in stack.")
                continue
            b = stack.get()
            a = stack.get()
            if token == '+':
                stack.put(a + b)
            elif token == '-':
                stack.put(a - b)
            elif token == '*':
                stack.put(a * b)
            elif token == '/':
                if b == 0:
                    print("Division by zero!")
                    stack.put(a)
                    stack.put(b)
                    continue
                stack.put(a / b)
        # если это число
        else:
            try:
                num = float(token)
                stack.put(num)
            except ValueError:
                print("Invalid input. Enter a number, operator, or '='.")
evaluate_rpn()
