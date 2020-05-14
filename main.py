from MFCC import MFCC
from play import Play
import time
import sys
from sklearn import neighbors
# from Vector import mfcc_vectors
from Vector import Vector
import numpy as npy
if __name__ == "__main__":
    for x in range(0,30):
        mfcc = MFCC('vibration.wav')
        play = Play()
        play.start()
        time.sleep(0.14)
        mfcc.start()
        mfcc.join()
        play.join()
        time.sleep(1)
    vectors = npy.array(Vector.mfcc_vectors)
    for x in range(1,31):
        for y in range(0,2000):
            vectors[x,y] = (vectors[x,y] - npy.min(vectors[1:31,y]))/(npy.max(vectors[1:31,y]) - npy.min(vectors[1:31,y]))





    # mfcc.terminate()
    # play.terminate()
    # sys.exit(0)


