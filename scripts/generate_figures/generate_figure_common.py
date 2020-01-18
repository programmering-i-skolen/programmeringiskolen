import matplotlib as mpl 
import matplotlib.pyplot as plt
import os 


def figure_begin(size=(4, 2.666)):
    mpl.rc('xtick', labelsize=7)
    mpl.rc('ytick', labelsize=7)
    mpl.rc('axes', labelsize=8)
    mpl.rc('legend', fontsize=8)
    mpl.rc('figure', titlesize=8)
    mpl.rc('axes', titlesize=8)
    mpl.rc('axes', titleweight="bold")
    mpl.rc('font', family="sans-serif")
    plt.figure(figsize=size)

def figure_end():
    plt.tight_layout()

def figure_save(filename_noend):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    plt.savefig(dir_path+"/output/"+filename_noend+".pdf")