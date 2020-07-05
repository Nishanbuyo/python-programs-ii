def validity(string1):
    brackets = ['()', '[]', '{}']
    while any(x in string1 for x in brackets):
        for br in brackets:
            string1 = string1.replace(br, '')
    return not string1.strip()

print(validity("()"))

str1 = ["()", "()[]{}", "[)", "({[)]", "{{{"]
for strr in str1:
    print(strr, ':', 'Balanced' if validity(strr) else 'Unbalanced')

