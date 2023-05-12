#File : Brightness, Contrass, dan Autolevel contrass
#Authors : Syahrul Fikri
#NIM : 1207070121
#Kelas : Pengolahan Citra Digital-C
#Teknik Elektro Fakultas Sains dan Teknologi UIN Sunan Gunung Djati Bandung

#import library
import matplotlib.pyplot as plt #Pada bagian ini library matplotplib digunakan untuk melakukan visualisasi pada objek gambar 

from skimage import data #Menggunakan library skimage untuk memanggil data gambar yang sudah disiapkan pada library
from skimage.io import imread #Menggunakan library skimage untuk membaca data gambar yang dipanggil
from skimage.color import rgb2gray #Menggunakan library skimage untuk melakukan konversi gambar RGB menjadi gambar Grayscale
from skimage.util import invert #Menggunakan library skimage untuk melakukan inversi gambar menjadi citra negatif
import numpy as np #Pada bagian ini menambahkan library untuk menjalankan program yaitu numpy dengan inisialisasi np yang mendukung scientific computing dalam hal ini digunakan untuk membentuk objek dari dimensi array yang diinginkan

#percobaan 1 : crop image
Book = plt.imread("Book.jpg") #Mendefinisikan variabel "Book" sebagai fungsi untuk membaca path file gambar dengan menggunakan library matplotlib
astronautImage = data.astronaut() #mengdefinisikan variabel "astrounautImage" untuk memanggil data gambar pada library yaitu astronaut
cameraImage = data.camera() #mengdefinisikan variabel "cameraImage" untuk memanggil data gambar pada library yaitu camera
astroCropped = astronautImage.copy() #mendefinisikan variabel "astroCropped" untuk menyalin data gambar astronaut yang telah terpanggil untuk dilakukan cropping
astroCropped = astroCropped[0:256,64:320] #mendefinisikan variabel "astroCropped" untuk mendefinisikan panjang array dimulai dari 0 hingga 256 dan posisi gambar pada array ke 64 hingga array 320
cameraCropped = cameraImage.copy() #mendefinisikan variabel "cameraCropped" untuk menyalin data gambar camera yang telah terpanggil untuk dilakukan cropping
cameraCropped = cameraCropped[0:256,64:320] #mendefinisikan variabel "cameraCropped" untuk mendefinisikan panjang array dimulai dari 0 hingga 256 dan posisi gambar pada array ke 64 hingga array 320
BookCropped = Book.copy() #mendefinisikan variabel "BookCropped" untuk menyalin data gambar Book yang telah terpanggil untuk dilakukan cropping
BookCropped = BookCropped[0:256,64:320] #mendefinisikan variabel "BookCropped" untuk mendefinisikan panjang array dimulai dari 0 hingga 256 dan posisi gambar pada array ke 64 hingga array 320

print('Astro Ori Shape : ',astronautImage.shape) #Nilai resolusi pada gambar astronaut akan ditampilkan pada pembacaan terminal
print('Astro Crop Shape : ',astroCropped.shape) #Nilai resolusi pada gambar astronaut setelah di cropping akan ditampilkan pada pembacaan terminal

print('Camera Ori Shape : ',cameraImage.shape) #Nilai resolusi pada gambar camera akan ditampilkan pada pembacaan terminal
print('Camera Crop Shape : ',cameraCropped.shape) #Nilai resolusi pada gambar camera setelah di cropping akan ditampilkan pada pembacaan terminal

print('Book Ori Shape : ',Book.shape) #Nilai resolusi pada gambar buku akan ditampilkan pada pembacaan terminal
print('Book Crop Shape : ',BookCropped.shape) #Nilai resolusi pada gambar buku setelah di cropping akan ditampilkan pada pembacaan terminal

fig,axes = plt.subplots(2,2, figsize=(12,12)) #Dengan menggunakan fungsi figure axes maka ukuran tampilan dapat dimodifikasi seperti tampilan berjumlah 2 disisi kiri dan 2 disisi kanan kemudian ukuran bingkai 12x12
ax = axes.ravel() #Menggunakan fungsi ravel pada library numpy untuk mengkonversi array pada axes menjadi flat array dengan inisialisasi variabel ax

ax[0].imshow(astronautImage) #pada tampilan figure gambar astronaut original akan ditempatkan pada array 0
ax[0].set_title("Citra Input 1") #tampilan pada masing-masing gambar yaitu gambar astronaut original akan diberikan judul yaitu Citra Input 1
ax[1].imshow(cameraImage, cmap='gray') #pada tampilan figure gambar camera original akan ditempatkan pada array 1 dengan format gambar grayscale
ax[1].set_title("Citra Input 2") #tampilan pada masing-masing gambar yaitu gambar camera original akan diberikan judul yaitu Citra Input 2
ax[2].imshow(astroCropped) #pada tampilan figure gambar astronaut cropping  akan ditempatkan pada array 2
ax[2].set_title("Citra Output 1") #tampilan pada masing-masing gambar yaitu gambar astronaut cropping akan diberikan judul yaitu Citra Output 1
ax[3].imshow(cameraCropped, cmap='gray') #pada tampilan figure gambar camera cropping akan ditempatkan pada array 3 dengan format gambar grayscale
ax[3].set_title("Citra Output 2") #tampilan pada masing-masing gambar yaitu gambar camera cropping akan diberikan judul yaitu Citra Output 2

#percobaan 2 : citra negative

