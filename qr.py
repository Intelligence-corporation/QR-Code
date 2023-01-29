import qrcode


data = {
    '01': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00001.html",
    '02': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00002.html",
    '03': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00003.html",
}

if __name__ == '__main__':
    colour = [(PG_BLUE, 'white'), ('white', PG_GREEN), (PG_BLUE, PG_GREEN)]
    for i, (key, value) in enumerate(data.items()):
        qr = qrcode.QRCode(none, qrcode.ERROR_CORRECT_H, box_size=18, border=2, )
        img = qr.make_image(fill_color=colour[i][0], back_color=)
        img.save(f'{key}.py')