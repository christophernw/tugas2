# Tugas 6 PBP

## Identitas
Nama    : Christopher Nathanael Wijaya<br>
NPM     : 2106630044<br>
Kelas   : E

## Link Hasil Deploy
Link untuk menuju ke web yang sudah di-deploy dapat diklik di [sini](https://tugas2christophernw.herokuapp.com/todolist/login/).

## Jawaban Pertanyaan
### Perbedaan Asynchronous Programming dan Synchronous Programming
Synchronous Programming menjalankan code secara berurutan, baris per baris. Ketika terjadi pemanggilan sebuah function, function tersebut harus diselesaikan terlebih dahulu sebelum melanjutkan ke baris code berikutnya. Pada synchronous programming, task-task yang ada harus dijalankan secara urut.

Asynchronous Programming tidak perlu menunggu baris code sebelumnya selesai. Ketika terjadi pemanggilan sebuah function asynchronous, baris code selanjutnya dapat dijalankan tanpa perlu menunggu function tersebut selesai. Dengan asynchronous programming, beberapa task dapat dijalankan secara bersamaan.

### Event-Driven Programming
Event-driven programming adalah suatu paradigma di mana alur yang dijalankan suatu program didasarkan atas event atau perilaku yang dilakukan antar user dan client. Sehingga, di terjadi pengiriman "pesan" yaitu event yang ingin diproses, lalu program akan memanggil perintah-perintah berdasarkan event yang didapat.

Pada Tugas 6, ini dilakukan dengan onReady document untuk inisialisasi, onClick untuk button form baru, serta onSuccess yang dipanggil setelah pemanggilan AJAX berhasil.

### Penerapan Async pada AJAX
Penerapan asyncronous programming pada AJAX terdapat pada fakta bahwa browser tidak perlu meng-suspend segala operasi yang dilakukan selama request AJAX berlangsung. Browser akan terus berjalan seperti biasa, bahkan dapat melaksanakan perintah lainnya di mana request tersebut berjalan di latar belakang. Oleh karena itu, AJAX dapat digunakan untuk mengubah tampilan website berdasarkan hasil tanpa memerlukan reload.

Tidak hanya itu, AJAX juga menggunakan paradigma Event-Driven Programming, di mana setelah AJAX dilakukan, dapat memanggil fungsi yang diberikan pada onSuccess dan memberi data hasil ke fungsi tersebut.

### Implementasi Checklists
- Membuat fungsi `show_todolist_json` pada `views.py` pada app todolist yang mengembalikan data JSON.
- Membuat routing pada `todolist/json` pada `urls.py` pada app todolist yang mengarah pada fungsi `show_todolist_json` di `views.py`.
- Menggunakan AJAX `getJSON` utnuk mengambil data JSON dari server.
- Iterasi tiap objek pada JSON dan ditampilkan pada card yang bersangkutan.
- Menambahkan atribut `onclick` pada tombol add task di navigation untuk menampilkan modal Boostrap.
- Membuat fungsi `add_task_ajax` pada `views.py` untuk menyimpan data dalam JSON sebagai objek baru pada database.
- Menambahkan routing `/todolist/add` pada `urls.py` di app todolist. yang mengarah pada `add_task_ajax` pada `views.py`.
- Menggunakan AJAX untuk override function submit pada html. AJAX akan mengumpulkan data-data yang ada pada form dan mengemasnya dalam sebuah JSON untuk dikirim melalui POST request ke url `todolist/add`. Setelah form di submit, modal akan ditutup dan data dimuat kembali dari server.