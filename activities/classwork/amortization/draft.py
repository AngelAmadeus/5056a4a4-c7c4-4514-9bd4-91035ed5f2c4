import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Cap = 18000
interest = .34
periods_ = 12
time_ = 6


def annuity_f(cap_, i, periods, time):
    """
    This function calculates the annuity of a loan
    :param cap_: Amount of the loan at time 0
    :param i: interest rate (annual)
    :param periods: periods of capitalization
    :param time: amount of months, trimesters, etc
    :return: the annuity of the loan
    """
    a1 = cap_
    a2 = 1-((1+i/periods)**(-time))
    a3 = i/periods
    a4 = a1/(a2/a3)
    return a4


Annuity = annuity_f(Cap, interest, periods_, time_)
Principal_l = [0]
Interest_l = [0]
Annuity_l = [Annuity]
Loan_Val_l = [Cap]

for j in range(time_):
    Annuity_l.append(Annuity_l[-1])
    Interest_l.append(Loan_Val_l[-1]*(interest/periods_))
    Principal_l.append(Annuity_l[-1]-Interest_l[-1])
    Loan_Val_l.append(Loan_Val_l[-1]-Principal_l[-1])

table = pd.DataFrame([Principal_l, Interest_l, Annuity_l, Loan_Val_l]).transpose()
table = table.rename(columns={0: 'Principal', 1: 'Interest', 2: 'Annuity', 3: 'Loan Value'})
print(table.iloc[1:, :].round(2))

plt.figure(1)
plt.subplot(2, 2, 1)
plt.plot(list(np.arange(time_)+1), list(table.iloc[1:, 0]))
plt.title('Principal')
plt.xlabel('Periods')
plt.ylabel('Amount $')
plt.subplot(2, 2, 2)
plt.plot(list(np.arange(time_)+1), list(table.iloc[1:, 1]))
plt.title('Interest')
plt.xlabel('Periods')
plt.ylabel('Interest $')
plt.subplot(2, 2, 3)
plt.plot(list(np.arange(time_)+1), list(table.iloc[1:, 2]))
plt.title('Annuity')
plt.xlabel('Periods')
plt.ylabel('Annuity $')
plt.subplot(2, 2, 4)
plt.plot(list(np.arange(time_)+1), list(table.iloc[1:, 3]))
plt.title('Loan Value')
plt.xlabel('Periods')
plt.ylabel('Loan Value $')
plt.show()


def int_rate(co, cn, n):
    """
    This function calculates the interest rate of a
    :param co: payment  on time 0
    :param cn: payment  on tim n
    :param n: amount of periods
    :return: interest rate
    """
    a1 = np.log(cn/co)
    int_r = math.exp(a1/n) - 1
    return int_r


def int_rate_cuad(c0, c1, c2):
    """
    This function calculates the interest rate from general formula
    :param c0:
    :param c1:
    :param c2:
    :return:
    """
    a1 = 2*c2
    a2 = -c1+np.sqrt((c1**2) + 4*c2*c0)
    int_r = (a1/a2)-1
    return int_r


a = int_rate(5237, 5470, 6)
print(a*12)

a = int_rate_cuad(10000, 5000, 7000)
print(a)


def int_rate_cuad2(c0, c1, i):
    """
    This function calculates the interest rate from general formula
    :param c0:
    :param c1:
    :param i:
    :return:
    """
    a1 = c0-c1*((1+i)**(-1))
    a2 = (1+i)**(-2)
    int_r = (a1 / a2)
    return int_r


a = int_rate_cuad2(55000, 37621, 0.061)
print(a)
