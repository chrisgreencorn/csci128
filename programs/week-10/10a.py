def cosWave(freq,amplitude):
  buildCos = makeEmptySoundBySeconds(2)
  sr = getSamplingRate(buildCos)
  interval = 1.0/ freq
  samplesPerCycle = interval * sr
  maxCycle = 2 * pi
  for pos in range (0, getLength(buildCos)):
    rawSample = cos((pos/samplesPerCycle) * maxCycle)
    sampleVal = int(amplitude*rawSample)
    setSampleValueAt(buildCos,pos,sampleVal)
  play(buildCos) 