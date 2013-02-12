from __future__ import division

def resistance(vr, i):
  return (vr/i)

def resistance_heat(vr, i, f, dt):
  return ((vr/i) - (f*dt))
