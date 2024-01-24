
#Limitador de caracteres no output
limite = 13

# Mensagens de erros
divzero = "N/P div by 0"
erro = "Erro"

# Números

# 0
def bt0(entry):
    if divzero in entry.get() or erro in entry.get():
        entry.delete(0, "end")
    if len(entry.get()) < limite:
        entry.insert(0+len(entry.get()), "0")

# 1
def bt1(entry):
    if divzero in entry.get() or erro in entry.get():
        entry.delete(0, "end")
    if len(entry.get()) < limite:
        entry.insert(0+len(entry.get()), "1")


# 2
def bt2(entry):
    if divzero in entry.get() or erro in entry.get():
        entry.delete(0, "end")
    if len(entry.get()) < limite:
        entry.insert(0+len(entry.get()), "2")


# 3
def bt3(entry):
    if divzero in entry.get() or erro in entry.get():
        entry.delete(0, "end")
    if len(entry.get()) < limite:
        entry.insert(0+len(entry.get()), "3")


# 4
def bt4(entry):
    if divzero in entry.get() or erro in entry.get():
        entry.delete(0, "end")
    if len(entry.get()) < limite:
        entry.insert(0+len(entry.get()), "4")


#  5
def bt5(entry):
    if divzero in entry.get() or erro in entry.get():
        entry.delete(0, "end")
    if len(entry.get()) < limite:
        entry.insert(0+len(entry.get()), "5")


# 6
def bt6(entry):
    if divzero in entry.get() or erro in entry.get():
        entry.delete(0, "end")
    if len(entry.get()) < limite:
        entry.insert(0+len(entry.get()), "6")


# 7
def bt7(entry):
    if divzero in entry.get() or erro in entry.get():
        entry.delete(0, "end")
    if len(entry.get()) < limite:
        entry.insert(0+len(entry.get()), "7")


# 8
def bt8(entry):
    if divzero in entry.get() or erro in entry.get():
        entry.delete(0, "end")
    if len(entry.get()) < limite:
        entry.insert(0+len(entry.get()), "8")


# 9
def bt9(entry):
    if divzero in entry.get() or erro in entry.get():
        entry.delete(0, "end")
    if len(entry.get()) < limite:
        entry.insert(0+len(entry.get()), "9")


# Vírgula
def btcomma(entry):
    if divzero in entry.get() or erro in entry.get():
        entry.delete(0, "end")
    if len(entry.get()) < limite and len(entry.get()) > 0:
        entry.insert(0+len(entry.get()), ".")


# Funções das operações

# Apagar tudo
def ac(entry):
    if divzero in entry.get() or erro in entry.get():
        entry.delete(0, "end")
    if len(entry.get()) > 0:
        entry.delete(0, "end")


# Apagar um dígito (<X)
def clearone(entry):
    if divzero in entry.get() or erro in entry.get():
        entry.delete(0, "end")
    if len(entry.get()) > 0:
        entry.delete(int(len(entry.get().replace(",", "").replace(".",""))-1))


# Soma
def btsum(entry):
    if divzero in entry.get() or erro in entry.get():
        entry.delete(0, "end")
    if len(entry.get()) < limite and len(entry.get()) > 0:
        entry.insert(0+len(entry.get()), "+")


# Multiplicação
def btmult(entry):
    if divzero in entry.get() or erro in entry.get():
        entry.delete(0, "end")
    if len(entry.get()) < limite and len(entry.get()) > 0:
        entry.insert(0+len(entry.get()), "*")


# Subtração
def btmin(entry):
    if divzero in entry.get() or erro in entry.get():
        entry.delete(0, "end")
    if len(entry.get()) < limite and len(entry.get()) > 0:
        entry.insert(0+len(entry.get()), "-")


# Divisão
def btdiv(entry):
    if divzero in entry.get() or erro in entry.get():
        entry.delete(0, "end")
    if len(entry.get()) < limite and len(entry.get()) > 0:
        entry.insert(0+len(entry.get()), "/")


# Porcentagem
def btpercent(entry):
    if divzero in entry.get() or erro in entry.get():
        entry.delete(0, "end")
    if len(entry.get()) < limite and len(entry.get()) > 0:
        entry.insert(0+len(entry.get()), "%")


# Resultado
def btres(entry):
    if len(entry.get()) > 0:
        try:
            opt = entry.get().replace(" ", "")
            opt = opt.replace("%", "/100*")
            result = eval(opt)
            entry.delete(0, "end")
            entry.insert(0, result)
        except ZeroDivisionError:
            entry.delete(0, "end")
            entry.insert(0, divzero)
        except Exception as e:
            entry.delete(0, "end")
            entry.insert(0, erro)
