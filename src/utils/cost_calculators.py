def api_cost_per_user(
    duration=10,  # minits,
    number_of_frame_per_min=12
):
    api_cost_per_request = 1/1000  # one euro for every request

    return api_cost_per_request*duration * number_of_frame_per_min


def storage_cost_per_user(user_storage_need=1):  # Giga bit,
    storage_cost = 2/100  # 2 Euros for every 100 Giga bites
    return storage_cost * user_storage_need
