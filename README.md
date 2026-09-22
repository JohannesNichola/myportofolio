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
4. Install dependencies: `pip install -r requirements.txt`
5. Jalankan migrasi: `python manage.py migrate`
6. Load data awal (agar konten saya langsung tampil): `python manage.py loaddata initial_data`
7. Jalankan: `python manage.py runserver`


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

### Tutorial 3

- Membuat `base.html` sebagai skeleton/template utama dan menerapkan template inheritance pada halaman web.
- Membuat form `ProjectForm` dan `ProjectImageForm`  menggunakan Django `ModelForm` untuk menambahkan Project.
- Mengimplementasikan CSRF protection pada form.
- Mengimplementasikan data delivery menggunakan JSON melalui endpoint API.
- Menambahkan fitur filter Project berdasarkan title.
- Mengimplementasikan serialize dan deserialize data Project.
- Menambahkan fitur delete Project dengan modal konfirmasi.
- Menambahkan responsive layout pada halaman Project dan form.

### Tugas 3

- Melakukan refactoring pada seluruh berkas HTML yang identik (`experience.html`, `education.html`, `project.html`, beserta berkas form-nya) agar menerapkan template inheritance dengan extend dari `base.html`.
- Membuat `ExperienceForm` dan `EducationForm` menggunakan Django `ModelForm` untuk menambahkan data Experience dan Education.
- Menambahkan fitur Create, Update (Edit), dan Delete untuk Project, Experience, dan Education menggunakan form dan modal konfirmasi.
- Menambahkan fitur Update (Edit) khusus untuk Project, termasuk halaman form yang dapat digunakan ulang baik untuk create maupun edit.
- Menambahkan fitur Edit dan Delete pada gambar Project (ProjectImage), termasuk validasi urutan gambar (order) agar tidak terjadi duplikasi slot dan slot yang dihapus langsung tersedia kembali tanpa perlu refresh manual.
- Mengimplementasikan data delivery menggunakan JSON melalui endpoint API untuk Experience dan Education, mengikuti pola yang sudah diterapkan pada Project.
- Menambahkan fitur filter/search berdasarkan title untuk Experience dan Education.
- Menambahkan modal popup untuk menampilkan gambar Project dalam ukuran asli.
- Menyesuaikan tampilan grid Project agar lebih rapi dan tidak terlalu memanjang ke bawah pada layar laptop.
- Menambahkan unit test untuk seluruh fungsi CRUD dan endpoint JSON pada Experience, Education, dan Project.

### Tutorial 4

- Mengimplementasikan sistem autentikasi menggunakan model `User` bawaan Django, dengan `UserCreationForm` untuk registrasi dan `AuthenticationForm` untuk login.
- Membuat halaman Register dan Login (`register.html`, `login.html`) yang mewarisi `base.html`.
- Menambahkan fungsi logout yang menghapus session pengguna.
- Menampilkan status login pengguna (username dan tombol Logout, atau tombol Login dan Register) pada navbar di `base.html`.
- Mengimplementasikan cookie kustom `last_login` yang dibuat saat pengguna login dan dihapus saat logout, menggunakan `set_cookie()` dan `delete_cookie()`.
- Menampilkan informasi sesi terakhir login pada halaman utama (`index.html`) dengan membaca `request.COOKIES`.
- Mengimplementasikan otorisasi menggunakan `@login_required` dan pengecekan `is_superuser` pada fungsi Create dan Delete Project, sehingga hanya pemilik portofolio yang dapat menambah dan menghapus proyek.
- Menyembunyikan tombol Add Project, Edit Project, Edit Image, dan Delete Project pada template untuk pengguna yang bukan pemilik portofolio.
- Menambahkan field `starred_by` (ManyToManyField ke model `User`) pada model Project untuk menyimpan data star.
- Menambahkan fitur star/unstar pada Project yang dapat digunakan oleh seluruh pengguna yang sudah login (tidak terbatas pada pemilik portofolio).
- Menyesuaikan endpoint JSON Project (`get_projects_json`) menggunakan `use_natural_foreign_keys=True` agar data `starred_by` ditampilkan dalam bentuk username, bukan id pengguna.

## Pertanyaan Reflektif

### Tugas 1

1. Pada pembuatan website portofolio ini, saya menggunakan elemen semantik HTML5, terutama `<section>`. Saya menggunakan `<section>` untuk membagi halaman berdasarkan bagian kontennya, seperti bagian profile dan portfolio. Menurut saya, penggunaan `<section>` membuat struktur HTML menjadi lebih rapi dan lebih mudah dipahami karena setiap bagian memiliki kelompok konten masing-masing. Selain itu, penggunaan `<section>` juga memudahkan saya saat mengatur tampilan menggunakan CSS karena setiap bagian dapat diberikan styling sesuai dengan kebutuhannya. Walaupun website yang dibuat masih berupa static web, struktur seperti ini menurut saya akan memudahkan jika nantinya ingin menambahkan atau mengembangkan konten. Selain `<section>`, penggunaan elemen seperti `<header>`, `<main>`, `<nav>`, dan `<footer>` membantu saya dalam membagi halaman berdasarkan fungsinya.

