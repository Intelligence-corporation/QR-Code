import qrcode

# Dicionário para armazenar os links
links = {}

print("Hello, world")

ok = 1
while ok == 1:
    quantify = int(input("How many QR codes do you want to generate? "))
    for c in range(quantify):
        link = input("Enter the link for QR code {}: ".format(c+1))
        confirmation = input("Do you want to add this link? (s/n): ")
        while confirmation.lower() not in ['s', 'n']:
            confirmation = input("Please enter 's' for yes or 'n' for no: ")
        if confirmation.lower() == 's':
            links["QR{}".format(c+1)] = link
    ok = 0

# Gerar QR codes para cada link
for name, link in links.items():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=28,
        border=1,
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("{}.png".format(name))
    print("QR code generated for {}: {}.png".format(name, name))
    print("Thank you for using my services. \nBy: Angell Belger")
