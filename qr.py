import qrcode


data = {
    '01': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00001.html",
    '02': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00002.html"
}

if __name__ == '__main__':
    for i, (key, value) in enumerate(data.items()):
        qr = qrcode.QRCode(qrcode.ERROR_CORRECT_H, box_size=18, border=2, )
        qr.add_data(value)
        img = qr.make_image(fill_color='black', back_color='white')
        img.save(f'{key}.png')