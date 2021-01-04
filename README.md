# Task 04 - Talent Factory Batch 1

## Intro

### Vigenère Cipher

Vigenere Cipher adalah metode kriptografi klasik untuk menyandikan suatu plaintext dengan menggunakan sistem substitusi, yaitu metode teknik enkripsi teks menggunakan substitusi alphabet

#### Rumus Enkripsi

`Ei = (Pi + Ki) mod 26`\
\
dimana:\
P = Plain text
K = Key

#### Rumus Dekripsi

`Di = (Ei - Ki + 26) mod 26`

#### Cara Kerja

![Case](doc/Screen%20Shot%202021-01-04%20at%2018.31.36.png)

Berikut gambaran enkripsi berdasarkan tabula recta:
![Tabula Recta](doc/tabula%20recta.png)

P1 = I\
K1 = D\
titik potong pada tabel kolom dan baris tersebut di gunakan sebagai hasil enkripsinya

### Studi Kasus

Terinspirasi dari enkripsi end-to-end pada instant messaging

Membuat aplikasi Chat Room sederhana

#### Demo

1. Menjalankan server
![Run](doc/run%20tthe%20server.png)

2. User yang memiliki `key`
![Case](doc/user%20with%20key.png)

3. User yang tidak memiliki `key`
![Case](doc/user%20without%20key.png)