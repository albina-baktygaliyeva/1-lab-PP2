import re

def camel_to_snake(string):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()

print(camel_to_snake("HelloWorldExample"))  
