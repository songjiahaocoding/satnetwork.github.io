import math
import statistics


arr = []
NUM_ORBITS = 40
for line in open('level_0_best_motif.txt'):
    orbs = line.split(",")
    tmp = abs(math.floor(eval(orbs[0]) / NUM_ORBITS)-math.floor(eval(orbs[1]) / NUM_ORBITS))
    arr.append(min(tmp, 40-tmp))

print(min(arr), max(arr), statistics.mean(arr), statistics.median(arr))