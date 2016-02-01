direction = "off"
me = "I"
mephrase= " "+me
article = me.lower()+"t"
verb = "shake"
phrase1 = verb+" "+article+" "+direction
line1 = phrase1 + mephrase + " "+phrase1
line2 = line1 + (mephrase * 2)
print line1+(" oooh"*3)
print line2
print me+" "+line2
print me+" "+line1