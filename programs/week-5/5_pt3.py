file = pickAFile()
picture = makePicture(file)


def reduceBlue(picture):
  for p in getPixels(picture):
    value = getBlue(p)
    setBlue(p,value*0.7)

def reduceGreen(picture):
  for p in getPixels(picture):
    value = getGreen(p)
    setGreen(p,value*0.7)

def makeSunset(picture):
  reduceBlue(picture)
  reduceGreen(picture)


makeSunset(picture)
repaint(picture)