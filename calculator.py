from tkinter import *
import math 
root = Tk()
root.geometry("350x300+450+150")
root.title("calculator")
pole=Label(root)
pole.config(text="",
    width=38,
    bg='grey',
    fg='green',
    borderwidth=3,
    justify=RIGHT,
    font=40
    )
def clear_one():
    vyraz = pole.cget("text")
    new_vyraz = vyraz[:-1]
    pole.config(text=new_vyraz)
num = 0
num1 = 0
num2 = 0
symbol = ""
duzhki_count = 0
def display(b_num):
    global num,num1,num2,symbol,duzhki_count
    vyraz = pole.cget("text")
    if b_num == "temples" and duzhki_count == 0:
        b_num= "("
        duzhki_count+=1
    elif b_num == "temples" and duzhki_count >0:
        b_num= ")"
        duzhki_count-=1
    num = b_num
    before = vyraz
    curent_n = str(before) + str(b_num)
    pole.config(text=str(curent_n))
    
def convert():
    vyraz = pole.cget("text")
    moves = ["=","+","-","/","*"]
    duzhki = ["(",")"]
    tokens = []
    current_num = ""
    for sym in vyraz:
        if sym not in moves and sym not in duzhki and sym.isdigit()== False and sym !="." :
            raise ValueError
        print(f"CONVERT DEBUG: current_sym:{sym},current_num:{current_num}")
        print(f"tokens:{tokens}")
        if sym in duzhki:
            if current_num:
                tokens.append(current_num)
            tokens.append(sym)
            current_num = ""
        elif sym.isdigit() or sym == ".":
            current_num += sym
        elif sym in moves:
            if current_num:
                tokens.append(current_num)
                current_num = ""
            tokens.append(sym)
    if current_num:
        tokens.append(current_num)
    print(current_num) 
    print(tokens)
    prioritety(tokens)
    
def prioritety(spis):
    num_1 = 0
    symbol = ""
    num_2 = 0
    syms = [0,1,2,3,4,5,6,7,8,9]
    operators = ["=","+","-","/","*","(",")"]
    if len(spis) == 1:
        pole.config(text=spis[0])
        return spis[0]
    else:
        open_d = None
        close_d = None
        d_ind = []
        for i in range(len(spis)):
            sym = spis[i]
            if sym == "(":
                d_ind.append(i)
            elif sym == ")":
                if not d_ind:
                    raise ValueError("не закрита дужка")
                open_d = d_ind.pop()
                close_d = i
                in_vyraz = spis[1+open_d:close_d]
                in_res = prioritety(in_vyraz)
                new_tokens = spis[:]
                new_tokens[open_d:close_d+1] = [str(in_res)]
                print(f"new_tokens={new_tokens},in_res={in_res}")
                print(f"sym={sym},open={open_d},close={close_d}")
                return prioritety(new_tokens)
        for i in range(len(spis)):
            sym = spis[i]
            if sym == "-" and i == 0:
                if i + 1 > len(spis):
                    raise ValueError("неправильний вираз")
                next_to_unar = float(spis[i+1])
                result_val = -next_to_unar
                new_tokens = spis[:i] + [str(result_val)] + spis[i+2:]
                return prioritety(new_tokens)
            elif sym == "-" and i > 0 and spis[i-1] in operators:
                next_to_unar = float(spis[i+1])
                result_val = -next_to_unar
                new_tokens = spis[:i] + [str(result_val)] + spis[i+2:]
                return prioritety(new_tokens)
        for i in range(len(spis)):
            sym = spis[i]
            if sym == "*" or sym == "/":
                num_1 = float(spis[i-1])
                num_2 = float(spis[i+1])
                half_res = calculate(num_1,sym,num_2)
                new_tokens = spis[:]
                new_tokens[i-1:i+2] = [str(half_res)]
                print(half_res)
                print(new_tokens)
                return prioritety(new_tokens)
        for i in range(len(spis)):
            sym = spis[i]
            if sym == "+" or sym == "-":
                num_1 = float(spis[i-1])
                num_2 = float(spis[i+1])
                half_res = calculate(num_1,sym,num_2)
                new_tokens = spis[:]
                new_tokens[i-1:i+2] = [str(half_res)]
                print(half_res)
                print(new_tokens)
                return(prioritety(new_tokens))
    try:
        return float(spis[0])
    except (ValueError, IndexError):
        raise ValueError
    
def calculate(num1,symbol,num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
        result = 0
        if symbol=="+":
            result = num1+num2
        elif symbol=="-":
            result = num1-num2
        elif symbol=="/":
            if num2 == 0:
                raise ZeroDivisionError
            else:
                result = num1/num2
        elif symbol=="*":
            result = num1*num2
        if result % 1 == 0:
            result = int(result)
    except ZeroDivisionError:
        result = "ділення на 0"
    except ValueError:
        result="неправильно введені числа"
    except Exception as e:
        result = f"помилка: {e}"
    finally:
        return result
        pole.config(text=result)
def clear():
    pole.config(text="")
zero=Button(root,text="0",width=6,relief=GROOVE,command=lambda: display(0))
zero.place(x=10,y=180)
one=Button(root,text="1",width=6,relief=GROOVE,command=lambda: display(1))
one.place(x=10,y=140)
two=Button(root,text="2",width=6,relief=GROOVE,command=lambda: display(2))
two.place(x=70,y=140)
three=Button(root,text="3",width=6,relief=GROOVE,command=lambda: display(3))
three.place(x=130,y=140)
four=Button(root,text="4",width=6,relief=GROOVE,command=lambda: display(4))
four.place(x=10,y=100)
five=Button(root,text="5",width=6,relief=GROOVE,command=lambda: display(5))
five.place(x=70,y=100)
six=Button(root,text="6",width=6,relief=GROOVE,command=lambda: display(6))
six.place(x=130,y=100)
seven=Button(root,text="7",width=6,relief=GROOVE,command=lambda: display(7))
seven.place(x=10,y=60)
eight=Button(root,text="8",width=6,relief=GROOVE,command=lambda: display(8))
eight.place(x=70,y=60)
nine=Button(root,text="9",width=6,relief=GROOVE,command=lambda: display(9))
nine.place(x=130,y=60)
point=Button(root,text=".",width=6,relief=GROOVE,command=lambda: display('.'))
point.place(x=70,y=180)
equal=Button(root,text="=",width=6,relief=GROOVE,command=convert)
equal.place(x=130,y=180)
plus=Button(root,text="+",width=6,relief=GROOVE,command=lambda: display('+'))
plus.place(x=190,y=180)
minus=Button(root,text="-",width=6,relief=GROOVE,command=lambda: display('-'))
minus.place(x=190,y=140)
mnozh=Button(root,text="*",width=6,relief=GROOVE,command=lambda: display('*'))
mnozh.place(x=190,y=100)
dil=Button(root,text="/",width=6,relief=GROOVE,command=lambda: display('/'))
dil.place(x=190,y=60)
delete=Button(root,text="AC",width=6,relief=GROOVE,command=clear)
delete.place(x=250,y=60)
sqrt=Button(root,text="sqrt",width=6,relief=GROOVE)
sqrt.place(x=250,y=100)
del_one=Button(root,text="<-",width=6,relief=GROOVE,command=clear_one)
del_one.place(x=250,y=140)
duzhki=Button(root,text="( )",width=6,relief=GROOVE,command=lambda: display("temples"))
duzhki.place(x=250,y=180)
pole.place(x=0,y=0,height=40)
root.mainloop()
