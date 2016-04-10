def reduceRedBottomHalf(source):
  file=pickAFile()
  source=makePicture(file)
  for x in range(getWidth(source)-1):
    for y in range((getHeight(source)/2)-1,getHeight(source)-1):
      p=getPixel(source,x,y)
      value=getRed(p)
      setRed(p,value*0.7)
      
  show(source)