#File : Inversi, Transformasi Logaritmik, Transformasi Powerlaw
#Authors : Syahrul Fikri
#NIM : 1207070121
#Kelas : Pengolahan Citra Digital-C
#Teknik Elektro Fakultas Sains dan Teknologi UIN Sunan Gunung Djati Bandung

#Import Library
import numpy as np #Pada bagian ini menambahkan library untuk menjalankan program yaitu numpy dengan inisialisasi np yang mendukung scientific computing dalam hal ini digunakan untuk membentuk objek dari dimensi array yang diinginkan
import cv2 #Pada bagian ini saya merubah library dari modul karena untuk menjalankan library imageio pada perangkat ada kesalahan dalam pembacaan sehingga hasil tidak dapat ditampilkan walaupun telah diubah baik ke v3.iio dan imageio.v2 as imageio, namun fungsi cv2 ini juga dapat digunakan untuk membaca data gambar dari file yang dipanggil
import matplotlib.pyplot as plt #Pada bagian ini library matplotplib digunakan untuk melakukan visualisasi pada objek gambar 
#Dengan menambahkan berbagai library pada program akan memudahkan proses dalam menghasilkan suatu modifikasi pada hasil tampilan yang diinginkan

#Membaca Gambar
img = cv2.imread("Dragon.jpeg") #Inisialisasi objek agar dapat dipanggil pada program selanjutnya yaitu menjadi "img" objek tersebut dibaca dengan menggunakan fungsi library cv2 dan menyebutkan nama file yang telah disimpan pada lokasi yang sama dengan program atau seperti yang digunakan saat ini yaitu menginput keseluruhan path gambar tersebut
#Program diatas adalah bagian untuk membaca suatu file gambar yang akan diproses jika file tidak dipanggil dan dibaca maka tidak akan menghasilkan proses apapun
img_height = img.shape[0] #ukuran pixel/resolusi tinggi dari gambar dihitung oleh fungsi shape dengan array urutan 0/awal
img_width = img.shape[1] #ukuran pixel/resolusi lebar dari gambar dihitung oleh fungsi shape dengan array urutan 1/kedua/selanjutnya
img_channel = img.shape[2] #ukuran pixel/resolusi kanal dari gambar dihitung oleh fungsi shape dengan array urutan 2/ketiga/selanjutnya
#Bagian program diatas merupakan berbagai fungsi untuk mendapatkan ukuran nilai atau resolusi dari bagian gambar

#INVERSI
#Operasi inversi ini dilakukan dengan mengurangkan nilai intensitas piksel dari nilai intensitas piksel maksimumnya menghasilkan tampilan citra negatif
#Membuat variabel img_inversi
img_inversi = np.zeros(img.shape, dtype=np.uint8) #menginisialisasi variabel pada gambar yang akan diubah dengan inisialisasi "img_inversi" untuk hasil gambar inversi dengan format semua elemen gambar diinisialisasi ke 0 karena penggunaan np.zeros selanjutnya akan diukur resolusi dengan fungsi img.shape dan tipe file ditetapkan yaitu uint8

#Membuat fungsi untuk inversi grayscale
def inversi_grayscale(nilai): #mendefinisikan fungsi baru yaitu dengan menambahkan def untuk fungsi inversi_grayscale dengan variabel "nilai"
    for y in range(0, img_height): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen y dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai tinggi pada file gambar
        for x in range(0, img_width): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai lebar pada file gambar
            red = img[y][x][0] #melakukan inisialisasi terhadap isi variabel untuk elemen red untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 0/pertama
            green = img[y][x][1] #melakukan inisialisasi terhadap isi variabel untuk elemen green untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 1/kedua/selanjutnya
            blue = img[y][x][2] #melakukan inisialisasi terhadap isi variabel untuk elemen blue untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 2/ketiga/selanjutnya
            gray = (int(red) + int(green) + int(blue)) / 3 #untuk mendapatkan hasil berupa grayscale nilai setiap variabel RGB di kalkulasi dalam rumus tersebut
            gray = nilai - gray #untuk mendapatkan nilai inversi grey dibuat fungsi lainnya pada rumus tersebut dengan mengurangi nilai yang dibaca dengan nilai grey dari rumus sebelumnya
            img_inversi[y][x] = (gray, gray, gray) #hasil tampilan pada setiap elemen RGB akan menampilkan hasil gray

