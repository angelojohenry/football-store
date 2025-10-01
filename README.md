TUGAS 2
1. - membuat direktori baru dengan nama "football-store", lalu mengaktifkan virtual environment di terminal
   - membuat file baru bernama "requirements.txt" yang diisi dengan dependencies, lalu menginstallnya
   - membuat proyek django bernama "football_store" dengan perintah "django-admin startproject football_store"
   - membuat file .env dan .envprod dan melakukan beberapa modifikasi pada settings.py
   - membuat repositori github baru, lalu mengunggah proyek ke dalamnya
   - deploy proyek ke pws
   - menjalankan perintah "python manage.py startapp main" pada direktori football-store
   - membuka settings.py lalu menambahkan main pada variable INSTALLED_APPS
   - membuat direktori baru di dalam main, lalu membuat main.html
   - membuat class Store dan menambahkan atribut name, price, description, thumbnail, category dan is_featured pada models.py
   - membuat fungsi show_main di views.py untuk menampilkan teks dari template html
   - memodifikasi main.html agar bisa menampilkan nama aplikasi, nama dan kelas
   - membuat file urls.py pada direktori main, mengimpor fungsi path dari django.urls, dan fungsi show_main yang sudah dibuat tadi
   - membuat variable app_name dan urlpatterns
   - mengimpor fungsi path dan include dari django.urls di urls.py pada direktori football_store
   - membuat list urlpatterns dan menambahkan main.urls
   - melakukan push ke pws

2. <img width="667" height="710" alt="image" src="https://github.com/user-attachments/assets/177aa5b8-0d89-4363-87e7-26906733918d" />
3. Peran settings.py dalam proyek django adalah:
   - menentukan engine database, nama database, username, password, host, dan port
   - menyimpan daftar aplikasi yang digunakan di dalam proyek
   - menentukan urutan middleware yang mengatur request/response
   - menentukan direktori template html
   - menyimpan konfigurasi keamanan seperti SECRET_KEY, DEBUG, dan ALLOWED_HOSTS
   - menentukan bahasa default dan zona waktu
4. Cara kerja migrasi database di django
   - ketika kita menjalankan perintah "python manage.py makemigrations", maka django akan membaca perubahan di models.py, lalu membuat file di folder migrations yang berisi instruksi python untuk mengubah database seperti migrations.CreateModel
   - lalu saat kita menjalankan perintah "python manage.py migrate", maka django akan mengeksekusi file tersebut
5. Menurut saya, django dijadikan permulaan pembelajaran pengembangan perangkat lunak karena memiliki library yang sudah lengkap dan juga struktur yang jelas

TUGAS 3
1. Kita memerlukan data delivery dalam pengimplementasian platform untuk mengirimkan data dari satu stack ke stack lainnya.
2. Menurut saya JSON lebih baik dari XML.
JSON lebih populer dan banyak digunakan daripada XML karena:
- lebih singkat & mudah dibaca
- lebih cepat diproses oleh aplikasi
- lebih efisien
3. Method is_valid() pada form django berfungsi untuk menjalankan proses validasi untuk memeriksa apakah semua field dalam form sudah sesuai dengan aturan yang ditentukan, misalnya tidak kosong, tidak melebihi panjang maksimal, dan lainnya.
  Kita membutuhkan method is_valid() sebagai gerbang utama sebelum data diproses dan untuk menjamin hanya data valid yang dapat masuk.
