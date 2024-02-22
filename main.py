import customtkinter as ctk
import Calc


root = ctk.CTk()
root.geometry("310x500")
root.title("EvoCalc")
root.resizable(False, False)



#Front end

output = ctk.CTkEntry(root,
                        width=310,
                        height=100,
                        font=("Arial", 40),
                        state="normal",
                        justify="right",
                        border_color="#4fc7ee"
                        )

output.place(x=0, y=0)

calculadora = Calc.Calculadora(output)

numpad = ctk.CTkFrame(root,
                      width=235,
                      height=310,
                      fg_color="transparent",
                      )
numpad.place(x= 0, y=190)

bt7 = ctk.CTkButton(numpad,
                    text="7",
                    width=70,
                    height=70,
                    corner_radius=30,
                    border_color="black",
                    fg_color="transparent",
                    hover_color="#393C3D",
                    font=("Arial", 17),
                    command=lambda: calculadora.bt7()
                    )
bt7.place(x=0,y=0)


bt8 = ctk.CTkButton(numpad,
                    text="8",
                    width=70,
                    height=70,
                    corner_radius=30,
                    border_color="black",
                    fg_color="transparent",
                    hover_color="#393C3D",
                    font=("Arial", 17),
                    command=lambda: calculadora.bt8()
                    )
bt8.place(x=83,y=0)

bt9 = ctk.CTkButton(numpad,
                    text="9",
                    width=70,
                    height=70,
                    corner_radius=30,
                    border_color="black",
                    fg_color="transparent",
                    hover_color="#393C3D",
                    font=("Arial", 17),
                    command=lambda: calculadora.bt9()
                    )
bt9.place(x=158,y=0)

bt4 = ctk.CTkButton(numpad,
                    text="4",
                    width=70,
                    height=70,
                    corner_radius=30,
                    border_color="black",
                    fg_color="transparent",
                    hover_color="#393C3D",
                    font=("Arial", 17),
                    command=lambda: calculadora.bt4()
                    )
bt4.place(x=0,y=75)

bt5 = ctk.CTkButton(numpad,
                    text="5",
                    width=70,
                    height=70,
                    corner_radius=30,
                    border_color="black",
                    fg_color="transparent",
                    hover_color="#393C3D",
                    font=("Arial", 17),
                    command=lambda: calculadora.bt5()
                    )
bt5.place(x=83,y=75)

bt6 = ctk.CTkButton(numpad,
                    text="6",
                    width=70,
                    height=70,
                    corner_radius=30,
                    border_color="black",
                    fg_color="transparent",
                    hover_color="#393C3D",
                    font=("Arial", 17),
                    command=lambda: calculadora.bt6()
                    )
bt6.place(x=158,y=75)

bt1 = ctk.CTkButton(numpad,
                    text="1",
                    width=70,
                    height=70,
                    corner_radius=30,
                    border_color="black",
                    fg_color="transparent",
                    hover_color="#393C3D",
                    font=("Arial", 17),
                    command=lambda: calculadora.bt1()
                    )
bt1.place(x=0,y=150)

bt2 = ctk.CTkButton(numpad,
                    text="2",
                    width=70,
                    height=70,
                    corner_radius=30,
                    border_color="black",
                    fg_color="transparent",
                    hover_color="#393C3D",
                    font=("Arial", 17),
                    command=lambda: calculadora.bt2()
                    )
bt2.place(x=83,y=150)

bt3 = ctk.CTkButton(numpad,
                    text="3",
                    width=70,
                    height=70,
                    corner_radius=30,
                    border_color="black",
                    fg_color="transparent",
                    hover_color="#393C3D",
                    font=("Arial", 17),
                    command=lambda: calculadora.bt3()
                    )
bt3.place(x=158,y=150)

bt0 = ctk.CTkButton(numpad,
                    text="0",
                    width=70,
                    height=70,
                    corner_radius=30,
                    border_color="black",
                    fg_color="transparent",
                    hover_color="#393C3D",
                    font=("Arial", 17),
                    command=lambda: calculadora.bt0()
                    )
bt0.place(x=83,y=226)

