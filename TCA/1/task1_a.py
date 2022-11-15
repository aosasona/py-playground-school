run_application = True

while run_application:
    """
    This is the main loop of the application.
    It will run infinitely until the user decides to quit by indirectly setting the run_application flag to False.
    """

    light_years = float(input("Enter the number of light years: "))
    kilometers = light_years / 0.00000000000010570
    print("The number of kilometers is: ", kilometers)
    run_application = input("Do you want to run the application again? (y/n): ").lower() == "y"

print("Goodbye!")
