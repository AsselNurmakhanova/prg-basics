import queue
def brackets_ok(expression):
    stack = queue.LifoQueue()
    # mapping of closing to opening brackets
    matching = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    for ch in expression:
        # opening brackets → push to stack
        if ch in '([{':
            stack.put(ch)
        # closing brackets → pop and compare
        elif ch in ')]}':
            if stack.empty():
                return False  # no opening bracket to match
            top = stack.get()
            if top != matching[ch]:
                return False  # mismatched brackets
    # after processing all characters,
    # stack must be empty for brackets to be correct
    return stack.empty()
