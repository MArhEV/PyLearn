comms = ['dupa1', 'dupa2', 'dupa3',]
sent_comms = []
def show_comms(comms):
    for comm in comms:
        print(comm)

def send_comms(comms):
    while comms:
        comm = comms.pop()
        print(comm)
        sent_comms.append(comm)


send_comms(comms[:])
print(comms)
print(sent_comms)