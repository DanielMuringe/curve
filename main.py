from numpy.linalg import solve as np_linalg_solve
from numpy import array as np_array
from string import join as str_join

class plotted_curve():
    def __init__(self,points):
        self.points = np_array(points)
    
    def constants(self):
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
    
    def __str__(self):
        superscript = []
        line        = []

        i = 0
        for constant in self.constants():
            constant    = round(constant,2)
            cond        = i<=0 or constant<0
            plus_space  = '' if cond else ' '
            plus        = '' if cond else '+'
            const_space = ' '*(len(str(constant)))
            
            superscript.append(f'{plus_space}{const_space} {i}')
            line.append(f'{plus}{constant}x ')

            i += 1
            
        superscript = str_join(superscript)
        line        = str_join(line)
        
        eq_str = f'''
{superscript}
{line}'''
        return eq_str

