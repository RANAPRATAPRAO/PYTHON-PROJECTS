# need to install library pyqrcode
# alll these project will run in the new environment so make sure that you have created new envionment
# and then we have to install pypng in the environment
import pyqrcode
def qrccode():
    q=pyqrcode.create(input())
    q.png("qrcode.png",scale=6)
    print("qr Generated")

if __name__ == "__main__":
    qrccode()