4. Kita membutuhkan csrf_token saat membuat form di django untuk sebagai verifikasi dan    mencegah request palsu dari situs lain
Jika tidak ada csrf_token maka aplikasi kita akan rentan terhadap csrf attack
Penyerang dapat memanfaatkan hal tersebut dengan cara:
- menaruh form tersembunyi di halaman mereka yang otomatis submit ke aplikasi target
- Menggunakan request GET dengan parameter berbahaya
- Membuat user mengklik link yang mengirim request tanpa sepengetahuan mereka
5. Cara saya mengimplementasikan checklist:
- Membuat direktori templates pada root folder
- membuat file base.html
- menambahkan direktori tersebut agar terdeteksi sebagai file template di bagian TEMPLATES pada settings.py
- memodifikasi file main.html agar mengextend dari base.html
- membuat file forms.py pada direktori main untuk membuat struktur form yang dapat menerima data item baru untuk football store.
- menambahkan beberapa import dan fungsi baru pada views.py seperti add_object dan show_object
- memodifikasi kode pada main.html agar bisa menampilkan data dari item serta tombol Add yang akan redirect ke halaman form
- membuat 2 file HTML baru pada main/templates yaitu add_object.html dan object_detail.html
- menambahkan CSRF_TRUSTED_ORIGINS pada settings.py
- membuat 4 fungsi baru yaitu show_xml, show_json, show_xml_by_id, show_json_by_id pada views.py
- menambahkan path url ke dalam urlpatterns
<img width="1074" height="770" alt="image" src="https://github.com/user-attachments/assets/cc33411e-c334-4a38-a739-2824c1600ff7" />
<img width="1087" height="728" alt="image" src="https://github.com/user-attachments/assets/8110caf5-aec3-4402-a57d-6706278f4023" />
<img width="1067" height="706" alt="image" src="https://github.com/user-attachments/assets/e889de9c-2fba-4bd2-bb95-fb9fb40c3b87" />
<img width="1122" height="919" alt="image" src="https://github.com/user-attachments/assets/4e085869-3f89-48b6-b2da-ad12a4769ef3" />

TUGAS 4
1. Django AuthenticationForm adalah form bawaan dari modul django.contrib.auth.forms. Form ini sudah menyediakan field username dan password serta memvalidasi apakah kredensial yang dimasukkan sesuai dengan kredensial user di database
Kelebihan:
   - Tidak perlu membuat form dari nol
   - Validasi otomatis
   - Keamanan terjamin
Kekurangan:
   - Username dan password terbatas
   - Kurang fleksibel
2. Autentikasi bertujuan untuk memverifikasi identitas pengguna sedangkan otorisasi bertujuan untuk menentukan hak akses pengguna terhadap resource
Implementasi autentikasi pada Django:
   - Django menyediakan model User dengan field seperti username dan password
   - Login dan logout ditangani oleh django.contrib.auth.authenticate(), django.contrib.auth.login(), django.contrib.auth.logout()
Implementasi otorisasi pada Django:
   - Decorator @login_required yang membatasi akses hanya untuk user yang sudah login
   - Cek apakah user login dengan user.is_authenticate 
3.
Session
Kelebihan:
   - Lebih aman karena data sensitif tidak disimpan di browser
   - Lebih fleksibel karena dapat menyimpan object/data kompleks
   - Ukuran lebih besar dan tidak terbatas seperti cookie
   - Integrasi dengan autentikasi
Kekurangan:
   - Data session disimpan di memori, database, atau cache sehingga dapat membebani server jika user banyak
   - Tidak persisten karena biasanya hilang setelah browser ditutup
   - Bergantung pada cookie atau URL rewriting
Cookies
Kelebihan:
   - Lebih persisten karena dapat bertahan walau browser ditutup
   - Tidak perlu resource server
   - Cocok untuk preferensi user
Kekurangan:
   - Rentan dimanipulasi
   - Ukuran terbatas
   - Bisa disalahgunakan lewat cookie theft
4. Penggunaan cookies tidak sepenuhnya aman secara default dan ada beberapa risiko potensial yang harus diwaspadai seperti manipulasi data, cookie theft, session hijacking, dan CSRF
Django menangani risiko-risiko tersebut dengan:
   - CSRF protection dengan otomatis menambahkan CSRF token pada form POST
   - Password hashing
   - Tidak menyimpan data sensitif pada cookie, hanya session ID
   - Cookie signing
   - Secure flags
