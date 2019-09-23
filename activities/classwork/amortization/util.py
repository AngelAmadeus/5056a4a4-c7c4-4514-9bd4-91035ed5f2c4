import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Amortization(object):

    def _init_(self, amount, interest, n):  # Object is initialized
        self.amount = amount  # All of the elements have an amount
        self.interest = interest  # All of the elements have interest
        self.n = n  # All of the elements have periods

    def annuity(self):
        """
        This function calculates the annuity of a credit
        :return: The annuity of the credit
        """
        # Annuity is a periodic payment made to amortize a credit.
        # The value of the annuity remains unchanged through the credit life.
        annuity = self.amount / ((1-(1+self.interest)**(-self.n))/self.interest)
        return annuity

    def get_table(self):
        """
        This function creates the amortization table of a credit with 5 columns: the period, the principal, the
        interest, the annuity and the loan value. Create a pandas DataFrame representing the amortization table.
        :return: The amortization table
        """
        annuity_ = self.annuity()
        principal_l = [0]
        interest_l = [0]
        annuity_l = [annuity_]
        loan_val_l = [self.amount]
        period_l = [0]

        for j in range(self.n):
            annuity_l.append(annuity_l[-1])
            interest_l.append(loan_val_l[-1] * self.interest)
            principal_l.append(annuity_l[-1] - interest_l[-1])
            loan_val_l.append(loan_val_l[-1] - principal_l[-1])
            period_l.append(j)

        table = pd.DataFrame([period_l, principal_l, interest_l, annuity_l, loan_val_l]).transpose()
        table = table.rename(columns={0: 'Period', 1: 'Principal', 2: 'Interest', 3: 'Annuity', 4: 'Loan Value'})
        return table

    def get_plot(self):
        """
        Create a plot (fig) to visualize at least two variables from the amortization table.
        :return: Figure
        """
        table = self.get_table()
        fig = plt.figure(1)
        plt.subplot(2, 2, 1)
        plt.plot(list(np.arange(self.n) + 1), list(table.iloc[1:, 0]))
        plt.title('Principal')
        plt.xlabel('Periods')
        plt.ylabel('Amount $')
        plt.subplot(2, 2, 2)
        plt.plot(list(np.arange(self.n) + 1), list(table.iloc[1:, 1]))
        plt.title('Interest')
        plt.xlabel('Periods')
        plt.ylabel('Interest $')
        plt.subplot(2, 2, 3)
        plt.plot(list(np.arange(self.n) + 1), list(table.iloc[1:, 2]))
        plt.title('Annuity')
        plt.xlabel('Periods')
        plt.ylabel('Annuity $')
        plt.subplot(2, 2, 4)
        plt.plot(list(np.arange(self.n) + 1), list(table.iloc[1:, 3]))
        plt.title('Loan Value')
        plt.xlabel('Periods')
        plt.ylabel('Loan Value $')
        plt.show()
        return fig
