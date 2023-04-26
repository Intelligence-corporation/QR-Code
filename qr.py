import qrcode


data = {
    '01-Moraes': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31387",
    '02-Gilmara': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31396",
    '03-Josival': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31400",
    '04-Bernardo': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31394",
    '05-Lenilce': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31401",
    '06-Abreu': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31402",
    '07-Silva': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31389",
    '08-Balieiro': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31383",
    '09-Costa': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31390",
    '10-Patricia': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31405",
    '11-Euclides': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31392",
    '12-Nogueira': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31398",
    '13-Batista': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31409",
    '14-Ricardo': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31406",
    '15-Odilavio': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31404",
    '16-Moreira': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31403",
    '17-Dias': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31386",
    '18-Adson': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31384",
    '19-Braga': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31408",
    '20-Suane': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31410",
    '21-Carla': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31461",
    '22-Souza': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31453",
    '23-Aranha': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31443",
    '24-Milanski': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31441",
    '25-PSilva': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31465",
    '26-Trevisani': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31463",
    '27-Giselle': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31452",
    '28-Vieira': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31439",
    '29-Adriano': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31469",
    '30-Ribeiro': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31444",
    '31-Macedo': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31457",
    '32-Marinho': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31445",
    '33-Leowecke': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31460",
    '34-Cavalcante': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31468",
    '35-Joel': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31456",
    '36-DeLima': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31447",
    '37-Pinho': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31467",
    '38-Aquilino': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31454",
    '39-Hélio': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31451",
    '40-Lopes': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31462",
    '41-Paulo': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31464",
    '42-Reis': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31450",
    '43-Fonseca': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31458",
    '44-Santana': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31446",
    '45-Amaral': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31466",
    '46-CSantos': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=31442",
    '47-Alexsandro': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=1517600",
    '48-Belger': "https://segmuc.altamira.pa.gov.br/servicos/validacao/funcional?code=1517619"

}

if __name__ == '__main__':
    for i, (key, value) in enumerate(data.items()):
        qr = qrcode.QRCode(qrcode.ERROR_CORRECT_H, box_size=28, border=1)
        qr.add_data(value)
        img = qr.make_image(fill_color='black', back_color='white')
        img.save(f'qrcode/{key}.png')
