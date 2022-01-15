clients             = ["John","Mary","Kate"]
clientsHighPriority = ["Tob","Pete"]
clientsLowPriority  = ["Vicky","Lessly"]

clientsHighPriority.reverse()

def output(argument):                          ### function that prints elements of a list
    for i in argument:
        print(i)

for name in clients + clientsHighPriority + clientsLowPriority:
    if name in clientsHighPriority:            ### High Priority Clients are added to the beginning of the list clients
        clients.insert(0,name)
    elif name in clientsLowPriority:           ### Low Priority Clients are added tot the end of the list clients
        clients.append(name)
    
output(clients)                                ### Call of the function output()