# Tugas 3 PBP

## Identitas
Nama    : Christopher Nathanael Wijaya<br>
NPM     : 2106630044<br>
Kelas   : E

## Link Hasil Deploy
Link untuk menuju ke web yang sudah di-deploy dapat diklik di [sini](https://tugas2christophernw.herokuapp.com/mywatchlist/).

## Screenshots dari Postman
### HTML
![image](https://user-images.githubusercontent.com/112311278/191530730-c00a247b-4605-42de-92dc-e51511007d29.png)
### JSON
![image](https://user-images.githubusercontent.com/112311278/191531162-af1b67dc-364d-400a-83ff-813a3cda8c13.png)
### XML
![image](https://user-images.githubusercontent.com/112311278/191531334-9d7351ab-7a36-4d2b-8369-2b4099144d70.png)


## Jawaban Pertanyaan
### Perbedaan JSON, XML, dan HTML
Baik JSON,XML, serta HTML merupakan format dari _data delivery_ yang sering dipakai di Django pada aplikasi platform. Namun HTML (_HyperText Markup Language_) biasanya lebih ditujukan untuk menampilkan data pada browser. HTML juga biasanya digunakan bersama-sama dengan CSS untuk mendesain bagian HTML tags. XML (_eXtensible Markup Language_) menggunakan format tags yang mirip seperti yang digunakan oleh HTML. Naun pada XML penerapanya bebas menggunakan tag yang dibuat sendiri (wajib memiliki tag penutup), sedangkan HTML hanya bisa menggunakan tag tertentu yang sesuai (terkadang tidak memerlukan tag penutup). Kemudian beberapa perbedaan lainya seperti, XML bersifat _case sensitive_ sedangkan HTML bersifat _case insensitive_. XML bersifat dinamis karena ditujukan untuk transfer data, sedangkan HMTL bersifat statis karena bertujuan untuk menampilkan data. JSON (_JavaScript Object Notation_) merupakan format file turunan dari JavaScript yang mirip dengan notasi _dictionary_ Python. JSON memiliki sintaks yang lebih ringkas dan mudah dipahami jika dibandingkan dengan XML. Kemudian, JSON lebih ringan dan cepat serta tidak menggunakan tag, sedangkan XML cenderung lebih lambat dibandingkan dengan JSON dan membutuhkan tag pembuka dan tag penutup. Dengan sintaks yang lebih mudah dipahami membuat JSON lebih popular dibandingkan dengan XML dalam digunakan untuk mendevelop suatu web applications.

### Pentingnya Data Delivery
Pertukaran data akan sering terjadi dari satu _stack_ ke _stack_ lainya, seperti misalnya antara _client_ dan _server_. Data Delivery merupakan suatu saran untuk mengirimkan data antar _stack_ tersebut. Sehingga komunikasi antar komputer dan terlaksana dan kita dapat mengirim, menyimpan, serta menggunakan data dengan format yang dibutuhkan pula.

### Implementasi Checklists
1) Membuat suatu app baru bernama "mywatchlist" dengan melakukan perintah `python manage.py startapp mywatchlist`.
3) Menambahkan "mywatchlist" ke `INSTALLED_APPS` pada `project_django/settings.py`.
4) Menambahkan routing berupa `path("mywatchlist/", include("mywatchlist.urls"))` ke `urlpatterns` di `project_django/urls.py`.
5) Membuat suatu class "MyWatchList" model pada `models.py` milik app mywatchlist dan menjalankan perintah `python manage.py makemigrations` dan `python manage.py migrate` untuk melakukan migrasi model ke database.
6) Membuat file json dnegan nama `initial_mywatchlist_data.json` pada `mywatchlist/fixtures/`.
7) Membuat fungsi `show_watchlist`, `show_json`, dan `show_xml` pada `views.py` pada app mywatchlist.
8) Membuat `app_name` dan routing pada `urlpatterns` di `mywatchlist/urls.py`.
9) Load data dari `initial_mywatchlist_data.json` dengan perintah `python manage.py loaddata initial_mywatchlist_data.json`.
10) Membuat `mywatchlist.html` di `mywatchlist/templates/`. 
11) Membuat  `test.py` di `mywatchlist/`.
12) Melengkapi isi dari `Procfile` agar dapat menampilkan data dari `initial_mywatchlist_data.json` saat di deploy di Heroku.
13) Selesai.