# %%
def whileexcercise():
    count = 0
    while count < 10:
        count += 1
        print ("Xuat \t"+ str(count) +"\t Byebyeworld")

def whileexcercise1():
    count = 0
    while count < 10:
        count += 1
        print ("Xuat \t"+ str(count) +"\t Byebyeworld")
    else:
        print("ketthuc while")
        
def breakandcontinue():
    text = input("nhap vao mot chuoi: ")
    answer = False
    index = 0
    while index < len(text):
        if text[index] == 'a' or text[index] == "A":
            answer = True
            break
        index += 1
        if answer:
            print("Chuoi chua ky tu a")
    else:
        print("Chuoi ko chua ky tu a")

def vehinhvuong():
    import turtle
    a = int(input("Nhap do dai cac canh cua hinh vuong: "))
    t = turtle.Turtle()
    t.hideturtle()
    t.pencolor("red")
    edge = 0
    while edge < 4:
        #ve 1 canh cua hinh vuong
        t.forward(a)
        t.right(90)
        edge += 1
        turtle.exitonclick

def turtleexcersiseliterally():
    #Dinh dang
    import turtle
    import random as r
    t= turtle.Turtle()
    t.shape("classic")
    t.hideturtle()
    t.pensize(3)
    t.color("blue")
    t.speed(1)
    t.penup()
    t.goto(-400,0)
    t.showturtle()
    #dieukienve
    count = 0
    while count < 10:
        #sinh hai gia tri ngau nhien
        down = r.randint(20,50)
        up =r.randint(20, 50) #randint = random interger = so thuc ngau nhien trong khoang
        t.pendown
        t.penup()
        t.forward(up)
        count += 1
    turtle.exitonclick

def whileextraexcersise():
    count = 0;
    while count < 7:
        a = str(input("Nhap mot chuoi"))
        count += 1
        if a != str("python"):
            print("ko dc")
        else:
            print("dc")
            break
def whiletrueexcersise():
    count = 0;
    while True:
        count += 1
        a = (str(input("Nhap chuoi Python: ")))
        if a == str("python"):
            print("Dung")
            break
        elif a != str("python"):
            print("ko dung")
        if count == 7:
            print("staph plz, input as instructed above.")
            break
if __name__ == "__main__":
    #whileexcercise1()
    #breakandcontinue()
    #vehinhvuong()
    #turtleexcersiseliterally():
    #whileextraexcersise()
    #whiletrueexcersise()