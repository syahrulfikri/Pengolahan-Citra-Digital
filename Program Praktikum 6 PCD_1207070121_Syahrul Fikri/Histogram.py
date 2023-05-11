#FIle : Histogram
#Authors : Syahrul Fikri
#NIM : 1207070121
#Kelas : Pengolahan Citra Digital-C
#Teknik Elektro Fakultas Sains dan Teknologi UIN Sunan Gunung Djati Bandung

#Import library
import numpy as np #Pada bagian ini menambahkan library untuk menjalankan program yaitu numpy dengan inisialisasi np yang mendukung scientific computing dalam hal ini digunakan untuk membentuk objek dari dimensi array yang diinginkan
import cv2 #Pada bagian ini saya merubah library dari modul karena untuk menjalankan library imageio pada perangkat ada kesalahan dalam pembacaan sehingga hasil tidak dapat ditampilkan walaupun telah diubah baik ke v3.iio dan imageio.v2 as imageio, namun fungsi cv2 ini juga dapat digunakan untuk membaca data gambar dari file yang dipanggil
import matplotlib.pyplot as plt #Pada bagian ini library matplotplib digunakan untuk melakukan visualisasi pada objek gambar 

#Membaca Gambar
img = cv2.imread("Dragon.jpeg")  #Inisialisasi objek agar dapat dipanggil pada program selanjutnya yaitu menjadi "img" objek tersebut dibaca dengan menggunakan fungsi library cv2 dan menyebutkan nama file yang telah disimpan pada lokasi yang sama dengan program

img_height = img.shape[0] #ukuran pixel/resolusi tinggi dari gambar dihitung oleh fungsi shape dengan array urutan 0/awal
img_width = img.shape[1] #ukuran pixel/resolusi lebar dari gambar dihitung oleh fungsi shape dengan array urutan 1/kedua/selanjutnya
img_channel = img.shape[2] #ukuran pixel/resolusi kanal dari gambar dihitung oleh fungsi shape dengan array urutan 2/ketiga/selanjutnya

#Merubah gambar menjadi Grayscale
img_grayscale = np.zeros(img.shape, dtype = np.uint8) #menginisialisasi variabel pada gambar yang akan diubah dengan inisialisasi "img_flip_horizontal" untuk hasil gambar horizontal dengan format semua elemen gambar diinisialisasi ke 0 karena penggunaan np.zeros selanjutnya akan diukur resolusi dengan fungsi img.shape dan dibaca type filenya dengan fungsi img_type dari hasil inisialisasi sebelumya

for y in range(0, img_height): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen y dengan argumen range yang berisikan nilai yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 untuk nilai tinggi
    for x in range(0, img_width): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 untuk nilai lebar
        red = img[y][x][0] #melakukan inisialisasi terhadap isi variabel untuk elemen red untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 0/pertama
        green = img[y][x][1] #melakukan inisialisasi terhadap isi variabel untuk elemen green untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 1/kedua/selanjutnya
        blue = img[y][x][2] #melakukan inisialisasi terhadap isi variabel untuk elemen blue untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 2/ketiga/selanjutnya
        gray = (int(red) + int(green) + int(blue))/3 #untuk mendapatkan hasil berupa grayscale nilai setiap variabel RGB di kalkulasi dalam rumus tersebut
        img_grayscale[y][x] = (gray,gray,gray) #hasil tampilan pada setiap elemen RGB akan menampilkan hasil gray

plt.imshow(img_grayscale) #menggunakan library matplotlib untuk memanggil hasil modifikasi yaitu untuk gambar konversi RGB ke grayscale
plt.title("Grayscale") #menggunakan library matplotlib untuk memberikan nama pada hasil tampilan gambar yang dipanggil yaitu Grayscale
plt.show() #menggunakan library matplotlib untuk memvisualisasikan hasil modifikasi tampilan yang dipanggil sebelumnya dengan fungsi imshow

