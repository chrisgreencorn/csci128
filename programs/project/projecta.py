# Write a function to create a movie where a red circle is moving from the top to the bottom
# and another item is moving from the bottom to the top.



def circleMovie(directory):
  for n in range(1,90):
    canvas = makeEmptyPicture(640,480)
    # ball one
    addOvalFilled(canvas,n+10,n*10,35,35,red)   
    # ball two
    addRectFilled(canvas, n+500,getHeight(canvas)-n*10,60,10,blue)
    nString = str(n)
    if n < 10:
      writePictureTo(canvas, directory+'/frame0'+nString+'.jpeg')
    if n >= 10:
      writePictureTo(canvas, directory+'/frame'+nString+'.jpeg')
  circleMovie = makeMovieFromInitialFile(directory+'/frame01.jpeg')
  # return(circleMovie)
  playMovie(circleMovie)       