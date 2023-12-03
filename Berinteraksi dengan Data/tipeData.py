# Tipe Data Primitif

x = 6
print(type(x))

x = 6.0
print(type(x))

x = 1+2j
print(type(x))

# tipe data number bersifat immutable, artinya tidak dapat diubah
var = 10
print(var)
print(id(var))
var = 11
print(var)
print(id(var))

# Boolean
x = True
print(type(x))

x = False
print(type(x))

# String
a = "ini adalah string"
print(type(a))
print(a[0])
print(a[4:])

multi_line = """Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu."""

print(multi_line)

# Formated String
name = "Perseus Evans"
print(f"Hello, nama saya {name}")
# %-formatting
name = "Perseus Evans"
print("Nama saya %s" % (name))
# str.format()
print("Nama saya {}".format(name))

# 
# Tipe Data Collection
# 

# List
x = [1, 'Dicoding', True, 1.0]
print(type(x))
print(x[2])
x[0] = 'Indonesia'
print(x)

# List indexing
x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0])
print(x[2])
print(x[-1])
print(x[-3])

x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0:5:2])
print(x[1:])
print(x[:3])

# Tuple
x = (1, "Dicoding", 1+3j)
print(type(x))
print(x[1])
print(x[0:3])

# Set
x = {1,2,7,2,3,13,3}
# print(x[0]) bakal error karena set tidak support indexing
print(x)
print(type(x))

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1.union(set2)
print("Union:", union)

intersection = set1.intersection(set2)
print("Intersection:", intersection)

# DIxctionary
x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
print(type(x))
print(x ['name'])

# Menambahkan data pada dictionary
x ['Job'] = "Web Developer"
print(x)
# Menghapus data pada dictionary
del x["isMarried"]
print(x)
# Mengubah data pada dictionary
x["age"] = 31
print(x)

# 
# KOnversi Tipe Data
# 

# konversi dari integer ke float
print(float(5))
# konversi dari float ke integer
print(int(10.6))
# konversi dari dan ke string
print(int("25"))
print(str(25))
print(float("25"))
print(str(25.6))
# konversi kumpulan data
print(set([1,2,3]))
print(tuple({5,6,7}))
print(list("hello"))
# konversi ke dictionary
print(dict([[1,2],[3,4]]))
print(dict([(3,26),(4,44)]))