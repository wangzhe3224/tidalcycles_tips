Scale.default = "minor"
Root.default = var([0,2],64)

nodes = P*(0,4,4.5,0.5) + var([0, 0.22], [16, 1])

p1 >> pads(dur=8, room=1, coarse=16, chop=1, lpf=linvar([400, 800], 24), lpr=linvar([0.1, 1], 14)) + nodes
p1.amp=0.7 
p2 >> blip(dur=12, fmod=4, vib=12, slide=-1, oct=7, pan=P+(-1, 0, 1), sus=4, bits=8, crush=8)

d1 >> play('xn', sample=[0, PRand(7)]).every(6, "stutter", 4, dur=3).every(8, "amen")
d2 >> play('[oo]', amp=linvar([0,1,0], [2, 0, 2]), bits=4, rate=2, crush=4, room=0.5, pan=[-1,1])
d3 >> play(Pvar(["  u ", "  u u"], 8), dur=PDur(var([4,5], 8), 8))
d4 >> play('funky', rate=4*PRand([1, 1.5, 1.25]), dur=1/4, pan=PStep(6, P*(-1,1)))

d2 >> play("< s>(X )( X)O ")

c1 >> play("#", dur=8, bits=4, cut=1/4, room=1, crush=8, shape=0.5, pan=[-1, 1], 
           slide=PRand([-1]),
           chop=320
           )
           
s1 >> saw(PWhite(32)[:8], dur=1/6, amp=0.6)  # very nice electric sound!!!!
s1.every(8, "degrade")

b1 >> bass([0, 0.5, var([1.5, 0], [7,1])], dur=var([3,4]), oct=3, shape=2, 
            slide=PRand([-1,0,-2,-3]),
            coarse=PRand([4,8,16,24])*PRand([1,1.5])
            )  # strange sounds!!!!

Master().lpf = var([0, 1000], [28, 4])
Master().lpr = linvar([0.1, 1])


d_all.lpf = 00
