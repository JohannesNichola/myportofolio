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

### Tutorial 2
- Membuat Django apps main
- Membuat model Experience untuk menyimpan data pengalaman.
- Membuat halaman Experience yang menampilkan data dari database (bukan hard code), menerapkan konsep MVT (Model-View-Template) pada Django.
- Melakukan testing pada fungsi views untuk Experience.

### Tugas 2
- Membuat halaman Education menggunakan konsep MVT, dengan data diambil dari database.
- Membuat halaman Project menggunakan konsep MVT, dengan data diambil dari database.
- Mengubah section Skills pada halaman utama agar tidak lagi hard code, melainkan mengambil data dari database.
- Menghapus section Experience, Education, dan Project dari halaman utama karena sudah dipindahkan ke halaman masing-masing.
- Melakukan testing pada fungsi views untuk Education, Project, Skill.

## Pertanyaan Reflektif

### Tugas 1

1. Pada pembuatan website portofolio ini, saya menggunakan elemen semantik HTML5, terutama `<section>`. Saya menggunakan `<section>` untuk membagi halaman berdasarkan bagian kontennya, seperti bagian profile dan portfolio. Menurut saya, penggunaan `<section>` membuat struktur HTML menjadi lebih rapi dan lebih mudah dipahami karena setiap bagian memiliki kelompok konten masing-masing. Selain itu, penggunaan `<section>` juga memudahkan saya saat mengatur tampilan menggunakan CSS karena setiap bagian dapat diberikan styling sesuai dengan kebutuhannya. Walaupun website yang dibuat masih berupa static web, struktur seperti ini menurut saya akan memudahkan jika nantinya ingin menambahkan atau mengembangkan konten. Selain `<section>`, penggunaan elemen seperti `<header>`, `<main>`, `<nav>`, dan `<footer>` membantu saya dalam membagi halaman berdasarkan fungsinya.

2. Tantangan yang saya temukan dalam membuat website responsive ada pada bagian Projects. Pada tampilan desktop, bagian ini menggunakan CSS Grid dengan dua kolom, yaitu informasi proyek di sebelah kiri dan gambar di sebelah kanan. Namun, jika ukuran layar lebih kecil, tampilan dua kolom tersebut menjadi terlalu sempit. Karena itu, saya menggunakan `@media` untuk mengubah layout menjadi satu kolom pada layar yang lebih kecil. Dengan begitu, informasi proyek dan gambar akan ditampilkan secara vertikal agar lebih nyaman dilihat, terutama pada perangkat mobile.

3. Salah satu batasan yang saya rasakan dari static web adalah keterbatasan dalam membuat interaksi yang lebih dinamis. Pada bagian Experience, Education, Skills, dan Projects, saya menggunakan `<details>` dan `<summary>` untuk membuat dropdown, tetapi animasinya masih cukup terbatas ketika bagian tersebut dibuka dan ditutup berulang kali. Selain itu, slider gambar pada bagian Projects masih menggunakan radio button, sehingga pengguna hanya bisa berpindah gambar dengan menekan titik navigasi. Pada iterasi selanjutnya, saya ingin menambahkan JavaScript agar slider dapat digeser menggunakan click and drag pada desktop serta swipe pada perangkat mobile. Menurut saya, fitur tersebut dapat membuat interaksi website terasa lebih natural dan nyaman digunakan.

### Tugas 2

1. Alur dimulai ketika pengguna membuka URL halaman portofolio baru di browser, misalnya `/experience/`. Permintaan (request) tersebut pertama kali diterima oleh `urls.py` milik proyek, yang menjadi pintu masuk utama untuk menentukan aplikasi mana yang bertanggung jawab menangani URL tersebut. Karena path-nya cocok dengan salah satu pola yang di-include dari aplikasi `main`, request kemudian diteruskan ke `urls.py` milik aplikasi, yang memetakan path spesifik tersebut ke sebuah fungsi view tertentu, dalam hal ini `show_experience`. Di dalam view, Django akan mengambil data yang dibutuhkan dengan memanggil model `Experience` melalui Django ORM, misalnya menggunakan `Experience.objects.all()`, sehingga model berperan sebagai perantara antara aplikasi dan database untuk mengambil, menyimpan, atau memanipulasi data. Data yang berhasil diambil kemudian dimasukkan ke dalam sebuah context (berupa dictionary) dan dikirim ke template melalui fungsi `render()`. Template, yang berisi berkas HTML dengan sintaks Django Template Language, kemudian menerima context tersebut dan menampilkan data secara dinamis menggunakan tag seperti `{% for %}` dan `{{ }}`. Hasil akhir dari proses render ini berupa HTML murni yang dikirim kembali oleh Django sebagai response, sehingga browser dapat menampilkannya kepada pengguna sebagai halaman portofolio yang utuh.

