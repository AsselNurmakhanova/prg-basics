import queue
def brackets_ok(expression):
    stack = queue.LifoQueue()
    matching = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    for ch in expression:
        if ch in '([{':
            stack.put(ch)
        elif ch in ')]}':
            if stack.empty():
                return False 
            top = stack.get()
            if top != matching[ch]:
                return False
    return stack.empty()
