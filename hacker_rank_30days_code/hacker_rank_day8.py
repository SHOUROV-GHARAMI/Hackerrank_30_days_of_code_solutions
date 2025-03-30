# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input().strip())
phoneBook={}

for i in range(0, n):
    name, number = input().strip().split(' ')
    phoneBook[name] = number
    
while True:
    try:
        entry = input().strip()
        if entry in phoneBook.keys():
            print('{}={}'.format(entry, phoneBook[entry]))
        else:
            print('Not found')
    except EOFError:
        break
            
