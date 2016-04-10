file = pickAFile()
picture = makePicture(file)

def decreaseRedBottomHalf(picture):
  pixels = getPixels(picture)
  for index in range(len(pixels)/2,len(pixels)):
   pixel = pixels[index]
   value = getRed(pixel)
   setRed(pixel,value*0.7)

decreaseRedBottomHalf(picture)
repaint(picture)

