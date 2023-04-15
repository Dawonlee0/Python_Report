# 개념 확인 과제 7.6

def aa(N,a,b):
    for i in range(a,b):
        print(f'{i} x {N} = {(i) * (N):2d}', end ='      ')

def bb(N,a,b):
    for i in range(1,2):
        aa(N,a,b)
        
def cc(a,b):
    for i in range(1,10):
        bb(i,a,b)
        print()
        
cc(2,6)      
print()                                                                                     
cc(6,10)      
