
#Limitador de caracteres na tela
limite = 13

# Números

# 0
def bt0(entry):
    if entry.get() == "" or len(entry.get()) < limite:
         entry.insert(0+len(entry.get()), "0")
    else:
        pass


# 1
def bt1(entry):
    if entry.get() == "" or len(entry.get()) < limite:
        entry.insert(0+len(entry.get()), "1")
    else:
        pass


# 2
def bt2(entry):
    if entry.get() == "" or len(entry.get()) < limite:
        entry.insert(0+len(entry.get()), "2")
    else:
        pass


# 3
def bt3(entry):
    if entry.get() == "" or len(entry.get()) < limite:
        entry.insert(0+len(entry.get()), "3")
    else:
        pass


# 4
def bt4(entry):
    if entry.get() == "" or len(entry.get()) < limite:
        entry.insert(0+len(entry.get()), "4")
    else:
        pass


#  5
def bt5(entry):
    if entry.get() == "" or len(entry.get()) < limite:
        entry.insert(0+len(entry.get()), "5")
    else:
        pass


# 6
def bt6(entry):
    if entry.get() == "" or len(entry.get()) < limite:
        entry.insert(0+len(entry.get()), "6")
    else:
        pass


# 7
def bt7(entry):
    if entry.get() == "" or len(entry.get()) < limite:
        entry.insert(0+len(entry.get()), "7")
    else:
        pass


# 8
def bt8(entry):
    if entry.get() == "" or len(entry.get()) < limite:
        entry.insert(0+len(entry.get()), "8")
    else:
        pass


# 9
def bt9(entry):
    if entry.get() == "" or len(entry.get()) < limite:
        entry.insert(0+len(entry.get()), "9")
    else:
        pass


# Vírgula
def btcomma(entry):
    if entry.get() == "" or len(entry.get()) < limite:
        entry.insert(0+len(entry.get()), ".")
    else:
        pass


# Funções das operações

# Apagar tudo
def ac(entry):
    if len(entry.get()) > 0:
        entry.delete(0, "end")
    else:
        pass


# Apagar um dígito (<X)
def clearone(entry):
    if len(entry.get()) > 0:
        entry.delete(int(len(entry.get().replace(",", "").replace(".",""))-1))
    else:
        pass


# Soma
def btsum(entry):
    if entry.get() == "" or len(entry.get()) < limite:
        entry.insert(0+len(entry.get()), "+")
    else:
        pass


# Multiplicação
def btmult(entry):
    if entry.get() == "" or len(entry.get()) < limite:
        entry.insert(0+len(entry.get()), "*")
    else:
        pass


# Subtração
def btmin(entry):
    if entry.get() == "" or len(entry.get()) < limite:
        entry.insert(0+len(entry.get()), "-")
    else:
        pass


# Divisão
def btdiv(entry):
    if entry.get() == "" or len(entry.get()) < limite:
        entry.insert(0+len(entry.get()), "/")
    else:
        pass


#Porcentagem
def btpercent(entry):
    if entry.get() == "" or len(entry.get()) < limite:
        entry.insert(0+len(entry.get()), "%")
    else:
        pass


# Resultado
def btres(entry):
    operadores = ["/", "*", "+", "-", "%"]
    opt = entry.get().replace("  ", " ").strip()
    for i in operadores:
        if i in opt:
            operador = i
            nums = opt.split(i)
            frs, sec = nums
        
            if "." in frs:
                frs = float(frs)
            else:
                frs = int(frs)
            if "." in sec:
                sec = float(sec)
            else:
                sec = int(sec)
            
            try:
                if operador == "/":
                    res = frs / sec
                elif operador == "*":
                    res = frs * sec
                elif operador == "+":
                    res = frs + sec
                elif operador == "-":
                    res = frs - sec
                elif operador == "%":
                    res = (frs/100) * sec
                else:
                    pass
            except  ZeroDivisionError:
                entry.delete(0, "end")
                entry.insert(0+len(entry.get()), "N/P div by 0")

            res = str(res)
            if "." in res:
                nums = res.split(".")
                part1, part2 = nums
                if "0" in part2 or "00" in part2 or "000" in part2:
                    res = int(part1)
                else:
                    pass
                res = float(res)
                res = f"{res:.2f}"
            else:
                res = int(res)
            
            entry.delete(0, "end")
            entry.insert(0+len(opt), res)
