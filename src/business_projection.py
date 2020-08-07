from business_model import BusinessModel
import matplotlib.pyplot as plt2
import streamlit as st
import numpy as np
# app functions
from utils.cost_calculators import api_cost_per_user, storage_cost_per_user
from utils.my_users import user_projection
from utils.helpers import tooman2euro, preack_even_point, millify


class Business_Projection():
    """
    We will generate projection bassed on Business Modell Object
    """

    def plot(self, business_model):

        self.acumulative_cost = business_model.cumulative_cost()
        self.acumulative_income = business_model.cumulative_income()
        self.accumulative_benefit = list(
            np.array(self.acumulative_income) - np.array(self.acumulative_cost))

        plt2.figure(num=None, figsize=(16, 16), dpi=80,
                    facecolor='w', edgecolor='k')

        plt2.subplot(2, 1, 1)

        x, y = preack_even_point(
            self.acumulative_income, self.acumulative_cost)

        if x > 0:
            plt2.text(x, y+10000, "Break even point is "+str(y)+" Euros at " + str(x) + "th months!",
                      rotation=45, rotation_mode='anchor')
            # ax.annotate('local maximum', xy=(x, y), xytext=(len(acumulative_cost)/3, max(acumulative_income)*0.66),
            #      arrowprops=dict(facecolor='black', shrink=0.05))

        else:
            #plt2.text(months/3,cost[int(len(cost)*0.66)]," You do NOT pass the break-even in "+str(months)+" months")
            plt2.text(len(business_model.users_projection)/2,
                      self.acumulative_cost[int(len(self.acumulative_cost)/2)],
                      " We do NOT pass the break-even in " +
                      str(len(business_model.users_projection))+" months",
                      size=30,
                      ha="center", va="center",
                      bbox=dict(
                boxstyle="round",
                ec=(1., 0.5, 0.5),
                fc=(1., 0.8, 0.8),
            )
            )

        plt2.text(
            self.accumulative_benefit.index(np.min(self.accumulative_benefit)),
            np.min(self.accumulative_benefit),
            "Capital requirement = " +
            str(-1*np.min(self.accumulative_benefit)) + "€",
            rotation=45, rotation_mode='anchor'
        )

        plt2.plot(self.acumulative_cost, label="Cumulative cost", marker='o')
        plt2.plot(self.acumulative_income,
                  label="Cumulative income", marker='o')
        plt2.ylabel(millify(max(self.acumulative_income)))
        plt2.xlabel("Months")
        plt2.legend(loc="upper left")
        plt2.title("Finantial projection")

        plt2.subplot(2, 1, 2)
        plt2.plot(business_model.users_projection)
        plt2.title("User projection")
        plt2.xlabel("Months")
        plt2.ylabel("Number of users")

        return plt2
