import tinify
import base64

with open("real.jpg", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    print(str)

with open("real.jpg", 'rb') as source:
    source_data = source.read()
    result_data = tinify.from_buffer(source_data).to_buffer()
    print(result_data)