def get_data():
    x1,y1=map(float,input().split())
    x2,y2=map(float,input().split())
    
    return x1,y1,x2,y2

def get_line(a1,b1,a2,b2):
    if a1==a2:
        rst=f"x={a1}"
        return rst
    
    elif b1==b2:
        rst=f"y={b1}"
        return rst

    else:   
        slp=(b1-b2)/(a1-a2)
        y_i=b1-slp*a1

        rst=f'y = {slp}x +({y_i})'
        return rst



x1,y1,x2,y2=get_data()
line=get_line(x1,y1,x2,y2)
print(line)
