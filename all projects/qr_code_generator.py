# import qrcode

# data = input("Enter the text or. URL: ").strip()
# filename = input("Enter the filename: ").strip()

# qr = qrcode.QRCode(box_size=10, border = 4)
# qr.add_data(data)

# image = qr.make_image(fill_color = "black", back_color = "white")
# image.save(filename)


import qrcode

# Data to encode
data = input("Enter the URL: ").strip()
filename = input("Enter the filename: ").strip()

# Create QR code object
qr = qrcode.QRCode()

# Add data to the QR code
qr.add_data(data)

# Generate the QR code
# qr.make()

# Create an image from the QR code
img = qr.make_image()

img.save(filename)