2. Tantangan yang saya temukan dalam membuat website responsive ada pada bagian Projects. Pada tampilan desktop, bagian ini menggunakan CSS Grid dengan dua kolom, yaitu informasi proyek di sebelah kiri dan gambar di sebelah kanan. Namun, jika ukuran layar lebih kecil, tampilan dua kolom tersebut menjadi terlalu sempit. Karena itu, saya menggunakan `@media` untuk mengubah layout menjadi satu kolom pada layar yang lebih kecil. Dengan begitu, informasi proyek dan gambar akan ditampilkan secara vertikal agar lebih nyaman dilihat, terutama pada perangkat mobile.

3. Salah satu batasan yang saya rasakan dari static web adalah keterbatasan dalam membuat interaksi yang lebih dinamis. Pada bagian Experience, Education, Skills, dan Projects, saya menggunakan `<details>` dan `<summary>` untuk membuat dropdown, tetapi animasinya masih cukup terbatas ketika bagian tersebut dibuka dan ditutup berulang kali. Selain itu, slider gambar pada bagian Projects masih menggunakan radio button, sehingga pengguna hanya bisa berpindah gambar dengan menekan titik navigasi. Pada iterasi selanjutnya, saya ingin menambahkan JavaScript agar slider dapat digeser menggunakan click and drag pada desktop serta swipe pada perangkat mobile. Menurut saya, fitur tersebut dapat membuat interaksi website terasa lebih natural dan nyaman digunakan.

### Tugas 2

1. Alur dimulai ketika pengguna membuka URL halaman portofolio baru di browser, misalnya `/experience/`. Permintaan (request) tersebut pertama kali diterima oleh `urls.py` milik proyek, yang menjadi pintu masuk utama untuk menentukan aplikasi mana yang bertanggung jawab menangani URL tersebut. Karena path-nya cocok dengan salah satu pola yang di-include dari aplikasi `main`, request kemudian diteruskan ke `urls.py` milik aplikasi, yang memetakan path spesifik tersebut ke sebuah fungsi view tertentu, dalam hal ini `show_experience`. Di dalam view, Django akan mengambil data yang dibutuhkan dengan memanggil model `Experience` melalui Django ORM, misalnya menggunakan `Experience.objects.all()`, sehingga model berperan sebagai perantara antara aplikasi dan database untuk mengambil, menyimpan, atau memanipulasi data. Data yang berhasil diambil kemudian dimasukkan ke dalam sebuah context (berupa dictionary) dan dikirim ke template melalui fungsi `render()`. Template, yang berisi berkas HTML dengan sintaks Django Template Language, kemudian menerima context tersebut dan menampilkan data secara dinamis menggunakan tag seperti `{% for %}` dan `{{ }}`. Hasil akhir dari proses render ini berupa HTML murni yang dikirim kembali oleh Django sebagai response, sehingga browser dapat menampilkannya kepada pengguna sebagai halaman portofolio yang utuh.

2. Menyimpan data pada model jauh lebih baik dibandingkan menuliskannya langsung di dalam template karena template seharusnya hanya berfokus pada bagaimana data ditampilkan, bukan menyimpan data itu sendiri. Jika data ditulis langsung di template (hard code), setiap kali ada perubahan data, seperti menambah pengalaman baru atau mengubah deskripsi skill, saya harus mengedit langsung berkas HTML, yang berisiko membuat struktur template menjadi berantakan dan sulit dibaca seiring bertambahnya data. Dengan menyimpan data pada model, saya cukup menambahkan, mengubah, atau menghapus data melalui Django admin atau Python shell tanpa perlu menyentuh kode template maupun view sama sekali. Hal ini juga membuat aplikasi lebih mudah dikembangkan, karena data yang tersimpan di database dapat digunakan kembali di berbagai halaman atau fitur lain tanpa perlu duplikasi, serta pemeliharaan aplikasi menjadi lebih rapi karena adanya pemisahan yang jelas antara logika data (model), logika tampilan (template), dan logika proses (view).