#Membuat fungsi untuk inversi rgb
def inversi_rgb(nilai): #mendefinisikan fungsi baru yaitu dengan menambahkan def untuk fungsi inversi_rgb dengan variabel "nilai"
    for y in range(0, img_height): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen y dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai tinggi pada file gambar
        for x in range(0, img_width): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai lebar pada file gambar
            red = img[y][x][0] #melakukan inisialisasi terhadap isi variabel untuk elemen red untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 0/pertama
            red = nilai - red #untuk mendapatkan nilai inversi red dibuat fungsi lainnya pada rumus tersebut dengan mengurangi nilai yang dibaca dengan nilai red sebelumnya
            green = img[y][x][1] #melakukan inisialisasi terhadap isi variabel untuk elemen green untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 1/kedua/selanjutnya
            green = nilai - green #untuk mendapatkan nilai inversi gren dibuat fungsi lainnya pada rumus tersebut dengan mengurangi nilai yang dibaca dengan nilai green sebelumnya
            blue = img[y][x][2] #melakukan inisialisasi terhadap isi variabel untuk elemen blue untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 2/ketiga/selanjutnya
            blue = nilai - blue #untuk mendapatkan nilai inversi blue dibuat fungsi lainnya pada rumus tersebut dengan mengurangi nilai yang dibaca dengan nilai blue sebelumnya
            img_inversi[y][x] = (red, green, blue) #hasil tampilan pada setiap elemen RGB akan menampilkan hasil dalam dimensi red, green, blue

#Menampilkan hasil inversi
inversi_grayscale(255) #hasil inversi dalam citra grayscale akan ditampilkan dalam resolusi 255 pixel
plt.imshow(img_inversi) #menggunakan library matplotlib untuk memanggil hasil modifikasi yaitu untuk gambar inversi dalam citra grayscale
plt.title("Inversi Grayscale") #menggunakan library matplotlib untuk memberikan nama pada hasil tampilan gambar yang dipanggil yaitu Inversi Grayscale
plt.show() #menggunakan library matplotlib untuk memvisualisasikan hasil modifikasi tampilan yang dipanggil sebelumnya dengan fungsi imshow

inversi_rgb(255)
plt.imshow(img_inversi) #menggunakan library matplotlib untuk memanggil hasil modifikasi yaitu untuk gambar inversi dalam citra RGB
plt.title("Inversi RGB") #menggunakan library matplotlib untuk memberikan nama pada hasil tampilan gambar yang dipanggil yaitu Inversi RGB
plt.show() #menggunakan library matplotlib untuk memvisualisasikan hasil modifikasi tampilan yang dipanggil sebelumnya dengan fungsi imshow

#LOG
#Formula Logaritma akan menaikkan nilai-nilai keabuan piksel gelap pada citra selama proses kompresi menjadi nilai keabuan yang tinggi
#Membuat variabel img_log untuk menampung hasil
img_log = np.zeros(img.shape, dtype=np.uint8) #menginisialisasi variabel pada gambar yang akan diubah dengan inisialisasi "img_log" untuk hasil gambar transformasi logaritmik dengan format semua elemen gambar diinisialisasi ke 0 karena penggunaan np.zeros selanjutnya akan diukur resolusi dengan fungsi img.shape dan tipe file ditetapkan yaitu uint8

#Mendefinisikan fungsi untuk log
def log(c): #mendefinisikan fungsi baru yaitu dengan menambahkan def untuk fungsi log dengan variabel "c"
    for y in range(0, img_height):#penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen y dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai tinggi pada file gambar
        for x in range(0, img_width): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai lebar pada file gambar
            red = img[y][x][0] #melakukan inisialisasi terhadap isi variabel untuk elemen red untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 0/pertama
            green = img[y][x][1] #melakukan inisialisasi terhadap isi variabel untuk elemen green untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 1/kedua/selanjutnya
            blue = img[y][x][2] #melakukan inisialisasi terhadap isi variabel untuk elemen blue untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 2/ketiga/selanjutnya
            gray = (int(red) + int(green) + int(blue)) / 3 #untuk mendapatkan hasil berupa grayscale nilai setiap variabel RGB di kalkulasi dalam rumus tersebut
            gray = int(c * np.log(gray + 1)) #untuk mendapatkan hasil transformasi logaritmik maka nilai ditetapkan sebagai data integer dengan mengalikan kontanta c dengan logaritma bervariabel dari nilai gray ditambah satu
            if gray > 255: #menentukan nilai ambang batas atas
                gray = 255 #mengisi nilai menjadi 255 atau putih
            if gray < 0: #menentukan nilai ambang batas bawah
                gray = 0 #mengisi nilai menjadi 0 atau hitam
            img_log[y][x] = (gray, gray, gray) #hasil tampilan pada setiap elemen RGB gambar transformasi logaritmik akan menampilkan hasil gray

