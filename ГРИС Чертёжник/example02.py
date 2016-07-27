from drawman import *

A = [(-200, 0), (+200, 0),
     (-120, 120), (+120, 120),
     (-120, -120), (+120, -120)]
penup()
for i in range(len(A)-1):
    for k in range(i+1, len(A)):
        goto(*A[i])
        pendown()
        goto(*A[k])
        penup()