5. Implementasi checklist:
   - Mengimpor UserCreationForm, messages, authenticate, login, logout, AuthenticationForm pada views.py
   - Membuat fungsi register, login_user, dan logout_user di views.py
   - Membuat file register.html dan login.html pada main/templates
   - Mengimpor fungsi register, login_user dan logout_user di urls.py lalu menambahkan path url ke urlpatterns
   - Membuat tombol logout pada main.html
   - Mengimpor decorator login_required di views.py dan menambahkannya pada fungsi show_main dan show_object
   - Mengimpor datetime, HttpResponseRedirect dan reverse pada views.py
   - Memodifikasi fungsi login_user agar dapat menyimpan cookie bernama last_login yang berisi timestamp terakhir user melakukan login, lalu menambahkannya ke dalam variable context pada fungsi show_main
   - Memodifikasi fungsi logout_user agar dapat menghapus cookie last_login ketika user logout
   - Menambahkan tampilan data waktu login terakhir user pada main.html
   - Mengimpor model User dan menambahkan atribut user pada class Product
   - Menjalankan perintah python manage.py makemigrations dan python manage.py migrate
   - Memodifikasi fungsi add_object pada views.py agar setiap objek yang dibuat akan otomatis terhubung dengan pengguna yang membuatnya
   - Memodifikasi fungsi show_main dengan menambahkan filter produk dengan 2 opsi yaitu "all" untuk menampilkan semua produk dan "my" untuk menampilkan produk yang dibuat oleh user
   - Menambahkan tombol filter my dan all pada main.html
   - Menambahkan tampilan nama author pada object_detail.html
   - Membuat 2 akun, lalu menambahkan masing-masing 3 produk di lokal
   - Add, commit, lalu push ke github dan pws

TUGAS 5
1. Urutan prioritas pengambilan CSS selector yaitu:
   Inline style > ID selector > Class/pseudo-class/attribute selector > Element/tag selector
2. Responsive design menjadi konsep yang penting dalam pengembangan aplikasi web karena:
   - Berbagai jenis perangkat yang digunakan oleh user seperti HP, laptop dan tablet
   - Meningkatkan user experience
   - Konsistensi tampilan di berbagai device
Contoh aplikasi yang sudah responsive adalah Youtube, karena layout video menyesuaikan layar, dan    menunya berubah menjadi hamburger menu di mobile
Contoh aplikasi yang belum responsive adalah website lama seperti forum-forum jadul, karena tampilan pecah di layar hp atau teks yang terlalu kecil
3. Perbedaan dari margin, border dan padding:
- Margin: ruang di luar elemen, memberi jarak antar elemen
- Border: garis tepi yang membungkus elemen
- Padding: ruang antara konten dan border
Implementasinya yaitu:
.box {
  margin: 20px;
  border: 2px solid black;
  padding: 15px;
} 
4. Flexbox:
  - Digunakan untuk mengatur layout 1 dimensi (horizontal dan vertikal)
  - Elemen fleksibel, mudah diatur align, justify dan order
  - Cocok untuk membuat navbar, daftar kartu, tombol sejajar.
Grid:
  - Digunakan untuk layout 2 dimensi (baris dan kolom)
  - Cocok untuk membuat tabel, dashboard, layout halaman penuh
  - Bisa mengatur area dengan presisi
5.  Implementasi checklist:
    - menambahkan script CDN dari Tailwind pada base.html di bagian head
    - Membuat fungsi edit_product dan delete_product di views.py
    - Membuat berkas edit_product.html pada main/templates
    - Import fungsi edit_product dan delete_product di urls.py dan menambahkan path urlnya di urlpatterns
    - Menambahkan tombol edit dan delete di main.html
    - Membuat navbar.html di root directory
    - include navbar.html pada main.html
    - Menambahkan middleware WhiteNoise pada settings.py
    - Mengkonfigurasi variabel STATIC_ROOT, STATICFILES_DIRS, dan STATIC_URL
    - Membuat direktori baru bernama static dan membuat direktori bernama css di dalamnya
    - Membuat file global.css pada static/css
    - Menghubungkan global.css dengan base.html
    - Menambahkan custom styling ke global.css
    - Melakukan styling pada navbar.html, login.html, register.html
    - Membuat file card_product.html pada main/templates
    - Menggunakan card_product.html pada main.html
    - Melakukan styling pada object_detail.html, add_object, dan edit_product
    - add, commit, push ke git dan pws
