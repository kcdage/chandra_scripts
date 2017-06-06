

from xspec import *



def FitSomeData():
    s=Spectrum("321.pi")

    m = Model(phabs*(diskbb+powerlaw))
    m.phabs.nH=0.016
    Model.showlist()
