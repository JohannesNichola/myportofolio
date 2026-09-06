Nama : Johannes Nichola Simatupang

NPM : 2406495930

Kelas : PBP C

# My Portfolio

## Deskripsi Proyek
Website portofolio pribadi yang dikembangkan sebagai proyek individu mata kuliah Pemrograman Berbasis Platform (PBP).

## Cara Menjalankan Proyek
1. Clone repository.
2. Masuk ke folder proyek.
3. Aktifkan virtual environment.
4. Jalankan: python manage.py runserver

## Progres Mingguan

### Tutorial 1
- Membuat struktur awal proyek Django.
- Membuat halaman About Me.

### Tugas 1
- Menambahkan section Portfolio.
- Menambahkan Experience pada section Portfolio.
- Menambahkan Education pada section Portfolio.
- Menambahkan Skills pada section Portfolio.
- Menambahkan Projects pada section Portfolio.
- Membuat responsive layout menggunakan CSS Grid dan media query.

## Pertanyaan Reflektif

### Tugas 1

1. Pada pembuatan website portofolio ini, saya menggunakan elemen semantik HTML5, terutama `<section>`. Saya menggunakan `<section>` untuk membagi halaman berdasarkan bagian kontennya, seperti bagian profile dan portfolio. Menurut saya, penggunaan `<section>` membuat struktur HTML menjadi lebih rapi dan lebih mudah dipahami karena setiap bagian memiliki kelompok konten masing-masing. Selain itu, penggunaan `<section>` juga memudahkan saya saat mengatur tampilan menggunakan CSS karena setiap bagian dapat diberikan styling sesuai dengan kebutuhannya. Walaupun website yang dibuat masih berupa static web, struktur seperti ini menurut saya akan memudahkan jika nantinya ingin menambahkan atau mengembangkan konten. Selain `<section>`, penggunaan elemen seperti `<header>`, `<main>`, `<nav>`, dan `<footer>` membantu saya dalam membagi halaman berdasarkan fungsinya.

2. Tantangan yang saya temukan dalam membuat website responsive ada pada bagian Projects. Pada tampilan desktop, bagian ini menggunakan CSS Grid dengan dua kolom, yaitu informasi proyek di sebelah kiri dan gambar di sebelah kanan. Namun, jika ukuran layar lebih kecil, tampilan dua kolom tersebut menjadi terlalu sempit. Karena itu, saya menggunakan `@media` untuk mengubah layout menjadi satu kolom pada layar yang lebih kecil. Dengan begitu, informasi proyek dan gambar akan ditampilkan secara vertikal agar lebih nyaman dilihat, terutama pada perangkat mobile.

3. Salah satu batasan yang saya rasakan dari static web adalah keterbatasan dalam membuat interaksi yang lebih dinamis. Pada bagian Experience, Education, Skills, dan Projects, saya menggunakan `<details>` dan `<summary>` untuk membuat dropdown, tetapi animasinya masih cukup terbatas ketika bagian tersebut dibuka dan ditutup berulang kali. Selain itu, slider gambar pada bagian Projects masih menggunakan radio button, sehingga pengguna hanya bisa berpindah gambar dengan menekan titik navigasi. Pada iterasi selanjutnya, saya ingin menambahkan JavaScript agar slider dapat digeser menggunakan click and drag pada desktop serta swipe pada perangkat mobile. Menurut saya, fitur tersebut dapat membuat interaksi website terasa lebih natural dan nyaman digunakan.


## AI Disclosure

### Tugas 1

Dalam pengerjaan tugas ini, saya menggunakan GenAI ChatGPT sebagai alat bantu untuk memahami konsep dan mendapatkan referensi, terutama pada bagian yang paling sulit seperti pembuatan layout dan slider gambar pada bagian **Projects**, serta penggunaan pseudo-class dan pseudo-element seperti `:hover`, `:checked`, `::before`, dan `::marker`. Namun, hasil dari AI tidak langsung saya gunakan sepenuhnya karena solusi yang diberikan terkadang masih terlalu umum dan belum tentu sesuai dengan struktur HTML, desain, dan kebutuhan website saya. Oleh karena itu, saya tetap melakukan penyesuaian dan perbaikan secara manual, seperti mengatur layout Projects agar responsif, menyesuaikan posisi dan ukuran elemen, serta menerapkan pseudo-class dan pseudo-element sesuai dengan fungsinya. Secara keseluruhan, AI membantu saya dalam memahami konsep dan memberikan referensi, tetapi proses implementasi, pengujian, pencarian kesalahan, dan penyesuaian akhir tetap saya lakukan secara manual agar hasilnya sesuai dengan kebutuhan website. Selain itu, saya meminta bantuan ChatGPT untuk memberikan contoh commit yang baik.
