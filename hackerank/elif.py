n = int(input().strip())
    if(n%2!=0):
        print('Weird')
    elif(2<=n<=5):
        print('Not Weird')
    elif(6<=n<=20):
        print('weird')
    elif(n%2==0 and n>20):
        print('Not Weird' )
