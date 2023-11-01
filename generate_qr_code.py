import qrcode

# image = qrcode.make("https://google.com")
# image.save("qr_create.png")

with open('urls.txt') as file:
    text = file.read()

urls_list = text.split('\n')

#make qr codes
for url in urls_list:
    image = qrcode.make(url)
    name = url.replace('https://','').split('.')[-2]
    image.save(f"qr_{name}.png")

##another solution
# import qrcode
 
# with open('urls.txt') as file:
#   lines = file.readlines()
#   count = 1
#   for line in lines:
#     img = qrcode.make(line)
#     img.save(f"{count}.png")
#     count += 1