#Menampilkan Histogram Gambar Grayscale
#Membuat variabel untuk menyimpan data gambar
hg = np.zeros((256)) #menginisialisasi variabel pada gambar dengan inisialisasi "hg" untuk hasil histogram dengan format semua elemen gambar diinisialisasi ke 0 karena penggunaan np.zeros selanjutnya untuk panjang resolusinya sampai dengan 256

#Mengisi setiap nilai dalam array hg dengan 0
for x in range(0, 256): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga array 256
    hg[x] = 0 #mengisi variabel hg dalam histogram pada elemen x dengan nilainya sama dengan 0

#Menghitung nilai dari gambar
for y in range(0, img_height): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen y dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai tinggi pada file gambar
    for x in range(0, img_width): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai lebar pada file gambar
        gray = img_grayscale[y][x][0] #inisialisasi variabel warna gray untuk setiap elemen y untuk tinggi dan elemen x untuk lebar gambar dengan array pada 0
        hg[gray] += 1 #mengisi variabel hg untuk elemen gray dalam histogram dengan nilai lebih dari sama dengan 1

#Menampilkan Histogram
# plt.figure(figsize=(20, 6))
# plt.plot(hg, color="black", linewidth=2.0)
# plt.show()

bins = np.linspace(0, 256, 100) #memberikan variabel nilai bins pada histogram dengan menggunakan fungsi np.linspace pada library numpy maka jarak spasi antar nilainya akan sama karena berisikan batasan-batasan pada numeriknya dengan nilai interval array dimulai dari 0 hingga 256 dengan jumlah tuple atau nampan 100
plt.hist(hg, bins, color="black", alpha=0.5) #menggunakan library matplotlib dengan menggunakan fungsi hist untuk menampilkan histogram berupa tampilan frekuensi dari data-data numerik yang bersifat kontinu dengan melakukan beberapa modifikasi yaitu menggunakan isi pada variabel hg, panjang nilai dengan variabel bins, warna block histogram yaitu hitam, dan tingkat kontrass blok diagram sebesar 0.5
plt.title("Histogram") #menggunakan library matplotlib untuk memberikan nama pada hasil tampilan yang dipanggil yaitu Histogram
plt.show() #menggunakan library matplotlib untuk memvisualisasikan hasil dari tampilan yang dipanggil yaitu histogram gambar grayscale

#Menampilkan Histogram Gambar RGB
#Membuat variabel untuk menyimpan data gambar
hgr = np.zeros((256)) #menginisialisasi variabel pada gambar dengan inisialisasi "hgr" untuk hasil histogram red dengan format semua elemen gambar diinisialisasi ke 0 karena penggunaan np.zeros selanjutnya untuk panjang resolusinya sampai dengan 256
hgg = np.zeros((256)) #menginisialisasi variabel pada gambar dengan inisialisasi "hgg" untuk hasil histogram green dengan format semua elemen gambar diinisialisasi ke 0 karena penggunaan np.zeros selanjutnya untuk panjang resolusinya sampai dengan 256
hgb = np.zeros((256)) #menginisialisasi variabel pada gambar dengan inisialisasi "hgb" untuk hasil histogram blue dengan format semua elemen gambar diinisialisasi ke 0 karena penggunaan np.zeros selanjutnya untuk panjang resolusinya sampai dengan 256
hgrgb = np.zeros((768)) #menginisialisasi variabel pada gambar dengan inisialisasi "hgrgb" untuk hasil histogram red,green,blue dengan format semua elemen gambar diinisialisasi ke 0 karena penggunaan np.zeros selanjutnya untuk panjang resolusinya sampai dengan 768

#Mengisi setiap nilai dalam array hg dengan 0
for x in range(0, 256): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga array 256
    hgr[x] = 0 #mengisi variabel "hgr" untuk histogram red dalam histogram pada elemen x dengan nilainya sama dengan 0
    hgg[x] = 0 #mengisi variabel "hgg" untuk histogram green dalam histogram pada elemen x dengan nilainya sama dengan 0
    hgb[x] = 0 #mengisi variabel "hgb" untuk histogram blue dalam histogram pada elemen x dengan nilainya sama dengan 0
    
