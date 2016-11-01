# statement = input()
#
# if (len(statement) > 10 ):
#     print(statement[:10] + '...')
# else:
#     print(statement)

# statement = input()
# delimiter = input()
#
# index = statement.rfind(delimiter) + len(delimiter)
#
# if (statement.rfind(delimiter) != -1):
#     print(statement[index:])
# else:
#     print(statement)

name = input("Please enter name: ")
initials = ""

for i in name:
   if i.isupper():
       initials = initials + i + '.'
print(initials)