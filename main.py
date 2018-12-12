from count import counter
from timer import allot
from display import disp

#Getting count values of each road
r1_count = counter("assets/video1.mp4", "Road 1")
r2_count = counter("assets/video2.mp4", "Road 2")
r3_count = counter("assets/video3.mp4", "Road 3")
r4_count = counter("assets/video4.mp4", "Road 4")

# Getting time allotment for each road

r1_time = allot(r1_count)
r2_time = allot(r2_count)
r3_time = allot(r3_count)
r4_time = allot(r4_count)

# disp()
disp(r1_time,r2_time,r3_time,r4_time)

