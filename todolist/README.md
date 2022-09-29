# Tugas 4 PBP

## Identitas
Nama    : Christopher Nathanael Wijaya<br>
NPM     : 2106630044<br>
Kelas   : E

## Link Hasil Deploy
Link untuk menuju ke web yang sudah di-deploy dapat diklik di [sini](https://tugas2christophernw.herokuapp.com/todolist/login/).

## Jawaban Pertanyaan
### Kegunaan `{% csrf_token %}`
`{% csrf_token %}`berguna untuk menghindari adanya serangan berupa CSRF (Cross Site Request Forgery). Pada dasarnya, `{% csrf_token %}` meng-generate suatu token random yang tidak diketahui siapapun. Suatu request akan diterima jika terdapat validasai atau kecocokan pada `{% csrf_token %}`yang tepat. Sehingga jika ada suatu request tanpa `{% csrf_token %}` yang tepat, request tersebut pasti ditolak.

CSRF token dikirim oleh server ke client dan client harus mengirim kembali token tersebut dari bagian dari request yang dilakukan selanjutnya. Apabila token tidak sesuai, maka reqeust tersebut akan di-reject oleh pihak server.

### Pembuatan Form secara manual
Pembuatan suatu form seara manual dapat dilakukan tanpa menggunakan `{{ form.as_table }}`. Kita dapat menggunakan tag `<form>`, menentukan request dari suatu form, dan mengatur kemana form akan dikirm dengan mengatur attribute `action`. Kemudian kita harus mengisi form tersebut dengan input field yang bisa digunakan di html, serta menambahkan button untuk melakukan submission form tersebut. Terakhir kita mengatur routing dan function akan memproses data yang dikirimkan form tersebut.

### Alur Data
Pengisian form oleh user akan disimpan pada browser user. Setelah tombol submit ditekan, form akan terkirim sebagai suatu HTTP request. Data kemudian diterima oleh server, Oleh server data di proses dan mengubah data pada database jika diperlukan. Ketika user meminta data dari server, server akan mengirimkan data baru yang baru dari data base.

### Implementasi Checklists
1) Membuat suatu app baru `todolist` dengan menjalankan program `python manage.py startapp todolist`, serta menambahkan `todolist` pada app di `settings.py`.
2) Melakukan routing pada `urls.py` di `project_django` dengan menambahkan `path('todolist/', include('todolist.urls'))`.
3) Membuat model `Task` pada `models.py` dengan beberapa field yang sesuai.
4) Membuat file html berupak `login.html` dan `register.html` pada `templates` di `todolist` dan membuat function yang terkait pada bagain `views.py` di `todolist`, berupak fungsi `login_user`, `register`, dan `logout`.
5) Membuat file baru pada `templates` berupa `todolist.html` dan membuat fungsi `todolist` pada `views.py` di app `todolist`.
6) Membuat file html `add_task.html` pada `templates` di `todolist` dan membuat fungsi `create_task`, `change_status`, dan `delete` pada `views.py` di `todolist`.
7) Melakukan routing pada `ursl.py` di `todolist` sesuai dengan fungsi yang bersangkutan di `views.py`. 
8) Deploy ke Heroku secara otomatis dengan malukan push ke repositori GitHub

### Akun
1) USERNAME: uchiha_madara    PASSWORD: thestrongestuchiha
2) USERNAME: senju_hashirama  PASSWORD: thestrongestshinobi
