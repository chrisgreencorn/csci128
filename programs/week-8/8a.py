wav=pickAFile()
sound=makeSound(wav)
play(sound) #original volume

def increaseVolumeNamed(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample,value * 3)

play(sound) #3x louder = +9db
 
 