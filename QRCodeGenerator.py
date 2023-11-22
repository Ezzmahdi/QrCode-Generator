import qrcode

def generate_qrcode(url, file_name = "qrcode.png"):
    qr = qrcode.QRCode(
        version = 1,
        error_correction =  qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )

    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color = 'black', back_color = 'white')
    img.save(file_name)

link = input('Enter your url: ')
file = input('Enter your file name: ') + '.png'
generate_qrcode(link)