for x in range(0, 768): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga array 768
    hgrgb[x] = 0 #mengisi variabel "hgbrgb" untuk histogram red,green,blue dalam histogram pada elemen x dengan nilainya sama dengan 0

#Menghitung nilai dari gambar
for x in range(0, 256): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga array 256
    hgr[x] = 0 #mengisi variabel "hgr" untuk histogram red dalam histogram pada elemen x dengan nilainya sama dengan 0
    hgg[x] = 0 #mengisi variabel "hgg" untuk histogram green dalam histogram pada elemen x dengan nilainya sama dengan 0
    hgb[x] = 0 #mengisi variabel "hgb" untuk histogram blue dalam histogram pada elemen x dengan nilainya sama dengan 0
    
for x in range(0, 768): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga array 768
    hgrgb[x] = 0 #mengisi variabel "hgbrgb" untuk histogram red,green,blue dalam histogram pada elemen x dengan nilainya sama dengan 0

# th = int(256/64)
temp = [0] #fungsi ini digunakan untuk menyimpan data sementara nilainya dalama array 0
for y in range(0, img.shape[0]): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen y dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai pada array 0 pada file gambar
    for x in range(0, img.shape[1]): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai pada array 1 pada file gambar
        red = int(img[y][x][0]) #melakukan inisialisasi terhadap isi variabel untuk elemen red untuk pixel sumbu y dan pixel sumbu x pada urutan array 0/pertama dengan jenis nilai integer
        green = int(img[y][x][1]) #melakukan inisialisasi terhadap isi variabel untuk elemen green untuk pixel sumbu y dan pixel sumbu x pada urutan array 1/kedua/selanjutnya dengan jenis nilai integer
        blue = int(img[y][x][2]) #melakukan inisialisasi terhadap isi variabel untuk elemen green untuk pixel y untuk tinggi dan pixel sumbu x pada urutan array 1/kedua/selanjutnya dengan jenis nilai integer
        green = green + 256 #untuk menghasilkan histogram green nilai pixel perlu ditambahkan 256 agar tidak tumpang tindih dengan histogram red
        blue = blue + 512 #untuk menghasilkan histogram blue nilai pixel perlu ditambahkan 512 agar tidak tumpang tindih dengan histogram red dan green
# temp.append(green)
        hgrgb[red] += 1 #mengisi variabel hgrgb untuk elemen red dalam histogram dengan nilai lebih dari sama dengan 1
        hgrgb[green] += 1 #mengisi variabel hgrgb untuk elemen green dalam histogram dengan nilai lebih dari sama dengan 1
        hgrgb[blue] += 1 #mengisi variabel hgrgb untuk elemen blue dalam histogram dengan nilai lebih dari sama dengan 1

binsrgb = np.linspace(0, 768, 100) #memberikan variabel nilai bins pada histogram red,green,blue dengan menggunakan fungsi np.linspace pada library numpy maka jarak spasi antar nilainya akan sama karena berisikan batasan-batasan pada numeriknya dengan nilai interval array dimulai dari 0 hingga 768 dengan jumlah tuple atau nampan 100
plt.hist(hgrgb, binsrgb, color="black", alpha=0.5) #menggunakan library matplotlib dengan menggunakan fungsi hist untuk menampilkan histogram berupa tampilan frekuensi dari data-data numerik yang bersifat kontinu dengan melakukan beberapa modifikasi yaitu menggunakan isi pada variabel hgrgb, panjang nilai dengan variabel binsrgb, warna block histogram yaitu hitam, dan tingkat kontrass blok diagram sebesar 0.5
# plt.plot(hgrgb)
plt.title("Histogram Red Green Blue") #menggunakan library matplotlib untuk memberikan nama pada hasil tampilan yang dipanggil yaitu Histogram Red Green Blue
plt.show() #menggunakan library matplotlib untuk memvisualisasikan hasil dari tampilan yang dipanggil yaitu histogram gambar red, green, blue

