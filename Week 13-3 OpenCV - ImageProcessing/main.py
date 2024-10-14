import cv2 #import lib
img = cv2.imread('image.png',0) #baca gambar
img[img>100]=100
# imd = img.copy()

if img is None:
    print('image not found')
    exit(0)

gambar_asli= cv2.imshow('Gambar Tampil',img) #Menampilkan citra gambar

keyboard = cv2.waitKey(0) #Membuat Variabel untuk menunggu keyboard tertekan

if keyboard == 27: #jika keyboard no 27 tertekan ESC
    cv2.destroyAllWindows() #maka tutup windows

