# Note : For this code, I'll only be doing very simple things
# just to keep up with the streak! 
# I'm currently occupied with other tasks & project of mine

# But worry not!
# You can explore more here https://pypi.org/project/qrcode/

import qrcode

# Maybe try to play with the class constructor
# qr = qrcode.QRCode (
#     version=None,
#     error_correction=constants.ERROR_CORRECT_M,
#     box_size=10,
#     border=4,
#     image_factory: Optional[Type[GenericImage]] = None,
#     mask_pattern=None,
# )

# Maybe try to play with custom input for qrcode.make()

img = qrcode.make('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
img.save('my-normal-QRcode.png')

# fr though, only 3 lines of code T_T
