import tinify,glob

gimg=glob.glob('C:\\Users\\USER\\Desktop\\Full Project Image Compressor\\unoptimized images\\*.jpg')
tinify.key = "rhHdcp47pcLK16n8mPmd2Vyy0cxPKR70"

def imgcompress():
    count=1
    for timg in gimg:
        source = tinify.from_file(timg)
        source.to_file(timg)
        source = tinify.from_file(timg)
        resized = source.resize(
            method="fit",
            width=250,
            height=250
        )
        resized.to_file(timg)
        source = tinify.from_file(timg)
        copyrighted = source.preserve("copyright", "creation")
        path="C:\\Users\\USER\\Desktop\\Full Project Image Compressor\\optimized images\\"
        name= path + "optimized" + str(count) + ".jpg"
        copyrighted.to_file(name)
        print("Done Optimizing:",count)
        count +=1 


imgcompress()



































































# with open("real.jpg", 'rb') as source:
#     source_data = source.read()
#     result_data = tinify.from_buffer(source_data).to_buffer()
#     print(result_data)

# source = tinify.from_url("https://upload.wikimedia.org/wikipedia/commons/8/8c/Cristiano_Ronaldo_2018.jpg")
# source.to_file("optimizedronaldo.jpg")