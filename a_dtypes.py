a = [1,2,"Three", 4,17 ]
b = {
    "id" : 1234
}

print(a, type(a))
print(b, type(b))

a = [1,2,"Three", 4,17 ]

print("Element 1:" , a[0])
print("Element Last:" , a[-1])

print("Slice a list:" , a[1:3], type(a[1:3]))

for e1 in a:
    print(e1)