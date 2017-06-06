import numpy as np
import scipy as sp
import matplotlib.pyplot as plt






def PlotSpectra():

    
    
    f=np.loadtxt('321bin.txt')

    f_pr = np.transpose(f)
 
  

    counts = f_pr[3]

    energy=f_pr[0]

  
    
    plt.plot(energy, counts, 'g')

    plt.ylabel('Normalized Counts s-1 chan-1')
    plt.xlabel('Channel')
    

    plt.show()
   
 
    



def BinFit(In1, In2, BinNo=200):


    vEnergy=In1
    vCounts=In2

    BinMin=np.min(vEnergy)
    BinMax=np.max(vEnergy)

    BinBoundaries = np.logspace(-4,2, BinNo)

    bins=BinBoundaries

    digitized=np.digitize(vCounts, BinBoundaries)

    bin_means_count = [vCounts[digitized == i].mean() for i in range(1, len(bins))]
    bin_means_energy= [vEnergy[digitized == i].mean() for i in range(1, len(bins))]
    


    return(bin_means_energy, bin_means_count)