3. `makemigrations` berfungsi untuk membuat berkas migrasi berdasarkan perubahan yang saya lakukan pada model, seperti menambah field baru, mengubah tipe data, atau menghapus field, di mana berkas ini berisi instruksi perubahan struktur database dalam bentuk kode python, namun perubahaan tersebutt belum benar-benar diterapkan ke database. Sementara itu, `migrate` berfungsi untuk mengeksekusi berkas migrasi tersebut sehingga perubahan strukturnya benar-benar diterapkan ke database yang sebenarnya. Sebagai contoh, ketika saya mengubah model `Skill` dengan menghapus field `tags` dan `started_at` karena diputuskan untuk tidak digunakan, saya perlu menjalankan `makemigrations` terlebih dahulu agar Django membuatkan berkas migrasi yang mencatat perubahan penghapusan kolom tersebut, kemudian menjalankan `migrate` agar kolom `tags` dan `started_at` benar-benar dihapus dari tabel `Skill` di database. Jika saya hanya menjalankan `makemigrations` tanpa `migrate`, perubahan tersebut hanya akan tercatat sebagai rencana migrasi, tetapi struktur tabel di database belum benar-benar berubah.

### Tugas 3

1. Saya menggunakan `ModelForm` alih-alih membuat form HTML secara manual karena `ModelForm` secara otomatis menghasilkan field form berdasarkan field yang ada pada model, sehingga saya tidak perlu menuliskan ulang setiap `<input>` beserta validasinya satu per satu. Selain itu, `ModelForm` juga otomatis menyediakan validasi data sesuai dengan tipe data pada model, misalnya memastikan `started_at` benar-benar berupa tanggal yang valid atau memastikan field yang wajib diisi (`blank=False`) tidak dikirim kosong, tanpa saya perlu menulis logika validasi tersebut secara manual di view. Ketika data valid, saya juga dapat langsung memanggil method `save()` untuk menyimpan data ke database, sehingga proses dari validasi hingga penyimpanan data menjadi jauh lebih ringkas dan konsisten dengan struktur model yang sudah dibuat. Selain itu, alasan `{% csrf_token %}` wajib ditambahkan pada setiap form adalah karena token ini berfungsi untuk mencegah serangan Cross-Site Request Forgery (CSRF), yaitu serangan di mana pihak lain mencoba mengirimkan request (misalnya uodate/delete data) atas nama pengguna yang sedang login tanpa sepengetahuan pengguna tersebut. Django akan menyisipkan token unik pada setiap form yang di-render, dan ketika form tersebut disubmit, Django akan memverifikasi bahwa token yang dikirim cocok dengan token yang diharapkan sebelum memproses request. Apabila token tidak ada atau tidak valid, Django akan menolak request tersebut, sehingga data pada aplikasi menjadi lebih aman dari manipulasi pihak yang tidak berwenang.

2. JSON lebih disukai dibandingkan XML dalam pengembangan aplikasi web modern karena beberapa alasan. Pertama, struktur JSON jauh lebih ringkas dibandingkan XML karena tidak memerlukan closing tag pada setiap elemen, sehingga ukuran data yang dikirim melalui jaringan menjadi lebih kecil dan proses transfer data menjadi lebih cepat, terutama untuk aplikasi dengan banyak request seperti API. Kedua, JSON memiliki struktur yang sangat mirip dengan objek pada JavaScript, sehingga proses parsing data di sisi client (browser) menjadi lebih mudah dan cepat menggunakan `JSON.parse()`, tanpa memerlukan parser tambahan seperti pada XML yang membutuhkan DOM parser atau XML parser yang lebih kompleks. Ketiga, hampir seluruh bahasa pemrograman modern, termasuk Python dan JavaScript, sudah menyediakan library bawaan untuk mengubah data menjadi JSON (serialize) maupun sebaliknya (deserialize), sehingga developer tidak perlu menulis banyak kode tambahan hanya untuk memproses format data tersebut. 

3. Ketika saya mengakses endpoint yang mengembalikan data dalam format JSON, misalnya `/api/experiences/`, alur dimulai ketika request diterima oleh view `get_experiences_json`. Di dalam view tersebut, saya mengambil data dari database menggunakan Django ORM, misalnya `Experience.objects.all()`, yang hasilnya berupa QuerySet, yaitu kumpulan objek model Python. Objek model tersebut tidak dapat langsung dikirim sebagai response karena format objek Python tidak dapat dipahami langsung oleh client (browser atau aplikasi lain) yang mengharapkan data dalam format teks standar seperti JSON. Oleh karena itu, saya perlu melakukan proses serialization menggunakan `serializers.serialize("json", experiences)`, yaitu proses mengubah objek model Django menjadi representasi teks dalam format JSON yang berisi field-field beserta value-nya dalam bentuk string terstruktur. Setelah proses serialization selesai, hasilnya saya kirim sebagai `HttpResponse` dengan `content_type="application/json"` agar client mengetahui bahwa data yang diterima berupa JSON. Di samping itu, ketika saya ingin menampilkan data tersebut di halaman web (seperti pada `show_experience`), saya perlu melakukan proses sebaliknya, yaitu deserialization, menggunakan `serializers.deserialize("json", ...)`, agar data JSON tersebut dapat diubah kembali menjadi objek model Django yang dapat diakses field-nya (misalnya `experience.title`) dan ditampilkan secara dinamis melalui template. Jadi, kita perlu melakukan proses serialization pada model Django sebelum datanya dikembalikan karena format objek Python tidak dapat dipahami langsung oleh client yang mengharapkan data dalam format teks standar seperti JSON.

