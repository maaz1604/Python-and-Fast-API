marks = int(input('Please enter the student\'s marks: \n'))
if(marks > 100):
    print("Please give marks in between 0-100 \n")
    exit()

if(marks < 60):
    print('F')
    
elif(marks < 70):
    print('D')
    
elif(marks < 80):
    print('c')
    
elif(marks < 90):
    print('B')
    
else:
    print('A')