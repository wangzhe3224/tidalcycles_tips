Scale.default.set(Scale.blues, tuning=Tuning.just)

chords = var([0, 6, 2, 5])

s1 >> prophet([7,6,4,2, b2.pitch + var([0,2], 8)], dur=[1,2,2,4], blur=1.5, pan=var([-1, 1]))

s2 >> piano(chords, dur=EuclidsAlgorithm(3, 8), sus=4, amp=0.4)

b1 >> bass(chords-var([0, 2, 4]), dur=PDur(6,10), amp=0.8, cutoff=linvar([100, 8000], 30))
b2 >> sawbass(chords, dur=PDur(5,8), cutoff=linvar([100, 8000], 30),
     amp=linvar([0.5, 1], 20), fmod=PWhite(-1,1))

p1 >> blip(chords + var([4,6,7], [7, 1]))

p2 >> prophet(P[3,2, chords].loop(4) | P[4,4,4,4], dur=1/4, amp=1.2)
p3 >> pads(p2 - 5, dur=8, room=1, coarse=16, chop=1, lpf=linvar([400, 800], 24), lpr=linvar([0.1, 1], 14))
p1.amp=0.7
p4 >> blip(fmod=4, vib=12, slide=-1, oct=7, dur=12, pan=P+(-1, 0, 1), sus=4, bits=8, crush=8, amp=0.1)
p5 >> space(s1+var([0, 4]), dur=PRange(4, 8)).sometimes("reverse")

print(Scale.names())

b3 >> bell(chords - PRand(0, 8), dur=var([2,4,8]), pan=var([-1, 1])).every(2, 'reverse')

d1 >> play('  --')
d2 >> play('x   ')
d3 >> play('   H', dur=1)
d4 >> play('  [Oo][ppp]', dur=1, amp=var([0, 1.0], [32, 4])).every(6, "jump", cycle=8)
d5 >> play("funky", rete=2).every(4, "amen").every(4, "reverse")
d6 >> play("[Xx]   ", amp=var([0, 1], [8, 1]), room=3, size=2, sus=1)  # live a heart beat!


Master().lpf = var([0, 800], [32, 4])

Master().hpf = var([0, 2000], [60, 3])
