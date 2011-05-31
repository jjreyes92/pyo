#! /usr/bin/env python
# encoding: utf-8
"""
Performs the cross-synthesis of two sounds.
created by belangeo, 31-05-2011

"""
from pyo import *

s = Server().boot()

snd1 = SfPlayer(SNDS_PATH+"/transparent.aif", loop=True)
snd2 = FM(carrier=[75,100.03,125.5,149], ratio=[.99,.505], index=20, mul=.4).mix(2)

size = 1024
olaps = 4

fin1 = FFT(snd1, size=size, overlaps=olaps)
fin2 = FFT(snd2, size=size, overlaps=olaps)

# get the magnitude of the first sound
mag = Sqrt(fin1["real"]*fin1["real"] + fin1["imag"]*fin1["imag"], mul=10)
# scale `real` and `imag` parts of the second sound by the magnitude of the first one
real = fin2["real"] * mag
imag = fin2["imag"] * mag

fout = IFFT(real, imag, size=size, overlaps=olaps)
ffout = fout.mix(2).out()

# change of fft size must be done on all fft and ifft objects at the same time!
def setSize(x):
    fin1.size = x
    fin2.size = x
    fout.size = x

s.gui(locals())

