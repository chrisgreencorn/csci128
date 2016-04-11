setMediaPath('/Users/chrisgreencorn/Desktop/lab 9')
file1 = makeSound(pickAFile()) 
file2 = makeSound(pickAFile())
container = makeEmptySoundBySeconds(60)
sr = getSamplingRate(container)   

def makeFade(): 
  ## ITERATE
  for index in range(0, getLength(container)):
    ## DEFINE FADE 
    v1 = 0.25 # initial volume file 1
    if v1 < 0.75: # max volume
      v1 = v1 + (index*(0.1/sr)) # fade gradient
    v2 = 0.75  # initial volume file 2
    if v2 > 0.25: #min volume
      v2 = v2 - (index*(0.05/sr)) # fade gradient
    ## BLEND
    wordsSample = getSampleValueAt(file1, index)
    musicSample = getSampleValueAt(file2, index)
    sampleBlend = wordsSample*v1 + musicSample*v2
    setSampleValueAt(container, index, sampleBlend)
    
  play(container)
  