## AI Disclosure

### Tugas 1

Dalam pengerjaan tugas ini, saya menggunakan GenAI ChatGPT sebagai alat bantu untuk memahami konsep dan mendapatkan referensi, terutama pada bagian yang paling sulit seperti pembuatan layout dan slider gambar pada bagian **Projects**, serta penggunaan pseudo-class dan pseudo-element seperti `:hover`, `:checked`, `::before`, dan `::marker`. Namun, hasil dari AI tidak langsung saya gunakan sepenuhnya karena solusi yang diberikan terkadang masih terlalu umum dan belum tentu sesuai dengan struktur HTML, desain, dan kebutuhan website saya. Oleh karena itu, saya tetap melakukan penyesuaian dan perbaikan secara manual, seperti mengatur layout Projects agar responsif, menyesuaikan posisi dan ukuran elemen, serta menerapkan pseudo-class dan pseudo-element sesuai dengan fungsinya. Secara keseluruhan, AI membantu saya dalam memahami konsep dan memberikan referensi, tetapi proses implementasi, pengujian, pencarian kesalahan, dan penyesuaian akhir tetap saya lakukan secara manual agar hasilnya sesuai dengan kebutuhan website. Selain itu, saya meminta bantuan ChatGPT untuk memberikan contoh commit yang baik.

### Tugas 2

Dalam pengerjaan tugas ini, saya menggunakan GenAI Claude sebagai alat bantu untuk meningkatkan pemahaman konsep MVT (Model-View-Template) pada Django, terutama untuk menjelaskan urutan alur kerja mulai dari `urls.py` proyek, `urls.py` aplikasi, view, model, hingga template, sehingga saya dapat memahami bagaimana masing-masing komponen tersebut saling terhubung dan berperan dalam menampilkan data ke browser. Selain itu, saya juga meminta bantuan AI untuk menjelaskan apa saja yang perlu diuji pada bagian views, seperti memastikan halaman dapat diakses dengan status code yang sesuai, memastikan template yang digunakan benar, serta memastikan data yang dikirim melalui context muncul dan ditampilkan dengan benar pada halaman, beserta contoh cara menuliskan test case menggunakan `TestCase` dari Django. Saya juga menggunakan AI untuk membantu saya dalam mengoreksi kode yang telah saya buat, khususnya untuk memeriksa kesesuaian antara model, view, dan template, seperti memastikan nama field pada model sudah sesuai dengan yang dipanggil pada view dan template, serta memastikan context yang dikirim dari view sudah sesuai dengan variabel yang digunakan pada template. Meskipun begitu, saya tidak langsung menyalin seluruh saran atau kode yang diberikan AI, melainkan tetap menyesuaikannya dengan struktur model, view, dan template yang telah saya buat sebelumnya, serta melakukan pengujian dan perbaikan secara mandiri untuk memastikan seluruh halaman berjalan dengan benar dan konsisten sesuai kebutuhan tugas.

### Tugas 3

Dalam pengerjaan tugas ini, saya menggunakan GenAI Claude sebagai alat bantu untuk  membantu proses refactoring HTML agar seluruh halaman menerapkan template inheritance dari `base.html`, serta untuk membantu saya dalam membuat `ExperienceForm`, `EducationForm`, beserta fungsi view CRUD untuk Experience dan Education dengan pola yang konsisten dengan implementasi Project yang sudah ada sebelumnya. Selain itu, saya juga meminta bantuan AI pada saat memeriksa kesamaan desain antar halaman, seperti memastikan struktur CSS class, posisi tombol, dan tata letak antar section (Experience, Education, Project) konsisten satu sama lain, mengingat beberapa bug yang saya temui justru berasal dari class CSS yang tidak konsisten digunakan antar halaman (misalnya perbedaan margin akibat class yang sama dipakai ulang untuk section yang berbeda). Saya juga menggunakan AI untuk membantu saya melengkapi unit test agar coverage testing pada seluruh fungsi CRUD dan endpoint JSON agar seluruh fungsi tercover. Selain itu, GenAI membantu saya dalam membuat initial data saya. Meskipun begitu, saya tetap melakukan verifikasi terhadap seluruh kode dan test case yang dihasilkan AI dengan menjalankan `python manage.py test` serta mencoba secara manual melalui `runserver`, dan melakukan penyesuaian pada bagian yang tidak sesuai dengan struktur model, view, maupun template yang telah saya buat sebelumnya, agar seluruh fitur berjalan dengan benar dan konsisten sesuai kebutuhan tugas.