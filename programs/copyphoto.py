def copyPhoto():
  # Set up the source and target pictures
  setMediaPath()
  bigbenPath=getMediaPath("bigben.jpg")
  bigben = makePicture(bigbenPath)
  canvasf = getMediaPath("640x480.jpg")
  canvas = makePicture(canvasf)
  # Now, do the actual copying
  X = 0
  for x in range(0,getWidth(bigben)):
    Y = 0
    for y in range(0,getHeight(bigben)):
      color = getColor(getPixel(bigben,x,y))
      setColor(getPixel(canvas,X,Y), color)
      Y = Y + 1
    X = X + 1
  show(bigben)
  show(canvas)
  return canvas