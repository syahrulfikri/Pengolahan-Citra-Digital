#File : Brightness, Contrass, dan Autolevel contrass
#Authors : Syahrul Fikri
#NIM : 1207070121
#Kelas : Pengolahan Citra Digital-C
#Teknik Elektro Fakultas Sains dan Teknologi UIN Sunan Gunung Djati Bandung

#import library
import numpy as np #Pada bagian ini menambahkan library untuk menjalankan program yaitu numpy dengan inisialisasi np yang mendukung scientific computing dalam hal ini digunakan untuk membentuk objek dari dimensi array yang diinginkan
import cv2 #Pada bagian ini saya merubah library dari modul karena untuk menjalankan library imageio pada perangkat ada kesalahan dalam pembacaan sehingga hasil tidak dapat ditampilkan walaupun telah diubah baik ke v3.iio dan imageio.v2 as imageio, namun fungsi cv2 ini juga dapat digunakan untuk membaca data gambar dari file yang dipanggil
import matplotlib.pyplot as plt #Pada bagian ini library matplotplib digunakan untuk melakukan visualisasi pada objek gambar 
#Dengan menambahkan berbagai library pada program akan memudahkan proses dalam menghasilkan suatu modifikasi pada hasil tampilan yang diinginkan

#load gambar
img = cv2.imread ("Japan View.jpg")  #Inisialisasi objek agar dapat dipanggil pada program selanjutnya yaitu menjadi "img" objek tersebut dibaca dengan menggunakan fungsi library cv2 dan menyebutkan nama file yang telah disimpan pada lokasi yang sama dengan program
#Program diatas adalah bagian untuk membaca suatu file gambar yang akan diproses jika file tidak dipanggil dan dibaca maka tidak akan menghasilkan proses apapun

#mendapatkan/define resolusi dan tipe gambar
img_height = img.shape[0] #ukuran pixel/resolusi tinggi dari gambar dihitung oleh fungsi shape dengan array urutan 0/awal
img_width = img.shape[1] #ukuran pixel/resolusi lebar dari gambar dihitung oleh fungsi shape dengan array urutan 1/kedua/selanjutnya
img_channel = img.shape[2] #ukuran pixel/resolusi kanal dari gambar dihitung oleh fungsi shape dengan array urutan 2/ketiga/selanjutnya
img_type = img.dtype #jenis type dari gambar yang dipanggil akan ditampilkan oleh fungsi dtype
#Bagian program diatas merupakan berbagai fungsi untuk mendapatkan ukuran nilai atau resolusi dari bagian gambar dan jenis tipe data file dengan menggunakan inisialisasi untuk memudahkan pembacaan

#percobaan pertama kita buat brightness untuk gambar grayscale
#membuat variabel img_brightness untuk menampung
img_brightness = np.zeros(img.shape, dtype = np.uint8) #menginisialisasi variabel pada gambar yang akan diubah dengan inisialisasi "img_brightness" untuk hasil gambar modifikasi kecerahannya dengan format semua elemen gambar diinisialisasi ke 0 karena penggunaan np.zeros selanjutnya akan diukur resolusi dengan fungsi img.shape dan tipe file ditetapkan yaitu uint8

#membuat fungsi penambahan brightness dengan nilai yang menjadi parameter
def brighter(nilai): #mendefinisikan fungsi baru yaitu dengan menambahkan def untuk fungsi brighter dengan variabel "nilai"
    for y in range(0, img_height):#penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen y dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai tinggi pada file gambar
        for x in range(0, img_width): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai lebar pada file gambar
            red = img[y][x][0] #melakukan inisialisasi terhadap isi variabel untuk elemen red untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 0/pertama
            green = img[y][x][1] #melakukan inisialisasi terhadap isi variabel untuk elemen green untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 1/kedua/selanjutnya
            blue = img[y][x][2] #melakukan inisialisasi terhadap isi variabel untuk elemen blue untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 2/ketiga/selanjutnya
            gray = (int(red) + int(green) + int(blue)) / 3 #untuk mendapatkan hasil berupa grayscale nilai setiap variabel RGB di kalkulasi dalam rumus tersebut
            gray += nilai #mengisi variabel "gray" dengan nilai lebih dari sama dengan variabel "nilai"
            if gray > 255: #menentukan nilai ambang batas atas
                gray = 255 #mengisi nilai menjadi 255 atau putih
            if gray < 0: #menentukan nilai ambang batas bawah
                gray = 0 #mengisi nilai menjadi 0 atau hitam
            img_brightness[y][x] = (gray,gray,gray) #hasil tampilan pada setiap elemen RGB pada sumbu y dan sumbu x gambar modifikasi kecerahan akan menampilkan hasil gray

