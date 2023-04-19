import qrcode

from userInput import make_your_qr

img=qrcode.make(make_your_qr)
img.save("myqr.jpg")

