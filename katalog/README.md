# Tugas 2 PBP

## Identitas
Nama    : Christopher Nathanael Wijaya<br>
NPM     : 2106630044<br>
Kelas   : E

## Link Hasil Deploy
Link untuk menuju ke web yang sudah di-deploy dapat diklik di [sini](https://tugas2christophernw.herokuapp.com/katalog/).

## Jawaban Pertanyaan
### Bagan 
![image](https://user-images.githubusercontent.com/112311278/190147136-523af3f3-1db1-4469-9b68-8d435bb00703.png)
Penjelasan singkat mengenai bagan :
1) Users / Client melakukan request pada server Django.
2) Request dari User / Client diproses oleh `urls.py` sesuai dengan yang ada di dalam `urlpatterns`.
3) Request kemudian masuk ke `views.py` dan diproses oleh fungsi fungsi yang ada.
4) Jika memerlukan akses ke database, `views.py` akan melakukan query ke `models.py`dan akan mengambil data dari database sesuai request.
5) Hasil respons berupa data dari `models.py` yang diambil dari database akan digunakan pada berkas file HTML yang dipilih oleh `views.py`.
6) Berkas HTML beserta hasil respon data yang sudah dipetakan siap untuk dilakukan proses render.
7) Template HTML / Berkas HTML akan ditampilkan di web browser sebagai respon.

### Virtual Environment
Virtual Environment memungkinkan untuk membentuk setiap proyek yang dibangun memiliki environment yang berisi package library yang diperlukan oleh suatu project tersebut secara terisolasi dengan kata lain tidak memengaruhi environment dari projek lainnya. 

Dengan adanya Virtual Environment, maka kita dapat mengisolasi dan memisahkan package library yang diperlukan untuk tiap tiap projek yang ada. Sehingga dnegan ada nya Virtual Environment memungkinkan beberapa projek yang kita miliki menggunakan suatu package library yang sama namun dengan versi yang berbeda tanpa adanya konflik tertenu. Berikut merupakan salah satu contoh kegunaan Virtual Environment, Misalkan terdapat 2 projek A dan B. Projek A dan B menggunakan library yang sama namun dnegan 2 versi berbeda. Projek A menggunakan suatu library versi 2, sedangkan projek B menggunakan library versi 3. Tanpa adanya Virtual Environment, maka kita tidak dapat mengakses projek dengan versi yang tidak bersesuaian, sehingga kita perlu mengatur versi yang digunakan komputer kita untuk menjalankan projek dengan versi library yang bersesuaian. Dengan adanya Virutal Environment maka tiap projek dapat dijalankan menggunakan package library yang telah diisolasi di dalam Virtual Environment projek tersebut, sehingga dalam hal ini tidak memicu terjadinya konflik pada projek lain.

Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan Virtual Environment. Namun, hal tersebut kurang direkomendasikan, karena akan kerap menimbulkan konflik antara satu projek dengan yang lainya. MIsalnya jika terdapat modul / library yang sama yang namun diperlukan 2 versi berbeda untuk tiap-tiap projek. Oleh karena itu direkomendasikan untuk membuat Virtual Environment bagi tiap-tiap projek yang akan kita buat. Agar setiap package dan library yang digunakan dapat terisolasi dalam suatu projek tersebut.

### Tahap-Tahap Implementasi Langkah 1 — 4
1) Membuat fungsi `show_katalog` pada `views.py` milik app katalog dengan parameter request yang berasal dari user. Import `CatalogItem` dari `models.py` pada folder katalog, agar di dalam fungsi dapat mengakses database  melalui model. Kemudian hasilnya akan dibawa ke `katalog.html` bersama-sama dengan context yang bersangkutan untuk ditampilkan.
2) Routing dilakukan dengan memasukan `path('katalog/',include('katalog.urls'))` pada `urlpatterns` dalam folder `project_django` serta memasukan `path('',show_katalog,name= 'show_katalog')` pada `urlpatterns` dalam folder `katalog`. Hal ini dilakukan agar dapat terhubung pada fungsi `show_katalog` yang terdapat pada `views.py` pada folder `katalog`.
3) Melakukan `makemigration` dan `migration` dari model ke database Django. Masing-masing menggunakan perintah `python manage.py makemigrations` dan `python manage.py migrate`. Kemudian melakukan load data yang berada pada `initial_catalog_data.json` dalam folder `katalog/fixtures` dengan perintah `python manage.py loaddata initial_catalog_data.json`. Memetakan data-data tersebut ke `katalog.html` untuk ditampilkan. Data akan diiterasi dari `list_barang` dan HTML juga akan menampilkan `nama` dan `student_id` yang berada dalam `context` yang berkaitan.
4) Worksflows, Procfile, dan lainya telah tersetup. Maka untuk mendeploy web page ini, say membuat APP baru pada Heroku dan menyambungkan nya dengan GitHub Repository yang bersangkutan. Kemudian memasukan `HEROKU_API_KEY` serta `HEROKU_APP_NAME` pada `repository secret` pada GitHub. Workflow yang gagal dijalankan kembali dan web berhasil terdeploy pada web browser.