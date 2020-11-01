
def fizzbuzz(num):
    numlist = range(num+1)
    fizzbuzzlist = [fb for fb in numlist if fb % 3 == 0 and fb % 5 == 0]
    fizzlist = [fizz for fizz in numlist if fizz % 3 == 0 and fizz not in fizzbuzzlist]
    buzzlist = [buzz for buzz in numlist if buzz % 5 == 0 and buzz not in fizzbuzzlist]

    for num in numlist:
        if num in  fizzbuzzlist:
            print('FizzBuzz')
        elif num in fizzlist:
            print('Fizz')
        elif num in buzzlist:
            print('Buzz')
        else:
            print(num)



if __name__ == "__main__":
    fizzbuzz(int(input('Please type a number to evaluate. ')))

