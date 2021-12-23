# %%
def greeting(name):
    print("hello, " + name)
    
person1 = {
  'name': "John",
  'age': 36,
  'country': "Norway",
  'job': "Engineer"
}
def greet(name):
    """
    Hàm này in ra dòng chào
    tên người được truyền vào hàm
    :param name: Tên người
    """
    print("Bye bye!, "+name)
    print(greet.__doc__)

def hamtrong():
    pass
def timgiatrilonnhatcuaso(a,b,c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c
def timgiatrinhonhat(a,b,c):
    if a<b:
        if a<c:
            return a
        else:
            return c
    else:
        if b<a:
            return b
        else:
            return c