btcomma = ctk.CTkButton(numpad,
                    text=",",
                    width=70,
                    height=70,
                    corner_radius=30,
                    border_color="black",
                    fg_color="transparent",
                    hover_color="#393C3D",
                    command=lambda: calculadora.btcomma(),
                    font=("Arial", 17)

                    )
btcomma.place(x=157,y=226)

opc_up = ctk.CTkFrame(root,
                      width=310,
                      height=77,
                      fg_color="transparent",
                      )
opc_up.place(x=0,y=115)

bt_clearall = ctk.CTkButton(opc_up,
                    text="𝗔𝗖",
                    width=75,
                    height=75,
                    text_color="#a3b0f6",
                    corner_radius=30,
                    border_color="black",
                    fg_color="transparent",
                    hover_color="#393C3D",
                    font=("Arial", 20),
                    command=lambda: calculadora.ac()

                    )
bt_clearall.place(x=0,y=0)

bt_clearone = ctk.CTkButton(opc_up,
                    text="<X",
                    width=75,
                    height=75,
                    corner_radius=30,
                    border_color="black",
                    fg_color="transparent",
                    text_color="#2ec68b",
                    hover_color="#393C3D",
                    font=("Arial", 14),
                    command=lambda: calculadora.clearone()

                    )
bt_clearone.place(x=80,y=0)

bt_percent = ctk.CTkButton(opc_up,
                    text="%",
                    width=75,
                    height=75,
                    corner_radius=30,
                    border_color="black",
                    fg_color="transparent",
                    text_color="#2ec68b",
                    hover_color="#393C3D",
                    font=("Arial", 15),
                    command=lambda: calculadora.btpercent()

                    )
bt_percent.place(x=162,y=0)

bt_div = ctk.CTkButton(opc_up,
                    text="➗",
                    width=75,
                    height=75,
                    corner_radius=30,
                    border_color="black",
                    hover_color="#393C3D",
                    text_color="#2ec68b",
                    fg_color="transparent",
                    command=lambda: calculadora.btdiv()

                    )
bt_div.place(x=236,y=0)

opc_right = ctk.CTkFrame(root,
                         width=83,
                         height=300,
                        fg_color="transparent",
                        )
opc_right.place(x=229,y=191)

bt_mult = ctk.CTkButton(opc_right,
                    text="✖️",
                    width=75,
                    height=75,
                    corner_radius=30,
                    border_color="black",
                    hover_color="#393C3D",
                    text_color="#2ec68b",
                    fg_color="transparent",
                    command=lambda: calculadora.btmult()

                    )
bt_mult.place(x=9,y=0)

bt_min = ctk.CTkButton(opc_right,
                    text="➖",
                    width=75,
                    height=75,
                    corner_radius=30,
                    border_color="black",
                    hover_color="#393C3D",
                    text_color="#2ec68b",
                    fg_color="transparent",
                    command=lambda: calculadora.btmin()

                    )
bt_min.place(x=9,y=75)

bt_sum = ctk.CTkButton(opc_right,
                    text="➕",
                    width=75,
                    height=75,
                    corner_radius=30,
                    border_color="black",
                    hover_color="#393C3D",
                    text_color="#2ec68b",
                    fg_color="transparent",
                    command=lambda: calculadora.btsum()

                    )
bt_sum.place(x=9,y=150)

bt_res = ctk.CTkButton(opc_right,
                    text="🟰",
                    width=75,
                    height=75,
                    corner_radius=30,
                    border_color="black",
                    hover_color="#393C3D",
                    text_color="#2ec68b",
                    fg_color="transparent",
                    command=lambda: calculadora.btres()

                    )
bt_res.place(x=9,y=226)

letreiro = ctk.CTkFrame(master=root,
                        width=75,
                        height=90,
                        fg_color="transparent",
                        )
letreiro.place(x=0,y=420)

lb_letreiro = ctk.CTkLabel(letreiro,
                           text="𝓔𝓥𝓞",
                           font=("Arial", 25),
                           )
lb_letreiro.place(x=17,y=15)

calculadora.change_color(root, lb_letreiro)


root.mainloop()
