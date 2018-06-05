#encoding=utf8
import sys 

def func1(i, j):
    x = -(i - j) * 64
    y = -(i + j) * 32
    print("x = " + str(x) + ", y = " + str(y))

# func1(0, 1)

str = "0,53 279,97 274,209 64,272 -155,250 -253,169 -224,88"
w = 584
h = 569
def func2(w,h,str):
    points = str.split(" ")
    for pstr in points:
        x = int(pstr.split(",")[0]) + w/2
        y = int(pstr.split(",")[1]) + h/2
        print(x,y)

func2(w,h,str)


# if __name__ == "__main__":
    # func(1,2)
    # if len(sys.argv) > 2: 