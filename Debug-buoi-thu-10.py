# %%
def vehinhvuongvonglapfor(a,b):
    import turtle
    wn =turtle.Screen()
    wn.bgcolor("cyan")
    wn.title("square")
    pen = turtle.Turtle()
    pen.speed(0)
    
    pen.fillcolor("purple")
    pen.begin_fill()
    for i in range (4):
        pen.fd(a)
        pen.rt(b)
    pen.end_fill()
    
    turtle.exitonclick

if __name__ == "__main__":
    vehinhvuongvonglapfor(200,90)


# %%
def sudungnestedloopdeve(a,b):
    import turtle
    wn = turtle.Screen()
    wn.title("Something")
    wn.bgcolor("black")
    t = turtle.Turtle()
    t.speed(0)
    t.fillcolor("yellow")
    t.begin_fill()
    for i in range (1,100):
        for i in range (1,6):
            t.lt(a)
            t.fd(b)
        t.lt(5)
    t.end_fill()
    
    turtle.exitonclick
if __name__ == "__main__":
    sudungnestedloopdeve(144, 200)

# %%
#FizzBuzz
class fizzbuzz:

    def main():
        a, b = [int(a) for a in input("Nhap hai so bat ky: ").split()]
        if a >= b:
            print ("Nhap lai")
        else:
            print ("So be nhat la: ", a)
            print ("So lon nhat la: ", b)
            for i in range (a,b):
                if i%3==0 and i%5==0:
                    print("fizzbuzz", i)
                    continue
                elif i%3==0:
                    print("fizz", i)
                    continue
                elif i%5==0:
                    print("buzz", i)
                    continue
            else:
                print ("So khong thoa man dieu kien", i)    
    if __name__ == "__main__":
        main()

            


# %%
#21games


# %%
def vehinhvnnsnhkytu():
    char = input('Your char?: ')
    width = int(input('Width?: '))
    height = int(input('Height?: '))

    for i in range(1,height + 1):
        print_str = ''
        for j in range(1,width + 1):
            if i == 1 or i == height:
                print_str += char
            else:
                if j == 1 or j == width:
                    print_str += char
                else:
                    print_str += ' '
        print(print_str)
if __name__ == "__main__":
    vehinhvnnsnhkytu()


