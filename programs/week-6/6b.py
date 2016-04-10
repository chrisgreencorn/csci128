def makeCollageWith2Pictures():
  setMediaPath()
  src = makePicture(pickAFile())
  canvas = makeEmptyPicture((getWidth(src)*2),(getHeight(src)*1)) 
  writePictureTo(canvas,'/tmp/canvas.jpg')
  trg = makePicture('/tmp/canvas.jpg')
    
  # First Copy (Source, left)
  targetX = 0
  for x in range(0,getWidth(src)):
    targetY = 0
    for y in range(0,getHeight(src)):
      color = getColor(getPixel(src,x,y))
      setColor(getPixel(trg,targetX,targetY),color)
      targetY = targetY + 1
    targetX = targetX + 1
  
  # Define sunset-izer function
  def makesunset(src):
    def reduceBlue(src):
      for p in getPixels(src):
        value = getBlue(p)
        setBlue(p,value*0.7)
    def reduceGreen(src):
      for p in getPixels(src):
        value = getGreen(p)
        setGreen(p,value*0.7)
    reduceBlue(src)
    reduceGreen(src)
  
  # Sunset-ize source, write to temp
  makesunset(src)
  writePictureTo(src,'/tmp/sunset.jpg')
  sunset = makePicture('/tmp/sunset.jpg')
  
  # Second Copy (Sunset, left)
  targetX = getWidth(src)
  for x in range(0,getWidth(sunset)):
    targetY = 0
    for y in range(0,getHeight(sunset)):
      color = getColor(getPixel(sunset,x,y))
      setColor(getPixel(trg,targetX,targetY),color)
      targetY = targetY + 1
    targetX = targetX + 1
  
  show(trg)