2. Menyimpan data pada model jauh lebih baik dibandingkan menuliskannya langsung di dalam template karena template seharusnya hanya berfokus pada bagaimana data ditampilkan, bukan menyimpan data itu sendiri. Jika data ditulis langsung di template (hard code), setiap kali ada perubahan data, seperti menambah pengalaman baru atau mengubah deskripsi skill, saya harus mengedit langsung berkas HTML, yang berisiko membuat struktur template menjadi berantakan dan sulit dibaca seiring bertambahnya data. Dengan menyimpan data pada model, saya cukup menambahkan, mengubah, atau menghapus data melalui Django admin atau Python shell tanpa perlu menyentuh kode template maupun view sama sekali. Hal ini juga membuat aplikasi lebih mudah dikembangkan, karena data yang tersimpan di database dapat digunakan kembali di berbagai halaman atau fitur lain tanpa perlu duplikasi, serta pemeliharaan aplikasi menjadi lebih rapi karena adanya pemisahan yang jelas antara logika data (model), logika tampilan (template), dan logika proses (view).

3. `makemigrations` berfungsi untuk membuat berkas migrasi berdasarkan perubahan yang saya lakukan pada model, seperti menambah field baru, mengubah tipe data, atau menghapus field, di mana berkas ini berisi instruksi perubahan struktur database dalam bentuk kode python, namun perubahaan tersebutt belum benar-benar diterapkan ke database. Sementara itu, `migrate` berfungsi untuk mengeksekusi berkas migrasi tersebut sehingga perubahan strukturnya benar-benar diterapkan ke database yang sebenarnya. Sebagai contoh, ketika saya mengubah model `Skill` dengan menghapus field `tags` dan `started_at` karena diputuskan untuk tidak digunakan, saya perlu menjalankan `makemigrations` terlebih dahulu agar Django membuatkan berkas migrasi yang mencatat perubahan penghapusan kolom tersebut, kemudian menjalankan `migrate` agar kolom `tags` dan `started_at` benar-benar dihapus dari tabel `Skill` di database. Jika saya hanya menjalankan `makemigrations` tanpa `migrate`, perubahan tersebut hanya akan tercatat sebagai rencana migrasi, tetapi struktur tabel di database belum benar-benar berubah.

## AI Disclosure

### Tugas 1

Dalam pengerjaan tugas ini, saya menggunakan GenAI ChatGPT sebagai alat bantu untuk memahami konsep dan mendapatkan referensi, terutama pada bagian yang paling sulit seperti pembuatan layout dan slider gambar pada bagian **Projects**, serta penggunaan pseudo-class dan pseudo-element seperti `:hover`, `:checked`, `::before`, dan `::marker`. Namun, hasil dari AI tidak langsung saya gunakan sepenuhnya karena solusi yang diberikan terkadang masih terlalu umum dan belum tentu sesuai dengan struktur HTML, desain, dan kebutuhan website saya. Oleh karena itu, saya tetap melakukan penyesuaian dan perbaikan secara manual, seperti mengatur layout Projects agar responsif, menyesuaikan posisi dan ukuran elemen, serta menerapkan pseudo-class dan pseudo-element sesuai dengan fungsinya. Secara keseluruhan, AI membantu saya dalam memahami konsep dan memberikan referensi, tetapi proses implementasi, pengujian, pencarian kesalahan, dan penyesuaian akhir tetap saya lakukan secara manual agar hasilnya sesuai dengan kebutuhan website. Selain itu, saya meminta bantuan ChatGPT untuk memberikan contoh commit yang baik.

### Tugas 2

Dalam pengerjaan tugas ini, saya menggunakan GenAI Claude sebagai alat bantu untuk meningkatkan pemahaman konsep MVT (Model-View-Template) pada Django, terutama untuk menjelaskan urutan alur kerja mulai dari `urls.py` proyek, `urls.py` aplikasi, view, model, hingga template, sehingga saya dapat memahami bagaimana masing-masing komponen tersebut saling terhubung dan berperan dalam menampilkan data ke browser. Selain itu, saya juga meminta bantuan AI untuk menjelaskan apa saja yang perlu diuji pada bagian views, seperti memastikan halaman dapat diakses dengan status code yang sesuai, memastikan template yang digunakan benar, serta memastikan data yang dikirim melalui context muncul dan ditampilkan dengan benar pada halaman, beserta contoh cara menuliskan test case menggunakan `TestCase` dari Django. Saya juga menggunakan AI untuk membantu saya dalam mengoreksi kode yang telah saya buat, khususnya untuk memeriksa kesesuaian antara model, view, dan template, seperti memastikan nama field pada model sudah sesuai dengan yang dipanggil pada view dan template, serta memastikan context yang dikirim dari view sudah sesuai dengan variabel yang digunakan pada template. Meskipun begitu, saya tidak langsung menyalin seluruh saran atau kode yang diberikan AI, melainkan tetap menyesuaikannya dengan struktur model, view, dan template yang telah saya buat sebelumnya, serta melakukan pengujian dan perbaikan secara mandiri untuk memastikan seluruh halaman berjalan dengan benar dan konsisten sesuai kebutuhan tugas.