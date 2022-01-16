
from typing import Sized


def page(m , n) :
    i=1
    j=1

    for i in range (m):
        for j in range (n) :
            if j % 2 == 0 :
             print("*" , end = '')
            else :
                print("#" , end = '')
        print("\n")


page(6,10)

page(4,6)
