import random


def search(data,target,init,fin):
    if init > fin:
        return False

    mid =int( (fin+init)/2)

    if target == data[mid]:
        return True
    elif target < data[mid]:
        return search(data, target,init, mid-1)
    else:
        return search(data, target,mid+1,fin)




if __name__ == "__main__":
    data = [random.randint(0,100) for i in range(100) ]

    data.sort()

    print(data)

    response = ' '
    while response != 'EXIT':
        response=input('What number would you like to Find?')
        if response.isnumeric() :
            target = int(response)
            found = search(data,target,0,len(data) -1)
            print(found)
        else:
            response =response.upper()
            if response != 'EXIT':
                print('This Program only use number if you want to stop please write exit')
