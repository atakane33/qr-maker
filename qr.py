import qrcode

img = qrcode.make('"Your src/img/link"')

type(img)

img.save('"your format(usually jpg)"')