#Menampilkan Histogram
for y in range(0, img_height): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen y dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai tinggi pada file gambar
    for x in range(0, img_width): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai lebar pada file gambar
        red = img[y][x][0] #melakukan inisialisasi terhadap isi variabel untuk elemen red untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 0/pertama
        green = img[y][x][1] #melakukan inisialisasi terhadap isi variabel untuk elemen green untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 1/kedua/selanjutnya
        blue = img[y][x][2] #melakukan inisialisasi terhadap isi variabel untuk elemen blue untuk pixel y untuk tinggi dan x untuk lebar pada urutan array 2/ketiga/selanjutnya
        hgr[red] += 1 #mengisi variabel hgr untuk elemen red dalam histogram dengan nilai lebih dari sama dengan 1
        hgg[green] += 1 #mengisi variabel hgrgb untuk elemen green dalam histogram dengan nilai lebih dari sama dengan 1
        hgb[blue] += 1 #mengisi variabel hgrgb untuk elemen blue dalam histogram dengan nilai lebih dari sama dengan 1

bins = np.linspace(0, 256, 100) #memberikan variabel nilai bins pada histogram dengan menggunakan fungsi np.linspace pada library numpy maka jarak spasi antar nilainya akan sama karena berisikan batasan-batasan pada numeriknya dengan nilai interval array dimulai dari 0 hingga 256 dengan jumlah tuple atau nampan 100
plt.hist(hgr, bins, color="red", alpha=0.5) #menggunakan library matplotlib dengan menggunakan fungsi hist untuk menampilkan histogram berupa tampilan frekuensi dari data-data numerik yang bersifat kontinu dengan melakukan beberapa modifikasi yaitu menggunakan isi pada variabel hgr, panjang nilai dengan variabel bins, warna block histogram yaitu red, dan tingkat kontrass blok diagram sebesar 0.5
plt.title("Histogram Red") #menggunakan library matplotlib untuk memberikan nama pada hasil tampilan yang dipanggil yaitu Histogram Red
plt.show() #menggunakan library matplotlib untuk memvisualisasikan hasil dari tampilan yang dipanggil yaitu histogram gambar untuk nilai red

plt.hist(hgg, bins, color="green", alpha=0.5) #menggunakan library matplotlib dengan menggunakan fungsi hist untuk menampilkan histogram berupa tampilan frekuensi dari data-data numerik yang bersifat kontinu dengan melakukan beberapa modifikasi yaitu menggunakan isi pada variabel hgg, panjang nilai dengan variabel bins, warna block histogram yaitu green, dan tingkat kontrass blok diagram sebesar 0.5
plt.title("Histogram Green") #menggunakan library matplotlib untuk memberikan nama pada hasil tampilan yang dipanggil yaitu Histogram Green
plt.show() #menggunakan library matplotlib untuk memvisualisasikan hasil dari tampilan yang dipanggil yaitu histogram gambar untuk nilai green

plt.hist(hgb, bins, color="blue", alpha=0.5) #menggunakan library matplotlib dengan menggunakan fungsi hist untuk menampilkan histogram berupa tampilan frekuensi dari data-data numerik yang bersifat kontinu dengan melakukan beberapa modifikasi yaitu menggunakan isi pada variabel hgb, panjang nilai dengan variabel bins, warna block histogram yaitu blue, dan tingkat kontrass blok diagram sebesar 0.5
plt.title("Histogram Blue") #menggunakan library matplotlib untuk memberikan nama pada hasil tampilan yang dipanggil yaitu Histogram Red
plt.show() #menggunakan library matplotlib untuk memvisualisasikan hasil dari tampilan yang dipanggil yaitu histogram gambar untuk nilai red

#Menampilkan Histogram Kumulatif
#Histogram kumulatif ini merupakan hasil gabungan beberap blok histogram yang saling tumpang tindi
hgk = np.zeros((256)) #menginisialisasi variabel pada gambar dengan inisialisasi "hgk" untuk hasil histogram kumulatif dengan format semua elemen gambar diinisialisasi ke 0 karena penggunaan np.zeros selanjutnya untuk panjang resolusinya sampai dengan 256
c = np.zeros((256)) #menginisialisasi variabel pada gambar dengan inisialisasi "c" untuk nilai kumulatif dengan format semua elemen gambar diinisialisasi ke 0 karena penggunaan np.zeros selanjutnya untuk panjang resolusinya sampai dengan 256

