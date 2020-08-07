from business_model import BusinessModel
from business_projection import Business_Projection
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

    business_projection = Business_Projection()

    # Stream Lit
    # st.markdown("<h1 style='text-align: center; color: red;'>Remotion Business Model simulator</h1>",
    #            unsafe_allow_html=True)
    st.pyplot(business_projection.plot(remotion))
    #ROI = max(remotion.subscription_income) / (-1*np.min(accumulative_benefit))
    #st.markdown('**ROI: ** {:04.2f}%'.format(ROI*100))
    #st.markdown("Last month subcription income / Initial investment")


if __name__ == '__main__':
    main()