#menampilkan gambar dengan parameter -100 dan 100
brighter(-100) #hasil modifikasi brightness pada gambar di set pada nilai -100
plt.imshow(img_brightness) #menggunakan library matplotlib untuk memanggil hasil modifikasi yaitu untuk gambar modifikasi brightness
plt.title("Brightness -100") #menggunakan library matplotlib untuk memberikan nama pada hasil tampilan gambar yang dipanggil yaitu Brightness -100 sesuai dengan set point yang diberikan
plt.show() #menggunakan library matplotlib untuk memvisualisasikan hasil modifikasi tampilan yang dipanggil sebelumnya dengan fungsi imshow

brighter (100) #hasil modifikasi brightness pada gambar di set pada nilai 100
plt.imshow(img_brightness) #menggunakan library matplotlib untuk memanggil hasil modifikasi yaitu untuk gambar modifikasi brightness
plt.title("Brightness 100") #menggunakan library matplotlib untuk memberikan nama pada hasil tampilan gambar yang dipanggil yaitu Brightness 100 sesuai dengan set point yang diberikan
plt.show() #menggunakan library matplotlib untuk memvisualisasikan hasil modifikasi tampilan yang dipanggil sebelumnya dengan fungsi imshow

#brightness RGB
img_rgbbrightness = np.zeros(img.shape, dtype = np.uint8) #menginisialisasi variabel pada gambar yang akan diubah dengan inisialisasi "img_rgbbrightness" untuk hasil gambar RGB yang dimodifikasi kecerahannya dengan format semua elemen gambar diinisialisasi ke 0 karena penggunaan np.zeros selanjutnya akan diukur resolusi dengan fungsi img.shape dan tipe file ditetapkan yaitu uint8

#fungsi untuk brightness RGB dengan nilai parameter
def rgbbrighter(nilai): #mendefinisikan fungsi baru yaitu dengan menambahkan def untuk fungsi rgbbrighter dengan variabel "nilai"
    for y in range(0, img_height):#penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen y dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai tinggi pada file gambar
        for x in range(0, img_width): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai lebar pada file gambar
            red = img[y][x][0] #melakukan inisialisasi terhadap isi variabel untuk elemen red untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 0/pertama
            red += nilai #mengisi variabel "red" dengan nilai lebih dari sama dengan variabel "nilai"
            if red > 255:#menentukan nilai ambang batas atas
                red = 255 #mengisi nilai menjadi 255 atau putih
            if red < 0: #menentukan nilai ambang batas bawah
                red = 0 #mengisi nilai menjadi 0 atau hitam
            green = img[y][x][1] #melakukan inisialisasi terhadap isi variabel untuk elemen green untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 1/kedua/selanjutnya
            green += nilai #mengisi variabel "red" dengan nilai lebih dari sama dengan variabel "nilai"
            if green > 255:#menentukan nilai ambang batas atas
                green = 255 #mengisi nilai menjadi 255 atau putih
            if green < 0: #menentukan nilai ambang batas bawah
                green = 0 #mengisi nilai menjadi 0 atau hitam
            blue = img[y][x][2] #melakukan inisialisasi terhadap isi variabel untuk elemen blue untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 2/ketiga/selanjutnya
            blue += nilai #mengisi variabel "blue" dengan nilai lebih dari sama dengan variabel "nilai"
            if blue > 255:#menentukan nilai ambang batas atas
                blue = 255 #mengisi nilai menjadi 255 atau putih
            if blue < 0: #menentukan nilai ambang batas bawah
                blue = 0 #mengisi nilai menjadi 0 atau hitam
            img_rgbbrightness[y][x] = (red,green,blue) #hasil tampilan pada setiap elemen RGB akan menampilkan hasil dalam dimensi red, green, blue