for x in range(0, 256): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga array 256
    hgk[x] = 0 #mengisi variabel hgk dalam histogram kumulatif pada elemen x dengan nilainya sama dengan 0
    c[x] = 0 #mengisi variabel c untuk nilai kumulatif pada elemen x dengan nilainya sama dengan 0

for y in range(0, img_height): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen y dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai tinggi pada file gambar
    for x in range(0, img_width): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai lebar pada file gambar
        gray = img_grayscale[y][x][0] #inisialisasi variabel warna gray untuk setiap elemen y untuk tinggi dan elemen x untuk lebar gambar dengan array pada 0
        hgk[gray] += 1 #mengisi variabel hgk untuk elemen gray dalam histogram dengan nilai lebih dari sama dengan 1
                
c[0] = hgk[0] #menginsialisasi nilai c pada array 0 sama dengan histogram kumulatif pada array 0
for x in range(1, 256): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 1 hingga array 256
     c[x] = c[x-1] + hgk[x] #untuk mendapatkan hasil nilai kumulatif pada elemen x dibuat suatu rumus untuk mendapatkannya dengan memanfaatkan variabel kumulatif "c" dan nilai histogram kumulatif "hgk"

hmaxk = c[255] #menginisialisasi nilai maksimum histogram kumulatif sama dengan kumulatif dengan array sampai dengan 255
for x in range(0, 256): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga array 256
    c[x] = 190 * c[x] / hmaxk #untuk mendapatkan hasil nilai kumulatif lainnya pada elemen x dibuat suatu rumus untuk mendapatkannya dengan memanfaatkan variable kumulatif "c" dan nilai histogram kumulatif maksimum "hmaxk"

plt.hist(c, bins, color="black", alpha=0.5) #menggunakan library matplotlib dengan menggunakan fungsi hist untuk menampilkan histogram berupa tampilan frekuensi dari data-data numerik yang bersifat kontinu dengan melakukan beberapa modifikasi yaitu menggunakan isi pada variabel c, panjang nilai dengan variabel bins, warna block histogram yaitu black, dan tingkat kontrass blok diagram sebesar 0.5
plt.title("Histogram Grayscale Kumulatif") #menggunakan library matplotlib untuk memberikan nama pada hasil tampilan yang dipanggil yaitu Histogram Grayscale Kumulatif
plt.show() #menggunakan library matplotlib untuk memvisualisasikan hasil dari tampilan yang dipanggil yaitu histogram gram untuk nilai histogram kumulatif grayscale

#Menampilkan Histogram Hequalisasi
#Histogram Hequalisasi ini merupakan suatu proses perataan histogram, dimana distribusi nilai derajat keabuan pada suatu citra dibuat rata dengan mengubah derajat keabuan suatu piksel dengan derajat keabuan yang baru dengan suatu fungsi transformasi
hgh = np.zeros((256)) #menginisialisasi variabel pada gambar dengan inisialisasi "hgh" untuk hasil histogram hequalisasi dengan format semua elemen gambar diinisialisasi ke 0 karena penggunaan np.zeros selanjutnya untuk panjang resolusinya sampai dengan 256
h = np.zeros((256)) #menginisialisasi variabel pada gambar dengan inisialisasi "h" untuk nilai hequalisasi dengan format semua elemen gambar diinisialisasi ke 0 karena penggunaan np.zeros selanjutnya untuk panjang resolusinya sampai dengan 256
c = np.zeros((256)) #menginisialisasi variabel pada gambar dengan inisialisasi "c" untuk nilai kumulatif dengan format semua elemen gambar diinisialisasi ke 0 karena penggunaan np.zeros selanjutnya untuk panjang resolusinya sampai dengan 256

