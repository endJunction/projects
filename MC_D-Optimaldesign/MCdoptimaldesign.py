import pyDOE2 as doe
import numpy as np

def doptimal(df,size,N):
    full=doe.ff2n(df)
    X=np.array([full[0]])
    design=[0]
    for i in np.arange(1,size):
        X=np.append(X,[full[i]],axis=0)
        design.append(i)
    X=np.c_[  np.ones(size),X ]
    Xnew=X.copy()
    H=np.dot(X.transpose(),X)
    Hnew=np.dot(Xnew.transpose(),Xnew)
    H_det=np.linalg.det(H)
    Hnew_det=np.linalg.det(Hnew)
    switch=False
    designnew=design.copy()
    for i in np.arange(0,N):
        random=np.random.randint(len(full))
        random2=np.random.randint(size)
        if random not in design:
            designnew[random2]=random
            Xnew[random2,1:]=full[random]
            switch=True
        if switch==True:
            Hnew=np.dot(Xnew.transpose(),Xnew)
            Hnew_det=np.linalg.det(Hnew)
            switch=False
        if Hnew_det>H_det:
            X=Xnew.copy()
            design=designnew.copy()
            H_det=Hnew_det.copy()
            print(i,H_det)
    return np.delete(X,0,1)

#print(X)
#print(design)