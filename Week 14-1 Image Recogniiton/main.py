import cv2 #import lib

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread('image4.jpeg',3) #baca gambar

faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20))

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)  # Menggambar persegi di sekitar wajah
#deteksi mata
    roi_gray = img[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

#adding eye detection
eyes = eye_cascade.detectMultiScale(roi_gray)
for (ex,ey,ew,eh) in eyes:
    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

# Tampilkan gambar dengan kotak deteksi wajah
cv2.imshow('Gambar Tampil dengan Deteksi Wajah', img)

# Tunggu tombol ditekan
keyboard = cv2.waitKey(0)

# Tutup semua jendela jika tombol ESC (kode 27) ditekan
if keyboard == 27:
    cv2.destroyAllWindows()

   