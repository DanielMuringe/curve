from numpy.linalg import solve as np_linalg_solve
from numpy import array as np_array



class plotted_curve():
    def __init__(self,points):
        self.points = points
    
    def eq(self):
        A = []
        B = []

        for point in self.points:
            x,y = point

            row = []
            for i in range(len(self.points)):
                row.append(x**i)
            A.append(row)
            B.append(y)
        
        A = np_array(A)
        B = np_array(B)

        X = np_linalg_solve(A,B)
        return X