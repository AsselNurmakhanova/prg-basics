import queue
customers = queue.Queue()
ticket_number = 1 
while True:
    print("1 - New customer")
    print("2 - Serve next customer")
    print("3 - Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        customers.put(ticket_number)
        print(f"Customer added. Ticket number: {ticket_number}")
        ticket_number += 1
    elif choice == '2':
        if customers.empty():
            print("No customers in the queue.")
        else:
            next_customer = customers.get()
            print(f"Serving customer with ticket number: {next_customer}")
    elif choice == '3':
        print("Exiting the system.")
        break
