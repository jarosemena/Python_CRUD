import sys
import csv
import os

#clients = ['pablo', 'ricardo']

CLIENT_TABLE = './.data/clients.csv'
CLIENT_SCHEMA = ['name','company', 'email','position']
clients = []


def _initialize_clientes_csv():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)

def _save_clientes_csv():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
        os.rename(tmp_table_name, CLIENT_TABLE)

def create_client(client):
    global clients
    if client not in clients:
       clients.append(client)
    else:
        print('Client already is in the client\'s list')


def find_client(client_name):
    global clients
    result =  'the cliente {} is not in the list'.format(client_name)
    for client in clients:
        if client['name'] == client_name:
            result = 'the client is in the list of clients'

    return result

def find_client_id(client_name):
    global clients
    result =  -1
    for client in clients:
        if client['name'] == client_name:
            return clients.index(client)

    return result

def list_clients():
    global clients
    for idx, client in enumerate(clients):
        print('{}: {} | {} | {} | {} '.format(idx, client['name'],client['company'],client['email'],client['position']))

    print('END Of LIST')
    print('')



def update_client(clientid, updated_client):
    global clients
    clients[clientid]= updated_client


def delete_client(client_name):
    global clients
    for client in clients:
        if client_name in client['name']:
            clients.remove(client)
    else:
        print('Client is not in clients list')


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[R]ead client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[F]ind client')


def _get_client_name():
    client_name= None

    while not client_name:
        client_name = input('what is the client name? ')

        if client_name == 'exit':
            client_name= None
            break

    if not client_name:
        sys.exit()

    return client_name


def _get_client():
    client_name= None
    company = None
    email = None
    position = None
    client = {}

    while not client_name:
        client_name = input('what is the client name? ')

        if client_name == 'exit':
            client_name= None
            break

    if not client_name:
        sys.exit()


    while not company:
        company = input('what is the client\'s company name? ')

        if company == 'exit':
            company= None
            break

    if not company:
        sys.exit()

    while not email:
        email = input('what is the client\'s Email? ')

        if email == 'exit':
            email = None
            break

    if not email:
        sys.exit()


    while not position:
        position = input('what is the client\'s position? ')

        if position == 'exit':
            position = None
            break

    if not position:
        sys.exit()

    client = {
        'name' : client_name,
        'company' : company,
        'email' : email,
        'position' : position
           }

    return client


if  __name__ == '__main__':
    _initialize_clientes_csv()
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'EXIT':
        sys.exit()
    else:
        if command == 'C':
            client = _get_client()
            create_client(client)
        elif command =='R':
            list_clients()
        elif command =='D':
            client_name = _get_client_name(i)
            delete_client(client_name)
        elif command =='U':
            client_name = _get_client_name()
            clientid= find_client_id(client_name)
            if clientid >= 0:
                print('Ingrese los datos actualizados del cliente')
                updated_client = _get_client()
                update_client(clientid,updated_client)
            else:
                print('this client not exist')
        elif command == 'F':
            client_name = _get_client_name()
            print(find_client(client_name))
        else:
            print('invalid command')

    _save_clientes_csv()

