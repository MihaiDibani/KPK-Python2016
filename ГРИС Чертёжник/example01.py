from drawman import *

A = [(-200, -150), (-200, -50), (-200, 50), (-200, 150)]
B = [(200,  -150), (200, -50), (200, 50), (200, 150)]

penup()
for point_A in A:
    for point_B in B:
        pendown()
        goto(*point_A)
        goto(*point_B)
        penup()
