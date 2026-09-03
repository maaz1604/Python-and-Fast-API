user_age = input("Give the user age: \n")
us_age = int(user_age);
if(us_age < 13):
    print("The user is child")

elif(us_age >= 13 | us_age <= 19):
    print('The user is teenager')

elif(20<=us_age<=59):
    print('The user is adult')

else:
    print('The user is senior citizen')