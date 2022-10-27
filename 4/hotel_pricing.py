print("""
|**************************************************|
|            HOTEL PRICING CALCULATOR              |
|**************************************************|

Use `ctrl + c` to terminate program early
""")

# VARS

data = {
    "people": 0,
    "type": None,
    "age": 0,
}
available_types = {
    "P": "personal",
    "B": "business"
}
discount = {
    "value": 0.0,
    "has_discount": False
}

BUSINESS_DISCOUNT = 0.2
AGE_DISCOUNT = 0.15

"""
FUNCTIONS
"""


def check_discount():
    try:
        if data["type"] == available_types["B"]:
            discount["value"] = BUSINESS_DISCOUNT
            discount["has_discount"] = True
            return
        elif data["type"] == available_types["P"]:
            discount["value"] = AGE_DISCOUNT
            discount["has_discount"] = True
            return
        else:
            return
    except Exception as e:
        print(e)


def calculate_rate(num: int, default_price: int):
    if num <= 4:
        return default_price
    return default_price / num


def calculate_price_with_discount(num: int, base_rate: int):
    if discount["has_discount"] is True:
        if num > 4:
            total_before_discount = base_rate * num
        else:
            total_before_discount = base_rate
        return total_before_discount - (total_before_discount * discount["value"])
    else:
        if num > 4:
            return base_rate * num
        else:
            return base_rate


def show_cost(final_cost: int):
    dis_val = discount["value"] * 100
    print(f"-----> Total cost is £{final_cost:.2f} with {dis_val:.0f}% discount applied")


def calculate_final_cost(num: int, base_num: int, base_cost: int):
    rate = calculate_rate(base_num, base_cost)
    cost = calculate_price_with_discount(num, rate)
    show_cost(cost)


"""
EXECUTION LOOPS
"""

while int(data["people"]) < 1:
    data["people"] = input(">> How many people are staying? ")

while data["type"] is None:
    stay_type = input(">> Is this a personal or business stay (P for personal, B for business)? ")
    if str(stay_type).upper() not in available_types:
        print("Error: invalid stay type!")
    else:
        data["type"] = available_types[stay_type.upper()]

while int(data["age"]) < 18:
    data["age"] = input(">> What is the paying customer's age? ")

# Check is discount is applicable
while discount["has_discount"] is False:
    check_discount()
    break

if discount["has_discount"] is True:
    dis = discount["value"] * 100
    print(f"-----> A discount of {dis:.0f}% is applicable to your rent cost")

people_int = int(data["people"])
match people_int:
    case _ if people_int <= 2:
        calculate_final_cost(num=people_int, base_num=people_int, base_cost=85)
    case 3:
        calculate_final_cost(num=people_int, base_num=3, base_cost=100)
    case _ if people_int >= 4:
        calculate_final_cost(num=people_int, base_num=4, base_cost=110)
    case _:
        print("Something went wrong!")
