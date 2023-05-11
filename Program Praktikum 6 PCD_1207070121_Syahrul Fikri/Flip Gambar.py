#FIle : Flip Gambar
#Authors : Syahrul Fikri
#NIM : 1207070121
#Kelas : Pengolahan Citra Digital-C
#Teknik Elektro Fakultas Sains dan Teknologi UIN Sunan Gunung Djati Bandung

#Import Depencency
import numpy as np #Pada bagian ini menambahkan library untuk menjalankan program yaitu numpy dengan inisialisasi np yang mendukung scientific computing dalam hal ini digunakan untuk membentuk objek dari dimensi array yang diinginkan
import cv2 #Pada bagian ini saya merubah library dari modul karena untuk menjalankan library imageio pada perangkat ada kesalahan dalam pembacaan sehingga hasil tidak dapat ditampilkan walaupun telah diubah baik ke v3.iio dan imageio.v2 as imageio, namun fungsi cv2 ini juga dapat digunakan untuk membaca data gambar dari file yang dipanggil
import matplotlib.pyplot as plt #Pada bagian ini library matplotplib digunakan untuk melakukan visualisasi pada objek gambar 
#Dengan menambahkan berbagai library pada program akan memudahkan proses dalam menghasilkan suatu modifikasi pada hasil tampilan yang diinginkan

#Membaca Gambar
img = cv2.imread('Dragon.jpeg') #Inisialisasi objek agar dapat dipanggil pada program selanjutnya yaitu menjadi "img" objek tersebut dibaca dengan menggunakan fungsi library cv2 dan menyebutkan nama file yang telah disimpan pada lokasi yang sama dengan program
#Program diatas adalah bagian untuk membaca suatu file gambar yang akan diproses jika file tidak dipanggil dan dibaca maka tidak akan menghasilkan proses apapun

#Mendapatkan resolusi dan type dari gambar
img_height = img.shape[0] #ukuran pixel/resolusi tinggi dari gambar dihitung oleh fungsi shape dengan array urutan 0/awal
img_width = img.shape[1] #ukuran pixel/resolusi lebar dari gambar dihitung oleh fungsi shape dengan array urutan 1/kedua/selanjutnya
img_channel = img.shape[2] #ukuran pixel/resolusi kanal dari gambar dihitung oleh fungsi shape dengan array urutan 2/ketiga/selanjutnya
img_type = img.dtype #jenis type dari gambar yang dipanggil akan ditampilkan oleh fungsi dtype
#Bagian program diatas merupakan berbagai fungsi untuk mendapatkan ukuran nilai atau resolusi dari bagian gambar dan jenis tipe data file dengan menggunakan inisialisasi untuk memudahkan pembacaan

#Membuat variabel dengan resolusi dan tipe yang sama seperti gambar
img_flip_horizontal = np.zeros(img.shape, img_type) #menginisialisasi variabel pada gambar yang akan diubah dengan inisialisasi "img_flip_horizontal" untuk hasil gambar horizontal dengan format semua elemen gambar diinisialisasi ke 0 karena penggunaan np.zeros selanjutnya akan diukur resolusi dengan fungsi img.shape dan dibaca type filenya dengan fungsi img_type dari hasil inisialisasi sebelumya
img_flip_vertical = np.zeros(img.shape, img_type) #menginisialisasi variabel pada gambar yang akan diubah dengan inisialisasi "img_flip_vertical" untuk hasil gambar vertical dengan format semua elemen gambar diinisialisasi ke 0  karena penggunaan np.zeros selanjutnya akan diukur resolusi dengan fungsi img.shape dan dibaca type filenya dengan fungsi img_type dari hasil inisialisasi sebelumya
#Pada bagian program diatas merupakan inisialisasi isi dari variabel yang akan dibaca dari hasil modifikasi file

#Membalik gambar secara horizontal
for y in range(0, img_height): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen y dengan argumen range yang berisikan nilai yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 untuk nilai tinggi
    for x in range(0, img_width): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 untuk nilai lebar
        for c in range(0, img_channel): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen c dengan argumen range yang berisikan nilai yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 untuk nilai channel
            img_flip_horizontal[y][x][c] = img[y][img_width-1-x][c] #dengan menggunakan fungsi ini akan dikalkulasi semua nilai elemen pada gambar tersebut untuk menampilkan tampilan berupa horizontal dengan rumus tersebut

#Membalik gambar secara vertical
for y in range(0, img_height): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen y dengan argumen range yang berisikan nilai yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 untuk nilai tinggi
    for x in range(0, img_width):#penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 untuk nilai lebar
        for c in range(0, img_channel):#penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen c dengan argumen range yang berisikan nilai yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 untuk nilai channel
            img_flip_vertical[y][x][c] = img[img_height-1-y][x][c] #dengan menggunakan fungsi ini akan dikalkulasi semua nilai elemen pada gambar tersebut untuk menampilkan tampilan berupa vertical dengan rumus tersebut
#Untuk mendapatkan hasil modifikasi dalam hal ini memodifikasi posisi gambar dalam bentuk horizontal dan vertikal setiap nilai variabel disebutkan dan disiapkan rumus untuk melakukan kalkulasi terhadap nilai elemennya sehingga akan menghasilkan modifikasi yang dimaksud

#Menampilkan hasil balik gambar
plt.imshow(img_flip_horizontal) #menggunakan library matplotlib untuk memanggil hasil modifikasi yaitu untuk gambar dengan tampilan horizontal
plt.title("Flip Horizontal") #menggunakan library matplotlib untuk memberikan nama pada hasil tampilan gambar yang dipanggil yaitu Flip Horizontal
plt.show() #menggunakan library matplotlib untuk memvisualisasikan hasil modifikasi tampilan yang dipanggil sebelumnya dengan fungsi imshow
plt.imshow(img_flip_vertical) #menggunakan library matplotlib untuk memanggil hasil modifikasi yaitu untuk gambar dengan tampilan vertical
plt.title("Flip Vertical") #menggunakan library matplotlib untuk memberikan nama pada hasil tampilan gambar yang dipanggil yaitu Flip Vertical
plt.show() #menggunakan library matplotlib untuk memvisualisasikan hasil modifikasi tampilan yang dipanggil sebelumnya dengan fungsi imshow
#Setiap hasil modifikasi harus menggunakan program diatas untuk dapat memvisualisasikan hasilnya jika tidak maka proses tetap dapat dijalankan akan tetapi tidak akan memunculkan visualisasi hasil dari proses tersebut