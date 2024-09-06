file = open('ayush.txt', 'w')

try:
    file.write("Ayush is Great")
finally:
    file.close()

with open('ayush.txt','w') as file:
    file.write('ayush pal')