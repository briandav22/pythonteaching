#scoping variables is a tougher concept to get your arms around at first. Lets take a look here. 

#this x variable is in 'global scope' which means that it can be accessed globablly with in the code. Generally you want to be very careful with globabl variables, they should not change throughout your application, it will cause problems. 

#this is a global variable 
x = 'something_global'


def my_func():
    
    print('printing the global variable inside the function call')
    print(x)

    print('creating a local variable inside the function with same name as globabl variable')
    x = 'new_global'
    print('notice how we print out the local variable inside the function ')
    print(x)

#
print(x)

my_func()