

clients = 'pablo, ricardo,'


def create_client(client_name):
    global clients
    if client_name not in clients:
       clients += " " + client_name + ","
    else:
        print('Client already is in the client\'s list')

def list_clients():
    global clients
    print(clients)


def update_client(client_name, updated_client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name, updated_client_name)
    else:
        print('Client is not in clients list')


def delete_client(client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
    else:
        print('Client is not in clients list')


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[D]elete client')
    print('[U]pdate client')
    

def _get_client_name():
    return input('what is the client name? ')

if  __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name() 
        list_clients()
        create_client(client_name)
        list_clients()
    elif command =='D':
        client_name = _get_client_name() 
        list_clients()
        delete_client(client_name)
        list_clients()
    elif command =='U':
        client_name = _get_client_name()
        updated_client_name = input('what is the new client name')
        update_client(client_name,updated_client_name)
        list_clients()
    else: 
        print('invalid command')


