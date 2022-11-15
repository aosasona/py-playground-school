import doctest

# Passing around raw strings could be dangerous, so we'll use constants
UNDERWEIGHT = "underweight"
HEALTHY = "healthy"
OVERWEIGHT = "overweight"
OBESE = "obese"

# This contains the fields that are required, and the type they should be
required_fields = {
    "name": ["name", str],
    "height": ["height (cm)", float],
    "weight": ["weight (kg)", float],
}


def get_data():
    """
    Ask user for the required data, and return it as a dictionary.
    """
    data = {}
    for field in required_fields:
        val = input(f"Enter your {required_fields[field][0]}: ")
        if type(val) != required_fields[field][1]:
            val = validate_fields(field, val)
        data[field] = val
    return data


def validate_fields(field, val):
    """
    Validate the data entered by the user and return it as the correct type if possible.
    :param field:  The field to validate
    :param val:  The value to validate
    :return: The value as the correct type if possible, otherwise raise an exception

    >>> validate_fields("height", "180")
    180.0
    """
    try:
        val = required_fields[field][1](val)
        if val == 0:
            raise ValueError(f"Invalid {required_fields[field][0]}")
    except ValueError:
        print(f"Invalid {required_fields[field][0]}")
        exit()
    return val


def convert_height_to_meters(height: float) -> float:
    """
    Convert the height from centimeters to meters.
    :param height: The height in centimeters
    :return: The height in meters

    >>> convert_height_to_meters(180)
    1.8
    """
    return height / 100


def calculate_bmi(weight: float, height: float) -> float:
    """
    Calculate the BMI of the user.
    :param weight: The weight of the user in kilograms
    :param height:  The height of the user in centimeters
    :return:  The BMI of the user as a float

    >>> calculate_bmi(80, 180)
    24.69
    """
    bmi = weight / (convert_height_to_meters(height) ** 2)
    return float(f"{bmi:.2f}")


def get_bmi_category(bmi: float) -> str:
    """
    Return the BMI category based on the BMI.
    :param bmi:  The BMI of the user
    :return:  The BMI category of the user

    >>> get_bmi_category(18.5)
    'healthy'
    """
    if bmi < 18.5:
        return UNDERWEIGHT
    elif bmi < 25:
        return HEALTHY
    elif bmi < 30:
        return OVERWEIGHT
    else:
        return OBESE


def write_to_file(filename: str, data: list):
    """
    This function will write the data to a file.
    :param filename: The name of the file to write to
    :param data: The data to write to the file as a list in the order it should be written
    :return: None
    """
    with open(filename, "a") as file:
        line = ""
        for item in data:
            line += f"{item}, "
        line = line[:-2] + "\n"
        file.write(line)


def main():
    try:
        data = get_data()
        bmi = calculate_bmi(data["weight"], data["height"])
        bmi_category = get_bmi_category(bmi)
        file_data = [data["name"], data["height"], data["weight"], bmi, bmi_category]
        write_to_file("bmi.csv", file_data)
        print(f">> {data['name']} is {bmi_category} with a BMI of {bmi} - see bmi.csv for more details")
    except Exception as e:
        print(f"An error occurred: {e}")
        exit()


if __name__ == "__main__":
    # Run the doctests first, and only run the main function if they pass
    doctest.testmod().failed == 0 and main()
