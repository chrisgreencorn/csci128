def twoObjectMovie(directory):
  for n in range(1,48):
    canvas = makeEmptyPicture(640,480)
    # object one: diag. right, top to bottom
    addOvalFilled(canvas,(n+400)+10,n*10,50,35,green)   
    # object two: left to right
    addRectFilled(canvas,n+13,400,60,10,makeColor(233,54,107))
    nString = str(n)
    if n < 10:
      writePictureTo(canvas, directory+'/frame0'+nString+'.jpeg')
    if n >= 10:
      writePictureTo(canvas, directory+'/frame'+nString+'.jpeg')
  circleMovie = makeMovieFromInitialFile(directory+'/frame01.jpeg')
  # return(circleMovie)
  playMovie(circleMovie)   