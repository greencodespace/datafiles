

# -*- coding : utf-8 -*-

#------------------------------------------------
# * file_name : scipy_1st_test_code                             
# * theme :                                    
# * kw    :                                    
# * from  :                                    
# * ref   :                                    
#------------------------------------------------

from numpy import *
from scipy import *
from pylab import *
from scipy import ndimage


print('hello_peace_world')
print('%10.5f' % 38)

def myplot(a,b,c):

    fig=plt.figure(facecolor='w');
    x=arange(a,b,c);
    plot(x,sin(x));
    show();
    del x;

if __name__ == "__main__":

    myplot(0,10,0.1);


# c