#Menampilkan hasil log
log(30) #hasil nilai transformasi logaritmik diberikan resolusi 30 pixel
plt.imshow(img_log) #menggunakan library matplotlib untuk memanggil hasil modifikasi yaitu untuk gambar transformasi logaritmik
plt.title("Log") #menggunakan library matplotlib untuk memberikan nama pada hasil tampilan gambar yang dipanggil yaitu Log
plt.show() #menggunakan library matplotlib untuk memvisualisasikan hasil modifikasi tampilan yang dipanggil sebelumnya dengan fungsi imshow


#INVERSI & LOG
#Formula Inverse logaritma akan memperluas nilai-nilai piksel tinggi pada citra selama proses kompresi menjadi nilai piksel yang lebih gelap
#Membuat variabel img_inlog untuk menampung hasil
img_inlog = np.zeros(img.shape, dtype=np.uint8) #menginisialisasi variabel pada gambar yang akan diubah dengan inisialisasi "img_inlog" untuk hasil gambar inversi dan transformasi logaritmik dengan format semua elemen gambar diinisialisasi ke 0 karena penggunaan np.zeros selanjutnya akan diukur resolusi dengan fungsi img.shape dan tipe file ditetapkan yaitu uint8

#Mendefinisikan fungsi untuk inversi log
def inlog(c): #mendefinisikan fungsi baru yaitu dengan menambahkan def untuk fungsi inversi log dengan variabel "c"
    for y in range(0, img_height):#penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen y dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai tinggi pada file gambar
        for x in range(0, img_width): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai lebar pada file gambar
            red = img[y][x][0] #melakukan inisialisasi terhadap isi variabel untuk elemen red untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 0/pertama
            green = img[y][x][1] #melakukan inisialisasi terhadap isi variabel untuk elemen green untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 1/kedua/selanjutnya
            blue = img[y][x][2] #melakukan inisialisasi terhadap isi variabel untuk elemen blue untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 2/ketiga/selanjutnya
            gray = (int(red) + int(green) + int(blue)) / 3 #untuk mendapatkan hasil berupa grayscale nilai setiap variabel RGB di kalkulasi dalam rumus tersebut
            gray = int(c * np.log(255 - gray + 1)) #untuk mendapatkan hasil transformasi logaritmik maka nilai ditetapkan sebagai data integer dengan mengalikan kontanta c dengan logaritma bervariabel dari nilai gray ditambah 1 dan mengurangi 255
            if gray > 255: #menentukan nilai ambang batas atas
                gray = 255 #mengisi nilai gray pada nilai 255 atau putih
            if gray < 0: #menentukan nilai ambang batas bawah
                gray = 0 #mengisi nilai gray pada nilai 0 atau hitam
            img_inlog[y][x] = (gray, gray, gray) #hasil tampilan pada setiap elemen RGB gambar inversi transformasi logaritmik akan menampilkan hasil gray

#Menampilkan hasil inversi log
inlog(30) #hasil nilai inversi transformasi logaritmik diberikan resolusi 30 pixel
plt.imshow(img_inlog) #menggunakan library matplotlib untuk memanggil hasil modifikasi yaitu untuk gambar inversi transformasi logaritmik
plt.title("Inversi & Log") #menggunakan library matplotlib untuk memberikan nama pada hasil tampilan gambar yang dipanggil yaitu Inversi & Log
plt.show() #menggunakan library matplotlib untuk memvisualisasikan hasil modifikasi tampilan yang dipanggil sebelumnya dengan fungsi imshow

#NTH POWER
#Formula Nth Powerlaw akan memetakan citra input dengan range nilai gelap yang sempit ke nilai output terang yang lebih lebar rangenya
#Membuat variabel img_nthpoer untuk menampung hasil
img_nthpower = np.zeros(img.shape, dtype=np.uint8) #menginisialisasi variabel pada gambar yang akan diubah dengan inisialisasi "img_nthpower" untuk hasil gambar power law dengan format semua elemen gambar diinisialisasi ke 0 karena penggunaan np.zeros selanjutnya akan diukur resolusi dengan fungsi img.shape dan tipe file ditetapkan yaitu uint8

