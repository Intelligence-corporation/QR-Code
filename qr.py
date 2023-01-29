import qrcode


data = {
    '00': "https://intelligence-corporation.github.io/GCM-WWW/",
    '01': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00001.html",
    '02': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00002.html",
    '03': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00003.html",
    '04': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00004.html",
    '05': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00005.html",
    '06': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00006.html",
    '07': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00007.html",
    '08': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00008.html",
    '09': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00009.html",
    '10': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00010.html",
    '11': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00011.html",
    '12': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00012.html",
    '13': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00013.html",
    '14': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00014.html",
    '15': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00015.html",
    '16': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00016.html",
    '17': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00017.html",
    '18': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00018.html",
    '19': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00019.html",
    '20': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00020.html",
    '21': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00021.html",
    '22': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00022.html",
    '23': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00023.html",
    '24': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00024.html",
    '25': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00025.html",
    '26': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00026.html",
    '27': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00027.html",
    '28': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00028.html",
    '29': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00029.html",
    '30': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00030.html",
    '31': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00031.html",
    '32': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00032.html",
    '33': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00033.html",
    '34': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00034.html",
    '35': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00035.html",
    '36': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00036.html",
    '37': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00037.html",
    '38': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00038.html",
    '39': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00039.html",
    '40': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00040.html",
    '41': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00041.html",
    '42': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00042.html",
    '43': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00043.html",
    '44': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00044.html",
    '45': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00045.html",
    '46': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00046.html",
    '47': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00047.html",
    '48': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00048.html",
    '49': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00049.html",
    '50': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00050.html",
    '51': "https://intelligence-corporation.github.io/GCM-WWW/010001/mat00051.html",
}

if __name__ == '__main__':
    for i, (key, value) in enumerate(data.items()):
        qr = qrcode.QRCode(qrcode.ERROR_CORRECT_H, box_size=28, border=1)
        qr.add_data(value)
        img = qr.make_image(fill_color='black', back_color='white')
        img.save(f'qrcode/{key}.png')