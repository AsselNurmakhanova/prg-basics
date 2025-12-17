import queue
# creates a stack
cards = queue.LifoQueue()
# adds elements to the top of the stack  
cards.put(2)
cards.put(3)
cards.put(7)
cards.put(4)
cards.put(1)
cards.put(9)
cards.put(8)
## prints number of elements of the stack
print('Number of stack elements:', cards.qsize())
last = cards.get()       # 8
second_last = cards.get()  # 9
last_two_sum = last + second_last
print("Sum of the last two numbers:", last_two_sum)
print(cards)
remaining_sum = 0
while not cards.empty():
    remaining_sum += cards.get()
print("Sum of remaining stack elements:", remaining_sum)
# removes and prints elements from the top of the stack
while not cards.empty():
    card = cards.get()
    print(card)