#Menampilkan hasil dengan nilai brightness -100 dan 100
rgbbrighter(-100) #hasil modifikasi rgbbrightness pada gambar di set pada nilai -100
plt.imshow(img_rgbbrightness) #menggunakan library matplotlib untuk memanggil hasil modifikasi yaitu untuk gambar modifikasi rgb brightness
plt.title("Brightness -100") #menggunakan library matplotlib untuk memberikan nama pada hasil tampilan gambar yang dipanggil yaitu Brightness -100 sesuai dengan set point yang diberikan
plt.show() #menggunakan library matplotlib untuk memvisualisasikan hasil modifikasi tampilan yang dipanggil sebelumnya dengan fungsi imshow

rgbbrighter(100) #hasil modifikasi rgbbrightness pada gambar di set pada nilai 100
plt.imshow(img_rgbbrightness) #menggunakan library matplotlib untuk memanggil hasil modifikasi yaitu untuk gambar modifikasi rgb brightness
plt.title("Brightness 100") #menggunakan library matplotlib untuk memberikan nama pada hasil tampilan gambar yang dipanggil yaitu Brightness 100 sesuai dengan set point yang diberikan
plt.show() #menggunakan library matplotlib untuk memvisualisasikan hasil modifikasi tampilan yang dipanggil sebelumnya dengan fungsi imshow

#Contrass
img_contrass = np.zeros (img.shape, dtype = np.uint8) #menginisialisasi variabel pada gambar yang akan diubah dengan inisialisasi "img_contrass" untuk hasil gambar grayscale yang dimodifikasi tingkat kontrassnya dengan format semua elemen gambar diinisialisasi ke 0 karena penggunaan np.zeros selanjutnya akan diukur resolusi dengan fungsi img.shape dan tipe file ditetapkan yaitu uint8

def contrass(nilai): #mendefinisikan fungsi baru yaitu dengan menambahkan def untuk fungsi contrass dengan variabel "nilai"
    for y in range(0, img_height):#penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen y dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai tinggi pada file gambar
        for x in range(0, img_width): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai lebar pada file gambar
            red = img[y][x][0] #melakukan inisialisasi terhadap isi variabel untuk elemen red untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 0/pertama
            green = img[y][x][1] #melakukan inisialisasi terhadap isi variabel untuk elemen green untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 1/kedua/selanjutnya
            blue = img[y][x][2] #melakukan inisialisasi terhadap isi variabel untuk elemen blue untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 2/ketiga/selanjutnya
            gray = (int(red) + int(green) + int(blue)) / 3 #untuk mendapatkan hasil berupa grayscale nilai setiap variabel RGB di kalkulasi dalam rumus tersebut
            gray += nilai #mengisi variabel "gray" dengan nilai lebih dari sama dengan variabel "nilai"
            if gray > 255: #menentukan nilai ambang batas atas
                gray = 255 #mengisi nilai menjadi 255 atau putih
            img_contrass[y][x] = (gray,gray,gray)  #hasil tampilan pada setiap elemen RGB pada sumbu y dan sumbu x gambar modifikasi contrass akan menampilkan hasil gray

#menampilkan gambar dengan nilai contrass 2 dan 10
contrass(2) #hasil modifikasi contrass pada gambar diberikan setpoint 2
plt.imshow(img_contrass) #menggunakan library matplotlib untuk memanggil hasil modifikasi yaitu untuk gambar modifikasi nilai contrass gambar grayscale
plt.title("Contrass 2") #menggunakan library matplotlib untuk memberikan nama pada hasil tampilan gambar yang dipanggil yaitu Contrass 2 sesuai dengan set point yang diberikan
plt.show() #menggunakan library matplotlib untuk memberikan nama pada hasil tampilan gambar yang dipanggil yaitu Brightness -100 sesuai dengan set point yang diberikan

