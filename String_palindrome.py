n=input()
s=''
for i in range(len(n)-1,-1,-1):
    s=s+n[i]
if s==n:
    print('palindrome')
else:
    print('Not')