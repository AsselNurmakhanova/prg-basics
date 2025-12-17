import queue
def reverse_string(s):
    stack = queue.LifoQueue()
    for ch in s:
        stack.put(ch)
    reversed_s = ""
    while not stack.empty():
        reversed_s += stack.get()
    return reversed_s
text = input("Enter text to reverse: ")
reversed_text = reverse_string(text)
print("Reversed text:", reversed_text)
