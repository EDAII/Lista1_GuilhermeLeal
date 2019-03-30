from data import DataSeq
from bubble import BubbleSort
from insertion import InsertionSort
from merge import MergeSort


import argparse
parser=argparse.ArgumentParser(description="Sort Visulization")
parser.add_argument('-l','--length',type=int,default=64)
parser.add_argument('-i','--interval',type=int,default=1)
parser.add_argument('-t','--sort-type',type=str,default='BubbleSort', 
                                    choices=["BubbleSort","InsertionSort","MergeSort","SelectionSort"])
parser.add_argument('-r','--resample', action='store_true')
parser.add_argument('-s','--sparse', action='store_true')

args=parser.parse_args()

if __name__ == "__main__":
    MAXLENGTH=1000
    Length=    args.length if args.length<MAXLENGTH else MAXLENGTH
    Interval=  args.interval
    SortType=  args.sort_type
    Resampling=args.resample
    Sparse=    args.sparse
  
    try:
        SortMethod=eval(SortType)
    except:
        print("Busca nao encontrada %s !"%SortType)
        exit()

    ds=DataSeq(Length, time_interval=Interval, sort_title=SortType, is_resampling=Resampling, is_sparse=Sparse)
    ds.Visualize()
    ds.StartTimer()
    SortMethod(ds)
    ds.StopTimer()
    ds.SetTimeInterval(0)
    ds.Visualize()