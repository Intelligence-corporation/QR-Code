import qrcode


data = {
    '01': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '02': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31394",
    '03': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '04': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '05': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '06': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '07': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '08': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '09': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '10': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '11': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '12': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '13': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '14': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '15': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '16': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '17': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '18': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '19': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '20': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '21': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '22': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '23': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '24': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '25': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '26': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '27': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '28': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '29': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '30': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '31': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '32': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '33': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '34': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '35': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '36': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '37': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '38': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '39': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '40': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '41': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '42': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '43': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '44': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '45': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '46': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '47': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '48': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '49': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
    '50': "https://segmuc.altamira.pa.gov.br/servicos/validacao/index.php?code=31387",
}

if __name__ == '__main__':
    for i, (key, value) in enumerate(data.items()):
        qr = qrcode.QRCode(qrcode.ERROR_CORRECT_H, box_size=28, border=1)
        qr.add_data(value)
        img = qr.make_image(fill_color='black', back_color='white')
        img.save(f'qrcode/{key}.png')
