#functions that just print stuff are not common at all in python. More likely you will have a function that returns something that can be used elswhere. 
#for example say you wanted to go and get a bunch of data from a database or a webserver and then do things with it later, you could have a function that makes the DB call and then stores it to a variable, then have another function that parses the data or whatever. 

def my_function_that_returns_data(number_1,number_2):
    final_data = number_1 + number_2
    #notic we use the 'return' keyword to tell the function to return the data. This will end the function, nothing after reutrn will be processed. 
    return final_data


#we now call the function and stores it's return value into a variable. 
some_data = my_function_that_returns_data(10,5)

print(some_data)