def camel_to_snake(str1, choose):
    snake= str1[0].lower()
    for c in str1[1:]:
        if ord(c) >= ord('A') and ord(c) <= ord('Z'):
            if choose == "snake":
                snake= snake + '_'
            if choose == "kebab":
                snake = snake + '-'
            snake = snake + c.lower()
        else:
            snake = snake + c.lower()
    return snake


print(camel_to_snake("ThisIsCamelCased", 'snake'))
print(camel_to_snake("ThisIsKebabCased", 'kebab'))