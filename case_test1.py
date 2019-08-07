w=input()
n=ord(w)
if 65<=n and n<=90:
    print('upper')
elif 48<=n and n<=57 :
    print('number')
elif 97<=n and n<=122:
    print('lower')