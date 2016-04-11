def increaseVolumeByFactor(wav,factor):
  sound=makeSound(wav)
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample,value*factor)
  play(sound)