#there are 5 datatypes I find myself using very frequently. Here are some examples of each of them. 

#strings
my_string = "This is a string datatype"

#intergers 
my_int = 1
#floating point

my_floting_point = 1.1

#lists 

my_list = ['element_0','element_1','element_2']

print('printing my list')
print(my_list)

print('printing first element in my list')
print(my_list[0])

print('printing third element in my list')
print(my_list[2])

#dictionary 

my_dict = {
    'some_key':'some data',
    'some_list_key':['some','list','data'],
    'some_dict_key': {
        'look':['a','dictionary inside a dictionary']
    }
}

print('printing my dictionary')
print(my_dict)

print('printing my dictionary using a specific key')
print(my_dict['some_list_key'])

print('printing my dictionary using a specific key that references a list and then specifcying the index in the list')
print(my_dict['some_list_key'][0])

print('some additional prints')
print(my_dict['some_dict_key']['look'])
print(my_dict['some_dict_key']['look'][1])