import qrcode as qrc
import image


def main():
    qr = qrc.QRCode(
    version = 15, # version of the qr code 
    box_size = 10, # size of the qr code
    border = 4,
    )
    data = input("Enter the data of the Qr to create : ")
    qr.add_data(data)
    qr.make(fit = True)
    img = qr.make_image(fill="blue", back_color = "white")
    img.save("qrcode.png")

if __name__ == '__main__':
    main()
