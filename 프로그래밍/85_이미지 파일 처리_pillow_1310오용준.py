from PIL import Image

img=Image.open("GR.jpg")
img.show()

print('이미지 크기:', img.size)
print('이미지 형식:', img.format)
print('이미지 모드:', img.mode)

resized=img.resize((200, 200))
resized.show()

rorated=img.rotate(90)
rorated.show()

gray=img.convert('L')
gray.show()

gray.save('gray_GR.jpg')