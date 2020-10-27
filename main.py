import sys

#clients = ['pablo', 'ricardo']

clients = [
        { 
            'name' :'Pablo',
            'company' : 'paythonorg',  
            'email' : 'pablo@google.com',
            'psition' : 'Software engineer'
        },
        {
            'name' :'Ricardo',
            'company' : 'Facebook',  
            'email' : 'Ricardo@facebook.com',
            'psition' : 'Data engineer'
        }
        ]


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

def list_clients():
    global clients
    for idx, client in enumerate(clients):
        print('{}: {}'.format(idx, client['name']))

    print('END Of LIST')
    print('')



def update_client(client_name, updated_client):
    global clients
    for client in clients:
        if client_name in client['name']:
            index = clients.index(client)
            clients[index]= updated_client
    else:
        print('Client is not in clients list')


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
    print('[D]elete client')
    print('[U]pdate client')
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
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'EXIT':
        sys.exit()
    else:
   	if command == 'C':
   	    client = _get_client() 
   	    list_clients()
   	    create_client(client)
   	    list_clients()
   	elif command =='D':
   	    client_name = _get_client_name() 
   	    list_clients()
   	    delete_client(client_name)
   	    list_clients()
   	elif command =='U':
   	    client_name = _get_client_name()
   	    updated_client = _get_client()
   	    update_client(client_name,updated_client)
   	    list_clients()
   	elif command == 'F':
   	    client_name = _get_client_name()
   	    print(find_client(client_name))
#  	     list_clients()
   	else: 
   	    print('invalid command')


