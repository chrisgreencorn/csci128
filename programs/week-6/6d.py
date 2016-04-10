def copyPhotoSideways():
  setMediaPath()
  src = makePicture(pickAFile())
  canvas = makeEmptyPicture(getWidth(src)*3,getHeight(src)) 
  writePictureTo(canvas,'/tmp/canvas.jpg')
  trg = makePicture('/tmp/canvas.jpg')
    
  # Copy (Source, to the right)
  targetX = 0
  for x in range(0,getWidth(src)):
    targetY = 0
    for y in range(0,getHeight(src)):
      color = getColor(getPixel(src,x,y))
      setColor(getPixel(trg,targetX,targetY),color)
      targetY = targetY + 1
    targetX = targetX + 1
  
  targetX = getWidth(src)*2
  for x in range(0,getWidth(src)):
    targetY = 0
    for y in range(0,getHeight(src)):
      color = getColor(getPixel(src,x,y))
      setColor(getPixel(trg,targetX,targetY),color)
      targetY = targetY + 1
    targetX = targetX + 1
  show(trg)