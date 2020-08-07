import copy
import numpy as np


class BusinessModel:
    def __init__(self, scenario='default'):
        self.senario_label = scenario
        self.fix_cost = {}
        self.users_projection = []
        self.payed_user_data = []
        self.variable_cost = {}
        self.total_cost = []

        self.subscription_income = []

    def users_data(self, data):
        self.users_projection = copy.deepcopy(data)
        return self.users_projection

    def payed_user_projection_update(self, data, convertion_rate=0.1):
        self.payed_user_data = list(map(lambda x: x*convertion_rate, data))

    def update_fix_cost(self, label, cost, tag="fix_cost", cycle_by_month=1):
        self.fix_cost.update(
            {
                label: {
                    "cost": cost,
                    "cycle": cycle_by_month,
                    "tag": tag
                }
            }
        )
        return self.fix_cost

    def update_variable_cost_per_user(self, label, cost, tag="Cloud service cost", cycle_by_hours_of_usage=1):
        self.variable_cost.update(
            {
                label: {
                    "cost": cost,
                    "cycle": cycle_by_hours_of_usage,
                    "tag": tag
                }
            }
        )
        return self.fix_cost

    def projection_of_fix_cost(self):
        expenses = []
        months = len(self.users_projection)
        for month in range(months):
            expenses.append(
                sum([v['cost']/v['cycle'] for k, v in self.fix_cost.items()])
            )
        return expenses  # , sum( expenses)

    def projection_of_variable_cost(self):
        months = len(self.users_projection)
        expenses_for_unique_user = []
        for month in range(months):
            expenses_for_unique_user.append(
                sum([v['cost']/v['cycle']
                     for k, v in self.variable_cost.items()])
            )
        return [a*b for a, b in zip(expenses_for_unique_user, self.users_projection)]

    def projection_of_subsciption_income(self, price):
        self.subscription_income = [
            price*users for users in self.payed_user_data]
        return self.subscription_income

    def cumulative_income(self):
        return np.cumsum(self.subscription_income)

        # return expenses, sum( expenses)

    def update_total_cost(self):
        self.total_cost = [sum(x) for x in zip(
            self.projection_of_fix_cost(), self.projection_of_variable_cost())]
        return self.total_cost

    def cumulative_cost(self):
        return np.cumsum(self.total_cost)

    def __str__(self):
        items = self.__dict__.items()
        return str('\n'.join([f" {k} = {v} " for k, v in items]))