contrass(10) #hasil modifikasi contrass pada gambar diberikan setpoint 10
plt.imshow(img_contrass) #menggunakan library matplotlib untuk memanggil hasil modifikasi yaitu untuk gambar modifikasi nilai contrass gambar grayscale
plt.title("Contrass 10") #menggunakan library matplotlib untuk memberikan nama pada hasil tampilan gambar yang dipanggil yaitu Contrass 10 sesuai dengan set point yang diberikan
plt.show() #menggunakan library matplotlib untuk memvisualisasikan hasil modifikasi tampilan yang dipanggil sebelumnya dengan fungsi imshow

#Contrass RGB
img_rgbcontrass = np.zeros(img.shape, dtype = np.uint8) #menginisialisasi variabel pada gambar yang akan diubah dengan inisialisasi "img_rgbcontrass" untuk hasil gambar RGB yang dimodifikasi tingkat kontrassnya dengan format semua elemen gambar diinisialisasi ke 0 karena penggunaan np.zeros selanjutnya akan diukur resolusi dengan fungsi img.shape dan tipe file ditetapkan yaitu uint8

#fungsi untuk Contrass RGB dengan nilai parameter
def contrassrgb(nilai): #mendefinisikan fungsi baru yaitu dengan menambahkan def untuk fungsi rgbbrighter dengan variabel "nilai"
    for y in range(0, img_height):#penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen y dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai tinggi pada file gambar
        for x in range(0, img_width): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai lebar pada file gambar
            red = img[y][x][0] #melakukan inisialisasi terhadap isi variabel untuk elemen red untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 0/pertama
            red += nilai #mengisi variabel "red" dengan nilai lebih dari sama dengan variabel "nilai"
            if red > 255:#menentukan nilai ambang batas atas
                red = 255 #mengisi nilai menjadi 255 atau putih
            green = img[y][x][1] #melakukan inisialisasi terhadap isi variabel untuk elemen green untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 1/kedua/selanjutnya
            green += nilai #mengisi variabel "red" dengan nilai lebih dari sama dengan variabel "nilai"
            if green > 255:#menentukan nilai ambang batas atas
                green = 255 #mengisi nilai menjadi 255 atau putih
            blue = img[y][x][2] #melakukan inisialisasi terhadap isi variabel untuk elemen blue untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 2/ketiga/selanjutnya
            blue += nilai #mengisi variabel "blue" dengan nilai lebih dari sama dengan variabel "nilai"
            if blue > 255:#menentukan nilai ambang batas atas
                blue = 255 #mengisi nilai menjadi 255 atau putih
            img_rgbcontrass[y][x] = (red,green,blue) #hasil tampilan pada setiap elemen RGB akan menampilkan hasil dalam dimensi red, green, blue

#menampilkan gambar dengan parameter 20 dan 100
contrassrgb(20) #hasil modifikasi contrass pada gambar RGB diberikan setpoint 20
plt.imshow(img_rgbcontrass) #menggunakan library matplotlib untuk memanggil hasil modifikasi yaitu untuk gambar RGB dengan modifikasi nilai contrass
plt.title("Contrass 20") #menggunakan library matplotlib untuk memberikan nama pada hasil tampilan gambar RGB yang dipanggil yaitu Contrass 20 sesuai dengan set point yang diberikan
plt.show() #menggunakan library matplotlib untuk memvisualisasikan hasil modifikasi tampilan yang dipanggil sebelumnya dengan fungsi imshow

contrassrgb(100) #hasil modifikasi contrass pada gambar RGB diberikan setpoint 100
plt.imshow(img_rgbcontrass) #menggunakan library matplotlib untuk memanggil hasil modifikasi yaitu untuk gambar RGB dengan modifikasi nilai contrass
plt.title("Contrass 100") #menggunakan library matplotlib untuk memberikan nama pada hasil tampilan gambar RGB yang dipanggil yaitu Contrass 100 sesuai dengan set point yang diberikan
plt.show() #menggunakan library matplotlib untuk memvisualisasikan hasil modifikasi tampilan yang dipanggil sebelumnya dengan fungsi imshow

