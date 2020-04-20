from Script.oscilloscope.Oscilloscope import Oscilloscope

if __name__ == '__main__':
    dc11202e = Oscilloscope(100, 1, "rigol", "kyiv", 8000, 2)
    port1c15 = Oscilloscope(100, 1, "fnirsi")
    v680 = Oscilloscope()
    for oscillolist in [dc11202e,port1c15,v680]:
        print(oscillolist)
    print(Oscilloscope.getyear())