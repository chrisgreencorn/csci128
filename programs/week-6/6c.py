def quarterScale():
  setMediaPath()
  src = makePicture(pickAFile())
  canvas = makeEmptyPicture(getWidth(src)/4,getHeight(src)/4) 
  writePictureTo(canvas,'/tmp/canvas.jpg')
  trg = makePicture('/tmp/canvas.jpg')
  
   # Scaled Copy
  targetX = 0
  for x in range(0,getWidth(src),4):
    targetY = 0
    for y in range(0,getHeight(src),4):
      color = getColor(getPixel(src,x,y))
      setColor(getPixel(trg,targetX,targetY),color)
      targetY = targetY + 1
    targetX = targetX + 1
    
  show(src)
  show(trg)
  writePictureTo(trg,'/tmp/quarter.jpg')