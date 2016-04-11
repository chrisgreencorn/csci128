
  
def normalizeAndDrop(sound):
  # Normalizing First Second
  sound = makeSound(sound)
  samplesPerSecond = getSamplingRate(sound)
  sps = samplesPerSecond
  loudest = getSampleValueAt(sound,0)
  for sampleIndex in range(1,sps):
    if loudest < getSampleValueAt(sound,sampleIndex):
      loudest = getSampleValueAt(sound,sampleIndex)
    normfactor = 32767.0/loudest
    normlevel = normfactor * getSampleValueAt(sound,sampleIndex)
    setSampleValueAt(sound,sampleIndex,normlevel)
# Dealing with the rest of the audio clip  
  factor = 0.8
  for sampleIndex in range(sps,getLength(sound)):
    if sampleIndex % sps == 0:
      factor = factor
      value = getSampleValueAt(sound,sampleIndex)
      setSampleValue(sampleIndex,value*factor)
    else:
      factor = factor - 0.2
      value = getSampleValueAt(sound,sampleIndex)
      setSampleValue(sampleIndex,value*factor)
  
  play(sound)
         
      