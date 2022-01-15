clients_fin = []

def showClients(argument):                                                   ### Function that prints elements of a list
    for i in argument:
        print(i)

seats = int(input("How many seats are available in the restaurant?"))        ### Limit of the input data is introduced

for names in range(seats):
    name = input(("What is your name?"))                                     ### User introduces his/her name
    priority = input("What is your order's level of priority (High/Low) ?")  ### User introduces priority level of his/her order
    if priority == "High":
        clients_fin.insert(0,name)                                           ### High priority level -> name is added to the beginning of the list of clients 
    elif priority == "Low":           
        clients_fin.append(name)                                             ### Low priority level -> name is added to the end of the list of clients
    else:
        print("Incorrect priority level was introduced?")
    
showClients(clients_fin)                                                     ### Call of the function output()
