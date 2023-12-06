# UPPERCASE
kata = 'dicoding'
kata = kata.upper()
print(kata)

# lowercase
kata = 'DICODING'
kata = kata.lower()
print(kata)


# 
# Awalan dan Akhiran
# 

# rstrip()
print("Dicoding          ".rstrip())

# istrip()
print("           Dicoding".lstrip())

# strip()
print("         Dicoding          ".strip())

kata = 'CodeCodeDicodingCodeCode'
print(kata.strip("Code"))

# startswith() Metode ini juga mengembalikan nilai True jika menemukannya kata di awal kalimat, sedangkan jika tidak menemukan kata yang diinginkan, nilai False dikembalikan.
print('Dicoding Indonesia'.startswith('Dicoding'))

# endswith()Metode ini juga mengembalikan nilai True jika menemukannya kata di akhir kalimat, sedangkan jika tidak menemukan kata yang diinginkan, nilai False dikembalikan.
print('Dicoding Indonesia'.endswith('Dicoding'))


# 
# Memisah dan Menggabung String
# 

# join()
print(' '.join(['Dicoding','Indonesia', '!']))
print('123'.join(['Dicoding','Indonesia']))


# split()
print('Dicoding Indonesia !'.split())
print('''Halo,
aku ikan,
aku suka sekali menyelam
aku tinggal di perairan.
Badanku licin dan renangku cepat.
Senang berkenalan denganmu.'''.split('\n'))

# replace()
string = "Ayo belajar Coding di Dicoding"
print(string.replace("Coding", "Pemrograman"))

# 
# Pengecekan String
# 

# isupper()
# isupper() akan mengembalikan nilai True jika semua huruf dalam string adalah huruf kapital (uppercase).
kata = 'DICODING'
print(kata.isupper())

# islower()
# Kebalikannya, islower() akan mengembalikan nilai True jika semua huruf dalam string adalah huruf kecil (lowercase). 
kata = 'dicoding'
print(kata.islower())


# isalpha()
# Metode ini mengembalikan nilai True jika semua karakter dalam string adalah huruf alfabet. Jika ada satu huruf lain yang bukan alfabet, seperti angka, nilai False akan dikembalikan.
kata = 'dicoding'
print(kata.isalpha())

# isalnum()
# Metode isalnum() mengembalikan nilai True jika karakter dalam string adalah alfanumerik, yaitu hanya huruf atau hanya angka atau berisi keduanya. Jika tidak, nilai False akan dikembalikan.
kata = 'dicoding123'
print(kata.isalnum())

# isdecimal()
# Metode isdecimal() akan mengembalikan nilai True jika karakter dalam string berisi hanya angka/numerik. Jika tidak, nilai False akan dikembalikan.
print('123'.isdecimal())

# isspace()
# Metode isspace() akan mengembalikan nilai True jika string hanya berisi whitespace, seperti spasi, tab, newline, atau karakter whitespace lainnya.
print('         '.isspace())

# istitle()
# Metode istitle() mengembalikan nilai True jika string berisi huruf kapital pada setiap kata pertamanya. Jika tidak, nilai False dikembalikan.
print('Dicoding Indonesia'.istitle())

# 
# Formatting pada String
# 

# zfill()
# Metode zfill() bertujuan untuk menambahkan nilai nol (0) di depan sebuah string dengan panjang tertentu. 
teks = 'Code'
tambah_number = teks.zfill(6)
print(tambah_number)

# rjust()
# Metode rjust() berguna untuk merapikan pencetakan teks. Dengan metode rjust() ini, Anda dapat membuat teks menjadi rata kanan sehingga tampilannya lebih rapi.
print('Dicoding'.rjust(20))
print('Dicoding'.rjust(20, '!'))


# ljust()
# Selanjutnya adalah metode ljust(), metode ini adalah kebalikan dari metode rjust() yang bertujuan untuk membuat teks menjadi rata kiri.
print('Dicoding'.ljust(20))

# center()
# Metode center() menjadikan teks rata tengah. Metode ini akan menambahkan whitespace di sebelah kiri dan kanan secara default. Anda juga bisa mengganti whitespace tersebut dengan karakter lain.
print('Dicoding'.center(10, '-'))

# 
# String Literals
# 

# st1 = 'Jum'at'
# diganti menjadi
st1 = "Jum'at" #atau
st1 = 'Jum\'at'

# contoh yang lain
# \' Single quote
# \" Double quote
# \t Tab
# \n Newline (line break)
# \\ Backslash

print("Halo!\nKapan terakhir kali kita bertemu?\nKita bertemu hari Jum\'at yang lalu.")

# 
# Raw String
# 

print(r'Dicoding\tIndonesia')
