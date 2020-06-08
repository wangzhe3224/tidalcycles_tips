# I like this one!

b1 >> bass(ch, dur=PSum(3,2))  # P[0.75, 0.75, 0.5]

ch = var([0,5,1,4], [8,4,2,2])  # values, duration
v1 >> viola(ch + [[2,0,0], 0, [0,2,2], [0,0,2]], dur=ch.dur, oct=(4, 5)) + var([(0,2,4), (2, 4)], [28,4])
v1.amp=var([0.5, 0.1], [48, 16])

A = var([0.7, 0], [16.5, 15.5])
z1 >> zap([3,2,0], dur=1/3, amp=A, pan=-1, sus=1/2)
p1 >> pluck([0,2], dur=1/4, amp=A, pan=1, sus=1/2) + [0,0,[0,0,1]]

be >> bell([2,1,0,2,3], dur=PSum(4,5), oct=(5,6), amp=var([0.4, 0.6])) + var([0,4,0,2], [12, 4.5, 11.5, 4])

be.stop()

k1 >> play("(x )(-[-x]-)")
h1 >> play("  ( H) ")
s1 >> play("  o ")
n1 >> play(" (   I)I(    [II])")
m1 >> play("m  m  m")
f1 >> play("pp[pp][ppp]")
f1.amp=var([0,1], [31,1])
f1.pan=(-.5,.5)
tm.rate=(.8, 1)
tm.pan=(-.5, .5)
##### : ) 

g = Group(k1, h1, s1, n1, m1, f1)
g.lpf = 1000

z1.stop()
p1.stop()
v1.stop()
b1.stop()
g.stop()

### This is a funny one!!!! 
Scale.default.set("minor")

print(PSum(5,16))

p1 >> pluck([(0, 2, 4), (0, 3, 5)], dur=4)

pat = [4,2,3]*4+[7,5,4,3,2]
dur = [1,1/2,1/2]*4+[1/2, 1/2]
p1 >> pluck(pat,dur=dur, sus=1)

b1 >> play("x ")
h1 >> play("----- ")
sn >> play("  o    o   o   o  o oo[ o]".replace('o', 'i'))
fl >> play("[  p ]")

ch = var([0,1,-2,3], [4,5])
print(ch)
b2 >> bass(ch, dur=PSum(5,3), slidefrom=[1,1,[1,1,2]])


cc >> charm((ch, ch+2, ch+4, 9)).offbeat()

dd >> dirt([2,1,0,4], oct=6, )
dd.amp=var([0.5, 0.1], [48, 16])

### : )








