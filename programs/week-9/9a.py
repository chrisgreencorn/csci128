c4 = makeSound(pickAFile())
e4 = makeSound(pickAFile())
lengthC = getLength(c4)
lengthE = getLength(e4)
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
