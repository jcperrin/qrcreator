"""
This script creates a qr label of the input file.

@author JC Perrin
@date 2017-09-09
"""

from PIL import Image
import qrcode
import sys

DEF_O_FNAME = 'out.png'

def to_qr(data, fname):
    """ Accepts a random peice of data and a filename and saves an image
    of a QR code to that filename.
    """
    # create a new instance of class QRCode allows for more control over
    # the type of QRCode generated
    qr = qrcode.QRCode(
            version=1
            )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    img.save(fname)

def main():
    to_qr('Hello, world!', DEF_O_FNAME)
    print 'Main completed'

if __name__=='__main__':
    main()
