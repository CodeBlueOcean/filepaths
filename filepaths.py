# example relative path 
# with open('app/sad.txt', mode='r') as my_file:
#     print(my_file.read())

# example absolute path
with open('/Users/aneagoie/Desktop/app/sad.txt', mode='r') as my_file:
    print(my_file.read())

# example  ./ from the current folder
with open('./app/sad.txt', mode='r') as my_file:
    print(my_file.read())

# example .. goes to the user account
with open('../app/sad.txt', mode='r') as my_file:
    print(my_file.read())
