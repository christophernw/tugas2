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

# Tugas 5 PBP

## Identitas
Nama    : Christopher Nathanael Wijaya<br>
NPM     : 2106630044<br>
Kelas   : E

## Link Hasil Deploy
Link untuk menuju ke web yang sudah di-deploy dapat diklik di [sini](https://tugas2christophernw.herokuapp.com/todolist/login/).

## Jawaban Pertanyaan
### Perbedaan Inline, Internal, dan External CSS
Inline CSS ditulis sebagai attribute dari sebuah tag HTML. Internal CSS dituliskan di dalam tag khusus, yaitu `<style>`. Tag ini biasanya ditempatkan dibagian header dari file html yang bersangkutan. External CSS merupakan metode penulisan CSS pada file berekstensi `.css` yang terpisah dengan halaman HTML. 

Inline CSS pada dasarnya cocok digunakan untuk menambahkan sedikit style pada sebuah tag dan mengoverride style lain yang ada. Namun jika terlalu banyak style yang ditambahkan, file HTML akan sulit untuk dibaca. Internal CSS cocok untuk menambahkan banyak style pada satu buah file HTML saja karena tidak perlu mengimport file lain. Internal CSS tidak coock untuk menambahkan banyak style pada banyak file HTML karena tiap file perlu menambahkan style nya masing-masing. Selain itu Internal CSS dapat membuat ukuran file HTML menjadi lebih besar. External CSS cocok untuk menambahkan style yang banyak dan kompleks ke beberapa file HTML. Kekurangan dari External CSS dalah tiap file HTMl perlu mengimport file CSS yang akan digunakan sehingga menambah waktu bagi browser mengload website.

### Tag HTML5
Berikut beberapa tag pada HTML5:
- `<a>` -> menambahkan hyperlink
- `<b>` -> bold teks
- `<div>` -> mendefinisikan suatu division atau bagian tertentu dalam suatu HTML
- `<form>` -> mendefinisikan suatu form untuk mengambil input user
- `<img>` -> menambahkan gambar
- `<span>` -> mendefinisikan bagian pada suatu teks menjadi inline dan styless
- `<style>` -> tempat mendefinisikan internal CSS dalam suatu halaman HTML
- `<th>` -> mendefinisikan header tabel

### Tipe Selector CSS
- Tag Selector, untuk menambahkan style pada sebuah tag. Penggunaanya cukup menuliskan tag yang ingin diberikan style, misalnya `div {`
- Class Selector, untuk menambahkan style pada elemen dengan class tertentu. Penggunaanya dengan menuliskan titik (`.`) diikuti dengan nama class, misalnya `.class1{`
- ID Selector, untuk menambahkan style pada elemen dengan ID tertentu. Penggunaanya dengan dengan menuliskan hashtag (`#`) diikuti dengan nama ID, misalnya `#id1 {`

### Implementasi Checklists
- Custom Login, Register, dan Create Task : 
Membuat suatu navbar yang berisikan status login, nama app, dan action button yang bersangkutan pada tiap-tiap halaman. Semua widget diletakan di dalam container agar lebih rapi. Pada halaman login, form dimasukan dalam sebuah flex yang memposisikan item di tengah. Memasukan control group dan control class pada tiap input form untuk memanfaatkan default layout dari bootstrap. Pada halaman register, memanfaatkan layout form default dari bootstrap dengan menginterasi setiap field pada form dan diintegrasi dengan control class dari bootstrap. Hal yang sama juga diterapkan pada Create Task.

- Implementasi halaman todolist :
Semua card task diletakan dalam suatu container. Setiap card berisi header yang merupakan status dari tugas. Body card diisi dengan judul dan deskripsi task. 2 button action di bagian kanan bawah untuk merubah status dan menghapus suatu task.

- Implementasi Responsiveness :
Menggunakan sistem grid dari Bootstrap. Menggunakan row dari bootstrap di luar iterasi tiap tas. Kemudian menambhakan card dengan col-lg-5 yang berarti pada checkpoint large, ubdah ukuran komlom menjadi 5/12 lebar container. Hal ini berlaku pada breakpoint large ke atas, yang tampilannya pada breakpoint large kebawah hanyasatu card per row, sedangkan pada breakpoint large keatas 2 card per row.

Checkpoint juga diterapkan pada form login yaitu col-sm-8 com-md-6 col-lg-3. Pada checkpoint small, lebar form adalah 8/12, pada checkpoint medium 6/12, dan pada checkpoint large 3/12. Hal ini mencegah ukuran form yang tidak proporsional. Hal yang sama juga diterapkan pada halaman register dan create-task.

- Implementasi Hover :
Implementasi Internal CSS dengan menggunakan selector class card. Animasi yang dilakukan adalah memperbesar ukuran card 5%.
