import qrcode


data = {
    'puzzle': "https://belgercompany.com/secrecy/miss_me.php",
}

print("Hello, world")

ok = 1
while (ok == 1):
    quantify = int(input("How many QR-code do you want?"))
    for c in range(0, quantify):
        data[c] = str(input("link: "))
    ok = 0


if __name__ == '__main__':
    for i, (key, value) in enumerate(data.items()):
        qr = qrcode.QRCode(qrcode.ERROR_CORRECT_H, box_size=28, border=1)
        qr.add_data(value)
        img = qr.make_image(fill_color='black', back_color='white')
        img.save(f'qrcode/{key}.png')
