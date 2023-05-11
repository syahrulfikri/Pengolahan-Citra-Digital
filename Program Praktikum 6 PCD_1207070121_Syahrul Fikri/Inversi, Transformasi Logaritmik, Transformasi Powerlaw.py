#File : Inversi, Transformasi Logaritmik, Transformasi Powerlaw
#Authors : Syahrul Fikri
#NIM : 1207070121
#Kelas : Pengolahan Citra Digital-C
#Teknik Elektro Fakultas Sains dan Teknologi UIN Sunan Gunung Djati Bandung

#Import Library
import numpy as np
import cv2
import matplotlib.pyplot as plt 

#Membaca Gambar
img = cv2.imread("D:/Tugas Syahrul fikri/1. UIN/PEMBELAJARAN/SEMESTER 6/PCD/Pertemuan Ke-9/Program Praktikum 6 PCD/Dragon.jpeg")
img_height = img.shape[0]
img_width = img.shape[1]
img_channel = img.shape[2]

#Inversi
#Membuat variabel img_inversi
img_inversi = np.zeros(img.shape, dtype=np.uint8)

#Membuat fungsi untuk inversi grayscale
def inversi_grayscale(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = nilai - gray
            img_inversi[y][x] = (gray, gray, gray)

#Membuat fungsi untuk inversi rgb
def inversi_rgb(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            red = nilai - red
            green = img[y][x][1]
            green = nilai - green
            blue = img[y][x][2]
            blue = nilai - blue
            img_inversi[y][x] = (red, green, blue)

#Menampilkan hasil inversi
inversi_grayscale(255)
plt.imshow(img_inversi)
plt.title("Inversi Grayscale")
plt.show()

inversi_rgb(255)
plt.imshow(img_inversi)
plt.title("Inversi RGB")
plt.show()


#LOG
#Membuat variabel img_log untuk menampung hasil
img_log = np.zeros(img.shape, dtype=np.uint8)

#Mendefinisikan fungsi untuk log
def log(c):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(c * np.log(gray + 1))
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            img_log[y][x] = (gray, gray, gray)

#Menampilkan hasil log
log(30)
plt.imshow(img_log)
plt.title("Log")
plt.show()


#INVERSI & LOG
#Membuat variabel img_inlog untuk menampung hasil
img_inlog = np.zeros(img.shape, dtype=np.uint8)

#Mendefinisikan fungsi untuk inversi log
def inlog(c):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(c * np.log(255 - gray + 1))
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            img_inlog[y][x] = (gray, gray, gray)

#Menampilkan hasil inversi log
inlog(30)
plt.imshow(img_inlog)
plt.title("Inversi & Log")
plt.show()

#NTH POWER
#Membuat variabel img_nthpoer untuk menampung hasil
img_nthpower = np.zeros(img.shape, dtype=np.uint8)

#Mendefinisikan fungsi untuk nth power
def nthpower(c, y):
    thc = c / 100
    thy = y / 100
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(thc * pow(gray, thy))
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            img_nthpower[y][x] = (gray, gray, gray)

#Menampilkan hasil
nthpower(50, 100)
plt.imshow(img_nthpower)
plt.title("Nth Power")
plt.show()

#NTH ROOT POWER
#Membuat varaiabel img_nthrootpower
img_nthrootpower = np.zeros(img.shape, dtype=np.uint8)

#Membuat fungsi untuk nth root power
def nthrootpower(c, y):
    thc = c / 100
    thy = y / 100
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(thc * pow(gray, 1./thy))
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            img_nthpower[y][x] = (gray, gray, gray)

#Menampilkan hasil
nthrootpower(50, 100)
plt.imshow(img_nthrootpower)
plt.title("Nth Root Power")
plt.show()