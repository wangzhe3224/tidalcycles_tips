Clock.bmp = 136

a = var([0,-2,3], [8,4,4])

# very soft and with feel
k1 >> klank(a+[0,0,-5], sus=4)
l1 >> soprano(a+[2,2,-3], sus=4)

p1 >> soprano(P[(0,2)].loop(9) | PTri(3), dur=PSum(3,2).loop(3) | PSum(6,2), 
           scale=Scale.majorPentatonic,
           oct=(2,2,4,4)).every(1.5, "reverse") + var([0,4,5,3])
p1.amp=0.4
           
b1 >> bass(a, dur=PSum(7,4).loop(2) | PSum(7,4), sus=1)

# Strange sounds...but nice
c1 >> crunch(dur=1/4)

d1 >> dirt(PTri(10)+[0,0,(0, 9), 0, (0,9)], dur=PSum(13,8), scale=Scale.majorPentatonic)


d1 >> play("x[X-] =")
cp >> play("  H ")
hh >> play("- --[- ] -- - --")
ck >> play("^tfr[/f]")

yy >> play(" <!,x,H>  ")


Master().lpf = var([0, 500], [28, 4])
           
      
print(SynthDefs)
