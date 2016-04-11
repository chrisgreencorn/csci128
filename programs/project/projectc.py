beachPic=makePicture('/Users/chrisgreencorn/Desktop/project/beach.jpg')
directory='/Users/chrisgreencorn/Desktop/project/sunset'  

def writeFrames(frame):
  frameString = str(frame)
  if frameString < 10:
    writePictureTo(canvas, directory+'/frame0'+frameString+'.jpeg')
  if frameString >= 10:
    writePictureTo(canvas, directory+'/frame'+frameString+'.jpeg')
    
def makeSunset(canvas):
  for p in getPixels(canvas):
    value=getBlue(p)
    setBlue(p,value*0.9)
    value=getGreen(p)
    setGreen(p,value*0.9)
      
def makeSettingSun(canvas,frame):
  addOvalFilled(canvas,342-(frame-10),62-(frame+10),20,20,yellow)

def sunsetOnBeach():
  canvas = beachPic
  # Sun setting
  for frame in range(1,16):
    makeSettingSun(beachPic,frame)
    makeSunset(beachPic)
    print frame
  writeFrames()
  
  sunsetMovie = makeMovieFromInitialFile(directory+'/frame01.jpeg')
  # return(circleMovie)
  playMovie(circleMovie)   
    