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
