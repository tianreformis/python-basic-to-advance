# Tugas
## Instruction
1. pada file main.py yang ada kenali wajah pada gambar (image4.jpeg)
2. tanpa menghilangkan image3 
3. jadi ketika di run program akan mengenali image3 dan image4 langsung

 #penjelasan:
    #- menggunakan library opencv yang berisi fungsi deteksi wajah dan mata
    #- membaca gambar
    #- melakukan deteksi wajah menggunakan fungsi detectMultiScale
    #- melakukan deteksi mata menggunakan fungsi detectMultiScale
    #- menggambar kotak deteksi wajah pada citra
    #- menggambar kotak deteksi mata pada citra
    #- menggambar kotak deteksi mata dan wajah pada citra
    #- menunggu tombol ditekan
    #- menutup semua jendela jika tombol ESC (kode 27) ditekan
    #- penjelasan:
    #- library opencv berfungsi untuk mengolah citra
    #- fungsi CascadeClassifier digunakan untuk melakukan deteksi wajah dan mata
    #- fungsi detectMultiScale digunakan untuk melakukan deteksi objek yang terdapat pada citra
    #- fungsi rectangle digunakan untuk membuat kotak deteksi pada citra
    #- fungsi waitKey digunakan untuk menunggu input keyboard
    #- fungsi destroyAllWindows digunakan untuk menutup semua jendela
    