from msilib.schema import Error


mu=input("введите данные:   ")


def chislo_stroka(m):
    # определить тип данных
    return type(m)

def dlina_mu():
    if mu>0:
        ch=len(mu)
        if ch>=1:
            return 1
        else:
            return 0
    else:
        return 0

def chislo():
    if mu>=len(mu):
        return True
    else:
        return False

def chetnoe(mu):
    if mu % 2 == 0:
        return True
    else:
        return False

# Будем считать email адрес корректным, если в нем есть символ собачки (@) и точки. программа проверяющую корректность email адреса.
def email(mu):
    s2=mu
    s1='@'
    s3='.'
    if (s1 in s2) and (s3 in s2):
        return'YES'
    else:
        return'NO'

def bukva(mu):
    A="qwertyuiopasdfghjklzxcvbnm"
    Aa=mu.lover
    D="йцукенгшщзхъфывапролджэячсмитьбю"
    Dd=mu.lover
    for mu in A or D or Aa or Dd:
        return True
    else:
        return False

    




# тесты для числа
# не путая строка
def test_ch_int():
    assert chislo_stroka(mu)!=str, "это строка"
    assert dlina_mu(mu)==1, "pusto"

def test_ch_dl():
    assert chislo_stroka(mu)!=str, "это строка"
    assert chislo(mu), "длина больше значения"
    

def test_ch_chetn():
        assert chislo_stroka(mu)!=str, "это строка"
        assert chetnoe(mu), "не четное"



    

# тесты для строки
def test_stroka_1():
    assert chislo_stroka(mu)==str, "это число"
    assert dlina_mu(mu)==1, "pusto"

def test_stroka_2():
    assert chislo_stroka(mu)==str, "это число"
    assert email(mu)=="NO", "адрес почты"

def test_stroka_3():
    assert chislo_stroka(mu)==str, "это число"
    assert bukva(mu), "адрес почты"


