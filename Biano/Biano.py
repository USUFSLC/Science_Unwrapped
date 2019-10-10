from test import *


def fruitSong():
    while True:
        if getTouch0():
            playC()
        if getTouch1():
            playD()
        if getTouch2():
            playE()
        if getTouch3():
            playF()
        if getTouch4():
            playG()
        if getTouch5():
            playA()
        if getTouch6():
            playB()
        if getTouch7():
            playHighC()
        if getTouch8():
            playAux0
        if getTouch9():
            playAux1
        if getTouch10():
            playAux2
        if getTouch11():
            playAux3


def main():
    fruitSong()


if __name__ == "__main__":
    main()
