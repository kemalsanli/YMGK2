import base64

def base64_str():
    with open("temp/sonuc.png", "rb") as img_file:
        base64_string = base64.b64encode(img_file.read())
    return base64_string