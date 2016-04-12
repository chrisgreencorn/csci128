# CSCI 128 Term Project #


#### Chris Greencorn ####

## Term Project ##

#### 1. Write a function to create a movie where a red circle is moving from the top to the bottom and another item is moving from the bottom to the top. ####

```
def circleMovie(directory):
  for n in range(1,90):
    canvas = makeEmptyPicture(640,480)
    # red circle
    addOvalFilled(canvas,n+10,n*10,35,35,red)   
    # object two
    addRectFilled(canvas, n+500,getHeight(canvas)-n*10,60,10,blue)
    nString = str(n)
    if n < 10:
      writePictureTo(canvas, directory+'/frame0'+nString+'.jpeg')
    if n >= 10:
      writePictureTo(canvas, directory+'/frame'+nString+'.jpeg')
  circleMovie = makeMovieFromInitialFile(directory+'/frame01.jpeg')
  # return(circleMovie)
  playMovie(circleMovie)       

```

#### 2. Write a function to create a movie where one item is moving in a diagonal line from the top to bottom right and another item is moving from the right to the left. ####

```
def twoObjectMovie(directory):
  for n in range(1,48):
    canvas = makeEmptyPicture(640,480)
    # object one: diag. right, top to bottom
    addOvalFilled(canvas,(n+400)+10,n*10,50,35,green)   
    # object two: left to right
    addRectFilled(canvas,n,400,60,10,makeColor(233,54,107))
    nString = str(n)
    if n < 10:
      writePictureTo(canvas, directory+'/frame0'+nString+'.jpeg')
    if n >= 10:
      writePictureTo(canvas, directory+'/frame'+nString+'.jpeg')
  circleMovie = makeMovieFromInitialFile(directory+'/frame01.jpeg')
  # return(circleMovie)
  playMovie(circleMovie)   

```

#### 3. Write a function to make a movie that draws a sun on the picture of a beach at different places on the picture so that it looks like the sun moving through the sky. Describe how you design the trajectory using code. Also use code to add some effect of picture’s color change due to the sunset. ####

```
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
  addOvalFilled(canvas,342-(frame*5),62+(frame*5),20,20,yellow)
  # trajectory: yellow circle (sun) starts in upper right  - increase in frame 
  # variable accelerates approach to zero on both x and y axes giving the illusion
  # of the sun's path in the sky 

def sunsetOnBeach():
  canvas = beachPic
  # Sun setting
  for frame in range(1,):
    makeSettingSun(beachPic,frame)
    makeSunset(beachPic)
    print frame
  writeFrames()
  
  sunsetMovie = makeMovieFromInitialFile(directory+'/frame01.jpeg')
  # return(circleMovie)
  playMovie(circleMovie)   

```

No screenshot because this program would have taken hours to finish. 