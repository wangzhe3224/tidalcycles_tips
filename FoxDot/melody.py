var.chords = var(
    PChain({
        0: [2,3],
        2: [0,5],
        3: [0,5],
        5: [3]
        })
    )

# s1 >> soprano([7,6,4,2,0], dur=[2,2,2,2,8])
s1 >> viola([7,6,4,2, b2.pitch + var([0,2], 8)], dur=[2,2,2,2,8], blur=1.5, pan=var([-1, 1]))

p1 >> blip([var.chords,4,6,7][:6], dur=PDur(3,8)*2)  # P[1.5, 1.5, 1.0]
p2 >> bell(var.chords + var([(0,2), (2,4)]), dur=[1, 1/2], amp=1/3)
p3 >> prophet(P[3,2, var.chords].loop(4)|P[4,4,4,4], dur=1/4, 
              hpf=linvar([0,5000], [16,0]),
              hpr=linvar([0.1, 1], 25),
              formant=PRand(4)[:16])
              
p_all.stop()

s_all.stop()

# d 
d1 >> play("<x[  [sn]]>< h><   (yt+)>", sample=2, dur=1).every(2, "reverse")
d2 >> play("ss  ", dur=1/2, sample=2)
d3 >> play("<  o ><   i>", sample=-2, dur=1/2, echo=var([0,0.5], [6, 2])).every([6,2], "mirror")
d4 >> play("K", sample=[1,2,3], dur=PDur(3,8,[0,2]), amp=1/2)
d5 >> play("funky", rete=2).every(4, "amen").every(4, "reverse")
d6 >> play("#", dur=32, room=1)

d_all.lpf = var([0, 500], [28, 4])
d_all.blur = 1.5

d_all.stop()

# bass
b1 >> sawbass(var.chords, dur=PDur(5,8), cutoff=linvar([100, 8000], 30),
     amp=linvar([0.5, 1], 20), fmod=PWhite(-1,1))
b2 >> bass(b1.pitch, dur=8, rate=5, room=1).spread()

b_all.stop()

# fmod: This adds a value to the frequency used to generate a note, but only in one of the channels.
# hpf : High-pass filter
# hpr : 
# var(): allows you to create values that change over time.
# format: filter. 1-7
# spead: 



print(PChain({
        0: [2,3],
        2: [0,5],
        3: [0,5],
        5: [3]
        }))



