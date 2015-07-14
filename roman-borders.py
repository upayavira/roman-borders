#!/usr/bin/python

import math
import sys


WIDTH=1000
HEIGHT=1414
MARGIN=20
THICKNESS=20
M=MARGIN
T=THICKNESS
H=HEIGHT
W=WIDTH
R="black"
G="black"
C1=T*2
C2=T*3
CENTRE="%s, %s" % (M+T*2.5, M+T*2.5)


def corner(r):
    line(r, M, M, T*3, 0, R)
    line(r, M, M, 0, T*3, R)
    line(r, M+T*3, M, 0, T*2, R)
    line(r, M+T, M+T, 0, T, R)
    line(r, M+T, M+T, T, 0, R)
    line(r, M+T*2, M+T, 0, T, R)
    line(r, M+T, M+T*2, T*3, 0, R)
    line(r, M, M+T*3, T*4, 0, R)
    line(r, M, M+T*4, T*2, 0, R)
    line(r, M+T, M+T*5, T, 0, R)
    line(r, M, M+T*4, 0, T, R)
    line(r, M+T*2, M+T*3, 0, T*2, R)
    line(r, M+T*3, M+T*3, 0, T*2, R)
    line(r, M+T*3, M+T*4, T, 0, R)
    line(r, M+T*3, M+T*5, T*2, 0, R)
    line(r, M+T*4, M, 0, T*4, R)
    line(r, M+T*5, M+T, 0, T*4, R)
    line(r, M+T*4, M, T, 0, R)


def side(d, r=""):
    line(r, M, M+T*5, 0, d/2-M-T*6-C1/2, G)
    line(r, M+T, M+T*5, 0, d/2-M-T*6-C2/2-T/4, G)
    line(r, M+T*2, M+T*5, 0, d/2-M-T*6-C2/2-T/4, G)
    line(r, M+T*3, M+T*5, 0, d/2-M-T*6-C1/2, G)
    arc(r, M, d/2, C1, 0, 20) # INNER
    arc(r, M, d/2, C2, 20, 30) # OUTER

    arc(r, M, d/2, C1, 50, 180) # INNER
    arc(r, M, d/2, C2, 50, 160) # OUTER

    arc(r, M+T*3, d/2, C1, 180, 180+20) # INNER
    arc(r, M+T*3, d/2, C2, 200, 200+10) # OUTER

    arc(r, M+T*3, d/2, C1, 180+50, 0) #INNER
    arc(r, M+T*3, d/2, C2, 200+30, 340) # OUTER

    line(r, M, d-M-T*5, 0, -(d/2-M-T*6-C1/2), G)
    line(r, M+T, d-M-T*5, 0, -(d/2-M-T*6-C2/2-T/4), G)
    line(r, M+T*2, d-M-T*5, 0, -(d/2-M-T*6-C2/2-T/4), G)
    line(r, M+T*3, d-M-T*5, 0, -(d/2-M-T*6-C1/2), G)


def box():
    rect(M,M, W-M*2, H-M*2)


def polar_to_cartesian(centerX, centerY, radius, angleInDegrees):
  angleInRadians = (angleInDegrees-90) * math.pi / 180.0;
  return centerX + (radius * math.cos(angleInRadians)), centerY + (radius * math.sin(angleInRadians))


def arc(r, x, y, radius, startAngle, endAngle):

    start = polar_to_cartesian(x, y, radius, endAngle);
    end = polar_to_cartesian(x, y, radius, startAngle);

    arcSweep = "0" if (endAngle - startAngle) <= 180 else "1"

    d = " ".join(["M", str(start[0]), str(start[1]),
        "A", str(radius), str(radius), str(0), str(arcSweep), "0", str(end[0]), str(end[1])
    ])

    print >>f, '<path transform="%s" id="arc1" fill="none" stroke="black" stroke-width="2" d="%s"/>' % (r, d)


def line(r, x, y, w, h, colour="black"):
    print >>f, '<line x1="%s" y1="%s" x2="%s" y2="%s" style="stroke:%s;stroke-width:2" transform="%s" />' % (x, y, x+w, y+h, colour, r)


def rect(x, y, w, h):
    print >>f, '<rect x="%s" y="%s" width="%s" height="%s" fill="none" stroke="red" stroke-width="4"/>' % (x, y, w, h)


def svg_start():
    print >>f, '<svg width="%s" height="%s">' % (W, H)


def svg_end():
    print >>f, "</svg>"


def border(filename):
    global f
    f=open(filename, "w")
    #box()
    svg_start()

    corner("")
    corner("translate(%s, 0) rotate(90, %s)" % (W-T*5-M*2, CENTRE))
    corner("translate(0, %s) rotate(270, %s)   " % (H-M*2-T*5, CENTRE))
    corner("translate(%s, %s) rotate(180, %s)   " % (W-M*2-T*5, H-M*2-T*5, CENTRE))

    side(H)
    side(H, "translate(%s, 0)" % (W-T*3-M*2))
    side(W, "translate(%s, 0) rotate(90, %s)" % (W-T*5-M*2, CENTRE))
    side(W, "translate(0, %s) rotate(-90, %s)" % ((H-T*5-M*2), CENTRE))

    svg_end()

if __name__ == "__main__":
    if len(sys.argv)==1:
        border("roman-borders.svg")
    else:
        border(sys.argv[1])


