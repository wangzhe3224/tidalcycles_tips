Clock.bmp = 100
Scale.default=Scale.minor

chord = var([0,5,2,3]+PRand(-1,1), [8,4,2,2])
b1 >> bass(chord, dur=PSum(3,2), amp=1.2).every(2, "reverse").every(8, "shuffle")
b2 >> bass([0, 0.5, var([1.5, 0], [7,1])], dur=var([3,4]), oct=3, shape=2, 
            slide=PRand([-1,0,-2,-3]),
            coarse=PRand([4,8,16,24])*PRand([1,1.5])
            )  # strange sounds!!!!
            
d1 >> play("X-", dur=1/2).every(8, "amen")
d2 >> play(" (Oo)#", dur=1, shape=0.3, crush=0.4, slide=linvar([-1,1]))
d3 >> play("funky", rate=PRand([1, 1.5, 1.25]), dur=1/4, pan=[-1, 1])
d4 >> play("Iiii{tttt}", sample=var([0,1,2,3])).every(5, "reverse")
d4 >> play("p[pp][ppp]", amp=var([0, 1], 6)).every(3, "reverse")

p1 >> pads(chord+var([0, 2]), dur=PDur(3,8), chop=4, sus=2, amp=0.5)  ## Nice echo effect!
p2 >> play("Cx  ", dur=8, coarse=16, slide=[-1,1]).every(4, "reverse")
p3 >> blip(dur=12, fmod=4, vib=12, slide=linvar([-1, 1]), sus=4, bits=8, cursh=8, amp=1.2)

s1 >> saw(PWhite(32), bits=4, dur=1/4, crush=2, amp=1)
s1.every(8, "degrade")

Master().lpf = var([0, 1000], [28, 8])  # remove low freq
Master().lpr = var([0.1, 1])
