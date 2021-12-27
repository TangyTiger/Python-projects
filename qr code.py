import qrcode

input = input("Enter Website: ")

image = qrcode.make(input)
image.save("qr.png", "PNG")
print("qr code made, check folder")
