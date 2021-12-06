#functions are also capable of taking in arugments to them. For example our basic function from before could be modified to accept arugments. 

#this is how we define a function.
def my_function(some_argument):
    # notice the 'string interpolation' we are using here. This is a very common was to pass a variable inside of a string. We will use this often as we learn python.
    print(f'this is a smarter function built for {some_argument}')

#this is how we call a function. 
my_function('Jose')


#there is no limit to number of args you can pass into a function. For example. 


def multiple_args_function(arg1,arg2,arg3):
   
   print(f'this is arg1: {arg1}, this is arg2: {arg2},this is arg3: {arg3}')


multiple_args_function('1','2', '3')