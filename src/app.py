from business_model import BusinessModel
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
# app functions
from utils.cost_calculators import api_cost_per_user, storage_cost_per_user
from utils.my_users import user_projection
from utils.helpers import tooman2euro, preack_even_point, millify


def main():
    remotion = BusinessModel()
    remotion.update_fix_cost("Product develmpent leader",
                             tooman2euro(20*10**6), tag="HR")
    remotion.update_fix_cost("Full stack devlooper",
                             tooman2euro(15*10**6), tag="HR")
    remotion.update_fix_cost("ML Engeeiner", tooman2euro(15*10**6), tag="HR")
    remotion.update_fix_cost("Front end develooper",
                             tooman2euro(15*10**6), tag="HR")
    remotion.update_fix_cost(
        "UX/UI develloper", tooman2euro(15*10**6), tag="HR")
    remotion.update_fix_cost("Data engeenier", tooman2euro(15*10**6), tag="HR")

    # Marketing

    remotion.update_fix_cost(
        "Digital Marketer", tooman2euro(15*10**6), tag="HR")
    remotion.update_fix_cost("Groth hacker", tooman2euro(15*10**6), tag="HR")
    remotion.update_fix_cost("Client success officer",
                             tooman2euro(15*10**6), tag="HR")

    # Business
    remotion.update_fix_cost("Business developper", 3000, tag="HR-EU")

    user_accusation_cost = st.slider(
        "User accusation cost? (Euros)", 0.01, 2.0, 0.02)
    remotion.update_variable_cost_per_user("Google Api", api_cost_per_user())
    remotion.update_variable_cost_per_user(
        "Google storage", storage_cost_per_user())
    remotion.update_variable_cost_per_user("Google Ads", user_accusation_cost)

    print("\n\n ************************************")
    print("Api cost= ", api_cost_per_user())
    print("Storage cost = ", storage_cost_per_user())

    months = st.slider(
        'How far do we project do reach targeted user?', 0, 5*12, 24)
    targeted_user = st.slider(
        'How many user do we project?', 1000, 10**6, 10**4)
    momentom = st.slider('Half lif?', .01, 3.0, 0.5)
    data = user_projection(
        months=months, maximum=targeted_user, half_life=momentom)
    remotion.users_data(data)

    convertion_rate = st.slider('Convertaion rate? (Percent)', 0.01, 0.2, 0.1)
    remotion.payed_user_projection_update(
        data, convertion_rate=convertion_rate)

    sunsciption_fee = st.slider('sunscription fee?', 1, 20, 9)
    print("Projection of fix cost: ", remotion.projection_of_fix_cost())

    print("Projection of variable cost", remotion.projection_of_variable_cost())

    print("Projection of Total cost", remotion.update_total_cost())

    print("Payed users", remotion.payed_user_data)
    print(" Income of suncription",
          remotion.projection_of_subsciption_income(sunsciption_fee))

    print("\n\n ************************************\n\n")

    acumulative_cost = remotion.cumulative_cost()
    acumulative_income = remotion.cumulative_income()
    accumulative_benefit = list(
        np.array(acumulative_income) - np.array(acumulative_cost))
    plt.figure(num=None, figsize=(16, 16), dpi=80,
               facecolor='w', edgecolor='k')

    plt.subplot(2, 1, 1)

    x, y = preack_even_point(acumulative_income, acumulative_cost)

    if x > 0:
        plt.text(x, y+10000, "Break even point is "+str(y)+" Euros at " + str(x) + "th months!",
                 rotation=45, rotation_mode='anchor')
        # ax.annotate('local maximum', xy=(x, y), xytext=(len(acumulative_cost)/3, max(acumulative_income)*0.66),
        #      arrowprops=dict(facecolor='black', shrink=0.05))

    else:
     #plt.text(months/3,cost[int(len(cost)*0.66)]," You do NOT pass the break-even in "+str(months)+" months")
        plt.text(months/2, acumulative_cost[int(len(acumulative_cost)/2)], " We do NOT pass the break-even in "+str(months)+" months",
                 size=30,
                 ha="center", va="center",
                 bbox=dict(
            boxstyle="round",
            ec=(1., 0.5, 0.5),
            fc=(1., 0.8, 0.8),
        )
        )

    plt.text(
        accumulative_benefit.index(np.min(accumulative_benefit)),
        np.min(accumulative_benefit),
        "Capital requirement = "+str(-1*np.min(accumulative_benefit)) + "€",
        rotation=45, rotation_mode='anchor'
    )

    plt.plot(acumulative_cost, label="Cumulative cost", marker='o')
    plt.plot(acumulative_income, label="Cumulative income", marker='o')
    plt.ylabel(millify(max(acumulative_income)))
    plt.xlabel("Months")
    plt.legend(loc="upper left")
    plt.title("Finantial projection")

    plt.subplot(2, 1, 2)
    plt.plot(data)
    plt.title("User projection")
    plt.xlabel("Months")
    plt.ylabel("Number of users")

    # Stream Lit
    st.markdown("<h1 style='text-align: center; color: red;'>Remotion Business Model simulator</h1>",
                unsafe_allow_html=True)
    st.pyplot(plt)
    ROI = max(remotion.subscription_income) / (-1*np.min(accumulative_benefit))
    st.markdown('**ROI: ** {:04.2f}%'.format(ROI*100))
    st.markdown("Last month subcription income / Initial investment")


if __name__ == '__main__':
    main()
