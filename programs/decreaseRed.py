file = pickAFile()
pic = makePicture(file)


def reduceBlue(pic):
  for p in getPixels(pic):
    value = getBlue(p)
    setBlue(p,value*0.7)

def reduceGreen(pic):
  for p in getPixels(pic):
    value = getGreen(p)
    setGreen(p,value*0.3)

def makeSunset(pic):
  reduceBlue(pic)
  reduceGreen(pic)

makeSunset(pic)
repaint(pic)