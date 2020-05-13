from MFCC import MFCC
from play import Play
import time
import sys
if __name__ == "__main__":
    mfcc = MFCC('vibration.wav')
    play = Play()
    play.start()
    time.sleep(0.14)
    mfcc.start()
    # time.sleep(0.1)

    mfcc.join()
    play.join()
    # mfcc.terminate()
    # play.terminate()
    # sys.exit(0)


