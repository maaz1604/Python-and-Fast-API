word = str(input('Please enter a string: '))

length = int(len(word))

ans = ""

for i in range(length-1,-1,-1):
    ans = ans + word[i]
    
print(ans)