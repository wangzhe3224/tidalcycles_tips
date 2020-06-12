chords = var([0, 4, 5, 3])
p1 >> piano(chords + (0, 2, 4), dur=4, sus=2)
p2 >> piano(chords + [0, 2, 3, 4, 7, 9], dur=1/4, sus=4, ).every(4, "reverse").every(8, "shuffle")

p3 >> pads(chords+var([0, 2]), dur=PDur(3,8), chop=4, sus=2, amp=0.3).sometimes("shuffle")

s2 >> saw(p2.pitch, amp=0.6).stop()

s1 >> space(p1.pitch, amp=0.8, sus=2, dur=1, chop=1, )

d1 >> play("- [--] ")
d2 >> play("[Xx]   ", amp=var([0, 1], [8, 1]), room=3, size=2, sus=1)  # live a heart beat!


print(SynthDefs)


Master().lpf = var([0, 1000], [28 ,4])

p_all.stop()
d_all.stop()
s_all.stop()
