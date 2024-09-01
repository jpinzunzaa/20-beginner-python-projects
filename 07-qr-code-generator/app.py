import qrcode
from qrcode.constants import ERROR_CORRECT_L

def generate_qrcode(text, version=1, error_correction=ERROR_CORRECT_L, box_size=10, border=4, file_path=None):
    qr = qrcode.QRCode(
      version=version,
      error_correction=error_correction,
      box_size=box_size,
      border=border,
    )

    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color='black', back_color='white')

    if file_path:
      img.save(file_path)

    return img