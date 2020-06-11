## Some effects..

p1 >> pads([0,[4,6,7]], dur=PDur(3,8), chop=4, sus=2)  ## Nice echo effect!

p2 >> play("C", dur=4, coarse=16)  ## another kind of echo.. 

b1 >> bass(dur=2, coarse=0, chop=4)

d1 >> play("x-o-", hpf=2000, hpr=0.5)

d1 >> play("x-o-", lpf=1000)

d1 >> play("X O ", bits=4, crush=1)

p1 >> pads(dur=4, sus=1, spin=4)

p1 >> pluck([0, 4], dur=4, glide=[7,-7]).sometimes("shuffle")