#Mendefinisikan fungsi untuk nth power
def nthpower(c, y): #mendefinisikan fungsi baru yaitu dengan menambahkan def untuk fungsi nth powerlaw dengan variabel dimensi "c" dan dimensi "y"
    thc = c / 100 #mendefinisikan nilai keabuan pada dimensi c
    thy = y / 100 #mendefinisikan nilai keabuan pada dimensi y
    for y in range(0, img_height):#penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen y dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai tinggi pada file gambar
        for x in range(0, img_width): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai lebar pada file gambar
            red = img[y][x][0] #melakukan inisialisasi terhadap isi variabel untuk elemen red untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 0/pertama
            green = img[y][x][1] #melakukan inisialisasi terhadap isi variabel untuk elemen green untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 1/kedua/selanjutnya
            blue = img[y][x][2] #melakukan inisialisasi terhadap isi variabel untuk elemen blue untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 2/ketiga/selanjutnya
            gray = (int(red) + int(green) + int(blue)) / 3 #untuk mendapatkan hasil berupa grayscale nilai setiap variabel RGB di kalkulasi dalam rumus tersebut
            gray = int(thc * pow(gray, thy)) #untuk mendapatkan nthpower memanfaatkan variabel dalam bentuk integer pada nilai keabuan dimensi c dikalikan dengan powerlaw berisikan variabel nilai grey dan keabuan pada dimensi y
            if gray > 255: #menentukan nilai ambang batas atas
                gray = 255 #mengisi nilai gray pada nilai 255 atau putih
            if gray < 0: #menentukan nilai ambang batas bawah
                gray = 0 #mengisi nilai gray pada nilai 0 atau hitam
            img_nthpower[y][x] = (gray, gray, gray) #hasil tampilan pada setiap elemen RGB gambar nth powerlaw akan menampilkan hasil gray

#Menampilkan hasil
nthpower(50, 100) #hasil nilai nth powerlaw diberikan resolusi 50 hingga 100 pixel
plt.imshow(img_nthpower) #menggunakan library matplotlib untuk memanggil hasil modifikasi yaitu untuk gambar nth powerlaw
plt.title("Nth Power") #menggunakan library matplotlib untuk memberikan nama pada hasil tampilan gambar yang dipanggil yaitu Nth Power
plt.show() #menggunakan library matplotlib untuk memvisualisasikan hasil modifikasi tampilan yang dipanggil sebelumnya dengan fungsi imshow

#NTH ROOT POWER
#Formula Nth root power akan melakukan  pemetaan kurva pada citra input dengan range nilai terang yang lebih lebar menjadi range nilai yang lebih sempit
#Membuat variabel img_nthrootpower
img_nthrootpower = np.zeros(img.shape, dtype=np.uint8) #menginisialisasi variabel pada gambar yang akan diubah dengan inisialisasi "img_nthrootpower" untuk hasil gambar root power law dengan format semua elemen gambar diinisialisasi ke 0 karena penggunaan np.zeros selanjutnya akan diukur resolusi dengan fungsi img.shape dan tipe file ditetapkan yaitu uint8

#Membuat fungsi untuk nth root power
def nthrootpower(c, y):#mendefinisikan fungsi baru yaitu dengan menambahkan def untuk fungsi nth powerlaw dengan variabel dimensi "c" dan dimensi "y"
    thc = c / 100 #mendefinisikan nilai keabuan pada dimensi c
    thy = y / 100 #mendefinisikan nilai keabuan pada dimensi y
    for y in range(0, img_height):#penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen y dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai tinggi pada file gambar
        for x in range(0, img_width): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai lebar pada file gambar
            red = img[y][x][0] #melakukan inisialisasi terhadap isi variabel untuk elemen red untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 0/pertama
            green = img[y][x][1] #melakukan inisialisasi terhadap isi variabel untuk elemen green untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 1/kedua/selanjutnya
            blue = img[y][x][2] #melakukan inisialisasi terhadap isi variabel untuk elemen blue untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 2/ketiga/selanjutnya
            gray = (int(red) + int(green) + int(blue)) / 3 #untuk mendapatkan hasil berupa grayscale nilai setiap variabel RGB di kalkulasi dalam rumus tersebut
            gray = int(thc * pow(gray, 1./thy)) #untuk mendapatkan nthrootpower memanfaatkan variabel dalam bentuk integer pada nilai keabuan dimensi c dikalikan dengan powerlaw berisikan variabel nilai grey dan invers keabuan pada dimensi y
            if gray > 255: #menentukan nilai ambang batas atas
                gray = 255 #mengisi nilai gray pada nilai 255 atau putih
            if gray < 0: #menentukan nilai ambang batas bawah
                gray = 0 #mengisi nilai gray pada nilai 0 atau hitam
            img_nthpower[y][x] = (gray, gray, gray) #hasil tampilan pada setiap elemen RGB gambar nth root powerlaw akan menampilkan hasil gray

#Menampilkan hasil
nthrootpower(50, 100) #hasil nilai nth powerlaw diberikan resolusi 50 hingga 100 pixel
plt.imshow(img_nthrootpower) #menggunakan library matplotlib untuk memanggil hasil modifikasi yaitu untuk gambar nth root powerlaw
plt.title("Nth Root Power") #menggunakan library matplotlib untuk memberikan nama pada hasil tampilan gambar yang dipanggil yaitu Nth Root Power
plt.show() #menggunakan library matplotlib untuk memvisualisasikan hasil modifikasi tampilan yang dipanggil sebelumnya dengan fungsi imshow