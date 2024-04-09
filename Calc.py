import random

class Calculadora:

    def __init__(self, entry):
        self._limite = 13
        self.divzero = "N/P div by 0"
        self.erro = "Erro"
        self._entry = entry


    def change_color(self,  root, lb_letreiro):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        color = f"#{r:02x}{g:02x}{b:02x}"
        lb_letreiro.configure(text_color=color)
        root.after(600, self.change_color, lb_letreiro, root)

    # 0
    def bt0(self):
        if self.divzero in self._entry.get() or self.erro in self._entry.get():
            self._entry.delete(0, "end")
        if len(self._entry.get()) < self._limite:
            self._entry.insert(0+len(self._entry.get()), "0")


    # 1
    def bt1(self):
        if self.divzero in self._entry.get() or self.erro in self._entry.get():
            self._entry.delete(0, "end")
        if len(self._entry.get()) < self._limite:
            self._entry.insert(0+len(self._entry.get()), "1")


    # 2
    def bt2(self):
        if self.divzero in self._entry.get() or self.erro in self._entry.get():
            self._entry.delete(0, "end")
        if len(self._entry.get()) < self._limite:
            self._entry.insert(0+len(self._entry.get()), "2")


    # 3
    def bt3(self):
        if self.divzero in self._entry.get() or self.erro in self._entry.get():
            self._entry.delete(0, "end")
        if len(self._entry.get()) < self._limite:
            self._entry.insert(0+len(self._entry.get()), "3")


    # 4
    def bt4(self):
        if self.divzero in self._entry.get() or self.erro in self._entry.get():
            self._entry.delete(0, "end")
        if len(self._entry.get()) < self._limite:
            self._entry.insert(0+len(self._entry.get()), "4")


    #  5
    def bt5(self):
        if self.divzero in self._entry.get() or self.erro in self._entry.get():
            self._entry.delete(0, "end")
        if len(self._entry.get()) < self._limite:
            self._entry.insert(0+len(self._entry.get()), "5")


    # 6
    def bt6(self):
        if self.divzero in self._entry.get() or self.erro in self._entry.get():
            self._entry.delete(0, "end")
        if len(self._entry.get()) < self._limite:
            self._entry.insert(0+len(self._entry.get()), "6")


    # 7
    def bt7(self):
        if self.divzero in self._entry.get() or self.erro in self._entry.get():
            self._entry.delete(0, "end")
        if len(self._entry.get()) < self._limite:
            self._entry.insert(0+len(self._entry.get()), "7")


    # 8
    def bt8(self):
        if self.divzero in self._entry.get() or self.erro in self._entry.get():
            self._entry.delete(0, "end")
        if len(self._entry.get()) < self._limite:
            self._entry.insert(0+len(self._entry.get()), "8")


    # 9
    def bt9(self):
        if self.divzero in self._entry.get() or self.erro in self._entry.get():
            self._entry.delete(0, "end")
        if len(self._entry.get()) < self._limite:
            self._entry.insert(0+len(self._entry.get()), "9")


    # Vírgula
    def btcomma(self):
        if self.divzero in self._entry.get() or self.erro in self._entry.get():
            self._entry.delete(0, "end")
        if len(self._entry.get()) < self._limite and len(self._entry.get()) > 0:
            self._entry.insert(0+len(self._entry.get()), ".")


    # Funções das operações

    # Apagar tudo
    def ac(self):
        if self.divzero in self._entry.get() or self.erro in self._entry.get():
            self._entry.delete(0, "end")
        if len(self._entry.get()) > 0:
            self._entry.delete(0, "end")


    # Apagar um dígito (<X)
    def clearone(self):
        if self.divzero in self._entry.get() or self.erro in self._entry.get():
            self._entry.delete(0, "end")
        if len(self._entry.get()) > 0:
            self._entry.delete(int(len(self._entry.get().replace(",", "").replace(".",""))-1))


    # Soma
    def btsum(self):
        if self.divzero in self._entry.get() or self.erro in self._entry.get():
            self._entry.delete(0, "end")
        if len(self._entry.get()) < self._limite and len(self._entry.get()) > 0:
            if not "+" in self._entry.get():
                self._entry.insert(0+len(self._entry.get()), "+")


    # Multiplicação
    def btmult(self):
        if self.divzero in self._entry.get() or self.erro in self._entry.get():
            self._entry.delete(0, "end")
        if len(self._entry.get()) < self._limite and len(self._entry.get()) > 0:
            if not "*" in self._entry.get():
                self._entry.insert(0+len(self._entry.get()), "*")


    # Subtração
    def btmin(self):
        if self.divzero in self._entry.get() or self.erro in self._entry.get():
            self._entry.delete(0, "end")
        if len(self._entry.get()) < self._limite and len(self._entry.get()) > 0:
            if not "-" in self._entry.get():
                self._entry.insert(0+len(self._entry.get()), "-")


    # Divisão
    def btdiv(self):
        if self.divzero in self._entry.get() or self.erro in self._entry.get():
            self._entry.delete(0, "end")
        if len(self._entry.get()) < self._limite and len(self._entry.get()) > 0:
            if not "/" in self._entry.get():
                self._entry.insert(0+len(self._entry.get()), "/")


    # Porcentagem
    def btpercent(self):
        if self.divzero in self._entry.get() or self.erro in self._entry.get():
            self._entry.delete(0, "end")
        if len(self._entry.get()) < self._limite and len(self._entry.get()) > 0:
            if not "%" in self._entry.get():
                self._entry.insert(0+len(self._entry.get()), "%")


    # Resultado
    def btres(self):
        if len(self._entry.get()) > 0:
            try:
                opt = self._entry.get().replace(" ", "")
                opt = opt.replace("%", "/100*")
                result = eval(opt)
                self._entry.delete(0, "end")
                self._entry.insert(0, result)
            except ZeroDivisionError:
                self._entry.delete(0, "end")
                self._entry.insert(0, self.divzero)
            except Exception as e:
                self._entry.delete(0, "end")
                self._entry.insert(0, self.erro)
