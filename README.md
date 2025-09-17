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