inv = invert(astroCropped) #Mendefinisikan variabel untuk inversi "inv" yang berisikan nilai dari gambar Astronaut yang telah dicropping
print('Shape Input : ', astroCropped.shape) #Pembacaan nilai resolusi dari gambar Astronaut hasil cropping akan ditampilkan sebagai input awalnya
print('Shape Output : ',inv.shape) #Pembacaan nilai resolusi dari gambar Astronaut hasil cropping yang telah diinversi akan ditampilkan sebagai outputnya

fig, axes = plt.subplots(2, 2, figsize=(12, 12)) #Dengan menggunakan fungsi figure axes maka ukuran tampilan dapat dimodifikasi seperti tampilan berjumlah 2 disisi kiri dan 2 disisi kanan kemudian ukuran bingkai 12x12
ax = axes.ravel() #Menggunakan fungsi ravel pada library numpy untuk mengkonversi array pada axes menjadi flat array dengan inisialisasi variabel ax

ax[0].imshow(astroCropped) #pada tampilan figure gambar astronaut croppping akan ditempatkan pada array 0
ax[0].set_title("Citra Input") #tampilan pada masing-masing gambar yaitu gambar astronaut original akan diberikan judul yaitu Citra Input 1

ax[1].hist(astroCropped.ravel(), bins=256) #pada tampilan figure akan menampilkan histogram astronaut croppping akan ditempatkan pada array 1 dengan jumlah bins 256 dengan tipe flat array dengan fungsi ravel
ax[1].set_title('Histogram Input') #tampilan pada histogram yaitu gambar astronaut cropping akan diberikan judul yaitu Histogram Input 1

ax[2].imshow(inv) #pada tampilan figure gambar astronaut croppping yang telah diinversi akan ditempatkan pada array 2
ax[2].set_title('Citra Output (Inverted Image)') #tampilan pada histogram yaitu gambar astronaut cropping yang telah diinversi akan diberikan judul yaitu Citra Output (Inverted Image)

ax[3].hist(inv.ravel(), bins=256) #pada tampilan figure akan menampilkan histogram astronaut croppping yang telah diinversi akan ditempatkan pada array 3 dengan jumlah bins 256 dengan tipe flat array dengan fungsi ravel
ax[3].set_title('Histogram Output') #tampilan pada histogram yaitu gambar astronaut cropping yang telah diinversi akan diberikan judul yaitu Histogram Output 1

#Percobaan 3: Brightness Citra
copyCamera = cameraCropped.copy().astype(float) #menginisialisasi variabel baru untuk "copyCamera" dengan menyalin gambara camera yang telah di cropping dengan type data float
m1,n1 = copyCamera.shape #mengambil dimensi matriks untuk dapat dipanggil pada fungsi lainnnya dengan mendefinisikan resolusi dari salinan data gambar camera
output1 = np.empty([m1, n1]) #menginisialisasi variabel untuk output dengan menggunakan library numpy pada fungsi np.empty maka array akan dikosongkan dan sisesuaikan isinya dengan variabel lain yang dipanggil

for baris in range(0, m1-1): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen baris dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga variabel m1 yang dikurangi 1 pada file gambar
    for kolom in range(0, n1-1): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen kolom dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga variabel n1 yang dikurangi 1 pada file gambar
        a1 = baris #mendefinisikan variabel "a1" berisikan nilai sama dengan baris
        b1 = kolom #mendefinisikan variabel "b1" berisikan nilai sama dengan kolom
        output1[a1, b1] = copyCamera[baris, kolom] + 100 #hasil tampilan output yang ditampilkan dalam elemen a1 dan b1 berisikan variabel salinan data gambar camera dengan array baris dan kolom ditambah nilai 100
        
fig, axes = plt.subplots(2, 2, figsize=(12, 12)) #Dengan menggunakan fungsi figure axes maka ukuran tampilan dapat dimodifikasi seperti tampilan berjumlah 2 disisi kiri dan 2 disisi kanan kemudian ukuran bingkai 12x12
ax = axes.ravel() #Menggunakan fungsi ravel pada library numpy untuk mengkonversi array pada axes menjadi flat array dengan inisialisasi variabel ax

ax[0].imshow(cameraCropped, cmap='gray') #pada tampilan figure gambar camera cropping akan ditempatkan pada array 0 dengan format gambar grayscale
ax[0].set_title("Citra Input") #tampilan pada masing-masing gambar yaitu gambar camera cropping akan diberikan judul yaitu Citra Input pada array 0

ax[1].hist(cameraCropped.ravel(), bins=256) #pada tampilan figure akan menampilkan histogram camera croppping akan ditempatkan pada array 1 dengan jumlah bins 256 dengan tipe flat array dengan fungsi ravel
ax[1].set_title('Histogram Input') #tampilan pada masing-masing histogram gambar camera cropping akan diberikan judul yaitu Histogram Input pada array 1

ax[2].imshow(output1, cmap='gray') #pada tampilan figure gambar camera cropping setelah hasil modifikasi brightness akan ditempatkan pada array 2 dengan format gambar grayscale
ax[2].set_title('Citra Output (Brightnes)')#tampilan pada masing-masing gambar yaitu gambar modifikasi camera cropping akan diberikan judul yaitu Citra Output (Brightnes) pada array 2

ax[3].hist(output1.ravel(), bins=256) #pada tampilan figure akan menampilkan histogram modifikasi brightness camera croppping akan ditempatkan pada array 3 dengan jumlah bins 256 dengan tipe flat array dengan fungsi ravel
ax[3].set_title('Histogram Output') #tampilan pada masing-masing histogram gambar camera cropping akan diberikan judul yaitu Histogram Input pada array 3
plt.show() #menggunakan fungsi library matplotlib untuk menamplkan setiap tampilan yang dipanggil menggunakan fungsi imshow