for x in range(0, 256): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga array 256
    hgh[x] = 0 #mengisi variabel hgh dalam histogram hequalisasi pada elemen x dengan nilainya sama dengan 0
    h[x] = 0 #mengisi variabel h untuk nilai hequalisasi pada elemen x dengan nilainya sama dengan 0
    c[x] = 0 #mengisi variabel c untuk nilai kumulatif pada elemen x dengan nilainya sama dengan 0

for y in range(0, img_height): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen y dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai tinggi pada file gambar
    for x in range(0, img_width): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai lebar pada file gambar
        gray = img_grayscale[y][x][0] #inisialisasi variabel warna gray untuk setiap elemen y untuk tinggi dan elemen x untuk lebar gambar dengan array pada 0
        hgh[gray] += 1 #mengisi variabel hgh untuk elemen gray dalam histogram dengan nilai lebih dari sama dengan 1
                
h[0] = hgh[0] #menginisialisasi nilai hequalisasi pada array 0 sama dengan histogram hequalisasi pada array 0
for x in range(1, 256): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 1 hingga array 256
     h[x] = h[x-1] + hgh[x] #untuk mendapatkan nilai hequalisasi pada elemen x dibuat suatu rumus untuk mendapatkannya menggunakan variabel hequalisasi "h" dan nilai histogram hequalisasi

for x in range(0, 256): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga array 256
     h[x] = h[x] / img_height / img_width #untuk mendapatkan nilai hequalisasi lainnya pada elemen x dibuat suatu rumus untuk mendapatkannya dengan menggunakan variabel hequalisasi "h", panjang nilai tinggi, dan panjang nilai lebar

for x in range(0, 256): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga array 256
    hgh[x] = 0 #mengisi variabel hgh dalam histogram hequalisasi pada elemen x dengan nilainya sama dengan 0
    
for y in range(0, img_height): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen y dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai tinggi pada file gambar
    for x in range(0, img_width): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga nilai lebar pada file gambar
        gray = img_grayscale[y][x][0] #inisialisasi variabel warna gray untuk setiap elemen y untuk tinggi dan elemen x untuk lebar gambar dengan array pada 0
        gray = h[gray] * 255 #menghitung nilai gray dengan menggunakan variabel hequalisasi "h" yang dikalikan dengan 255
        hgh[int(gray)] += 1 #mengisi variabel hgh untuk elemen gray dengan tipe data integer dalam histogram dengan nilai lebih dari sama dengan 1

c[0] = hgh[0] #menginisialisasi nilai kumulatif pada array 0 sama dengan histogram hequalisasi pada array 0
for x in range(1, 256): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 1 hingga array 256
     c[x] = c[x-1] + hgh[x] #untuk mendapatkan hasil nilai kumulatif pada elemen x dibuat suatu rumus untuk mendapatkannya dengan memanfaatkan variabel kumulatif "c" dan nilai histogram kumulatif "hgk"

hmaxk = c[255] #menginisialisasi nilai maksimum histogram kumulatif sama dengan kumulatif dengan array sampai dengan 255

for x in range(0, 256): #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga array 256
    c[x] = 190 * c[x] / hmaxk #penggunaan fungsi for untuk melakukan perulangan variabel untuk elemen x dengan argumen range yang berisikan nilai array yang akan digunakan oleh fungsi for yang berisikan array dimulai dari 0 hingga array 256

plt.hist(c, bins, color="black", alpha=0.5) #menggunakan library matplotlib dengan menggunakan fungsi hist untuk menampilkan histogram berupa tampilan frekuensi dari data-data numerik yang bersifat kontinu dengan melakukan beberapa modifikasi yaitu menggunakan isi pada variabel c, panjang nilai dengan variabel bins, warna block histogram yaitu black, dan tingkat kontrass blok diagram sebesar 0.5
plt.title("Histogram Grayscale Hequalisasi") #menggunakan library matplotlib untuk memberikan nama pada hasil tampilan yang dipanggil yaitu Histogram Grayscale Hequalisasi
plt.show() #menggunakan library matplotlib untuk memvisualisasikan hasil dari tampilan yang dipanggil yaitu histogram gram untuk nilai histogram hequalisasi grayscale