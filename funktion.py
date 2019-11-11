def sum2(a, b):
    return a + b

print (sum2(2, 4))

def create_greeting(name):
    return "hejsan " + name + " hur står det till?"

print (create_greeting("stefan"))

def mean2(x, y):
    return (x + y) / 2

print (mean2(8, 10))

def sum_my_list(my_list):
    result = 0
    for x in my_list:
        result = result + x
    return result

a_list = [10, 40, 2, 5] 
print(sum_my_list(a_list))

