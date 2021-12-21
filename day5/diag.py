x1, y1 = 3, 3
x2, y2 = 1, 1

def get_range(a1, a2):
    a_range = list(range(abs(a2-a1) + 1))
    if a2 < a1:
        a_range = [ -1 * x for x in a_range]
    
    return(a_range)

diag = [(x1 + x_inc, y1 + y_inc) for (x_inc, y_inc) in zip(get_range(x1,x2), get_range(y1,y2)) ]

print(diag)