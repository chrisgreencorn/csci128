# CSCI128 Lab 9 #


#### Chris Greencorn ####

## Lab 9 ##

#### 1. Write a function that will create a new sound with one half of one sound and then add the two sounds together and then add the second half of the second sound. This is easiest to do if the sounds have the same length. ####

```
c4 = makeSound(pickAFile())
e4 = makeSound(pickAFile())
lengthC = getLength(c4) 
lengthE = getLength(e4) # both samples are the same length
mixpoint = (lengthC)/2
contLength = mixpoint+lengthE
container = makeEmptySound(contLength)

def makeMixedSound(c4,e4):
  for index in range(0, mixpoint):
    sample1 = getSampleValueAt(c4, index)
    setSampleValueAt(container, index, sample1)
  for index in range(mixpoint, length1):
    cSample = getSampleValueAt(c4, index)
    eSample = getSampleValueAt(e4, (index-mixpoint))
    cmajDiad = 0.5 * cSample + 0.5 * eSample
    setSampleValueAt(container, index, cmajDiad)
  for index in range(length1,contLength):
    sample2 = getSampleValueAt(e4, (index-mixpoint))
    setSampleValueAt(container, index, sample2)
  
  play(container)
  
```

#### 2. Blend in some words over some music. Start with the music at 75% and the words at 25% and gradually make the words 75% and the music 25%. ####

```
setMediaPath('/Users/chrisgreencorn/Desktop/lab 9')
file1 = makeSound(pickAFile()) 
file2 = makeSound(pickAFile())
container = makeEmptySoundBySeconds(60)
sr = getSamplingRate(container)

def makeFade(): 
  ## ITERATE
  for index in range(0, getLength(container)):
    ## DEFINE FADE 
    v1 = 0.25 # INITIAL VOLUME OF FILE 1
    if v1 < 0.75: # MAX VOLUME
      v1 = v1 + (index*(0.1/sr)) # FADE GRADIENT
    v2 = 0.75  # INITIAL VOLUME of FILE 2
    if v2 > 0.25: # MIN VOLUME
      v2 = v2 - (index*(0.05/sr)) # FADE GRADIENT
    ## BLEND
    wordsSample = getSampleValueAt(file1, index)
    musicSample = getSampleValueAt(file2, index)
    sampleBlend = wordsSample*v1 + musicSample*v2
    setSampleValueAt(container, index, sampleBlend)
    
  play(container)
  
```

