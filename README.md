# Topological Sort

## Deskripsi Singkat
Program Topological Sort mencari solusi dari pernyusunan rencana kuliah dengan menerapkan *Divide and Conquer*. *Topological Sort* adalah suatu metode *sorting* pada *Directed Acylic Graph* untuk menentukan keterurutan setiap simpul dari simpul yang paling diutamakan sampai yang paling tidak diutamakan.

Implementasi *decrease and conquer* dalam program ini adalah:
1. Decrease <br>
Dari sebuah *list* berisi mata kuliah, yang memiliki banyak simpul sebagai di dalamnya, program akan memproses setiap simpul berdasarkan derajat-masuknya dan akan melakukan pengecekan terhadap derajat-masuk dari setiap simpul
2. Conquer <br>
Untuk tahapan ini, program akan mencari simpul-simpul yang memiliki derajat-masuk 0 dari list kuliah secara rekursif. Cara bekerja rekursifnya adalah dengan mengecek apakah semua simpul sudah diproses (pengecekan apakah simpulnya memiliki derajat-masuk 0 atau tidak) atau belum, sampai tidak ada simpul yang dapat diproses kembali

## Requirement Program
PC sudah ter-*install* python3. Jika belum, silakan mengunjungi [laman ini](https://www.python.org/downloads/) untuk panduan instalasinya.

## Cara Menggunakan Program
1. *Clone repository* ini
```sh
git clone https://github.com/cyn-rus/topological-sort
```
2. Masuk ke dalam *directory* di mana program utama berada di dalam terminal
```sh
cd ../topological-sort/src
```
3. Ketik python main.py atau python3 main.py
```sh
python main.py
```
atau
```sh
python3 main.py
```
4. Masukkan nama file yang sudah terisi dengan persoalan *topological sort* dan pastikan file tersebut berada di dalam ./topological-sort/test, atau dengan file-file yang sudah tersedia. Format *file* teks untuk masukan adalah:
```sh
<kode kuliah 1>,<kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>, <kode kuliah prasyarat - 3>.
<kode kuliah 2>,<kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>.
<kode kuliah 3>,<kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>, <kode kuliah prasyarat - 3>, <kode kuliah prasyarat - 4>.
<kode kuliah 4>.
.
.
.
```

## Identitas Pembuat
Program ini dibuat oleh [@cyn-rus](https://github.com/cyn-rus) untuk menuntaskan tugas kecil 2 dari mata kuliah IF2211 Strategi Algoritma