#contrass autolevel
img_autocontrass = np.zeros (img.shape, dtype = np.uint8) #menginisialisasi variabel pada gambar yang akan diubah dengan inisialisasi "img_autocontrass" untuk hasil gambar grayscale yang dimodifikasi tingkat kontrassnya dengan format semua elemen gambar diinisialisasi ke 0 karena penggunaan np.zeros selanjutnya akan diukur resolusi dengan fungsi img.shape dan tipe file ditetapkan yaitu uint8

def autocontrass(): #mendefinisikan fungsi baru yaitu autocontrass untuk mendapatkan hasil kalkulasi otomatis dalam tampilan modifikasi contrass
    xmax = 200 #Menginisialisasi batas atas atau maksimum bins
    xmin = 0 #Menginisialisasi batas bawah atau maksimum bins
    d = 0 #Mendefinisikan nilai variabel untuk perhitungan dengan inisialisasi 0

    for y in range (0, img_height): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen y dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai tinggi pada file gambar
        for x in range(0, img_width): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai lebar pada file gambar
            red = img[y][x][0] #melakukan inisialisasi terhadap isi variabel untuk elemen red untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 0/pertama
            green = img[y][x][1] #melakukan inisialisasi terhadap isi variabel untuk elemen green untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 1/kedua/selanjutnya
            blue = img[y][x][2] #melakukan inisialisasi terhadap isi variabel untuk elemen blue untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 2/ketiga/selanjutnya
            gray = (int(red) + int(green) + int(blue)) / 3 #untuk mendapatkan hasil berupa grayscale nilai setiap variabel RGB di kalkulasi dalam rumus tersebut
            if gray < xmax: #Menentukan nilai batas atas
                xmax = gray #Mengisikan nilai elemen maksimal x dalam hasil nilai gray
            if gray > xmin : #Menentukan nilai batas bawah
                xmin = gray #Mengisikan nilai elemen minimum x dalam hasil nilai gray
    
    d = xmin -xmax #Menentukan rentang nilai untuk variabel d

    for y in range (0, img_height): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen y dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai tinggi pada file gambar
        for x in range(0, img_width): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai lebar pada file gambar
            red = img[y][x][0] #melakukan inisialisasi terhadap isi variabel untuk elemen red untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 0/pertama
            green = img[y][x][1] #melakukan inisialisasi terhadap isi variabel untuk elemen green untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 1/kedua/selanjutnya
            blue = img[y][x][2] #melakukan inisialisasi terhadap isi variabel untuk elemen blue untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 2/ketiga/selanjutnya
            gray = (int(red) + int(green) + int(blue)) / 3 #untuk mendapatkan hasil berupa grayscale nilai setiap variabel RGB di kalkulasi dalam rumus tersebut
            gray = int(float(255/d)*(gray-xmax)) #untuk mendapatkan hasil gambar grayscale contrass secara otomatis menggunakan referensi rumus berikut menggunakan variabel yang telah didefinisikan 
            img_autocontrass[y][x]=(gray,gray,gray) #hasil tampilan pada setiap elemen RGB pada sumbu y dan sumbu x gambar modifikasi contrass akan menampilkan hasil gray

autocontrass() #Pemanggilan penghitungan fungsi autocontrass dengan nilai set point sesuai dengan hasil perhitungan yang didapatkan
plt.imshow(img_autocontrass) #menggunakan library matplotlib untuk memanggil hasil modifikasi yaitu untuk gambar grayscale dengan modifikasi nilai contrass
plt.title("contrass autolevel") #menggunakan library matplotlib untuk memberikan nama pada hasil tampilan gambar grayscale yang dipanggil yaitu Contrass autolevel
plt.show() #menggunakan library matplotlib untuk memvisualisasikan hasil modifikasi tampilan yang dipanggil sebelumnya dengan fungsi imshow