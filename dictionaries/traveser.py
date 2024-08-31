d = {
"key": "value",
"harry": "code",
"marks": "100",
"list": [1, 2, 9]
}

print(id(d)) #gives the address of the object

for i in d:  ##traverse in dict
    print(i,':',d[i])

