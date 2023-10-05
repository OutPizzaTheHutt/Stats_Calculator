import K_Y_stats_module
numbers = []
while True:
    print("Options:")
    print("1. Input a number")
    print("2. Find the Mean")
    print("3. Find the Variance")
    print("4. Find the Standard Deviation")
    print("5. Find the Standard Error")
    print("6. Find the Z- Score")
    print("7. Summary of Statistics")
    print("When finished, enter (done)")
    
    option = input("Enter your option: ")
    if option == '1':
        try:
            num = float(input("Enter a number: "))
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a valid number." )
    elif option == '2':
        mean = K_Y_stats_module.calculate_mean(numbers)
        print(f"Mean: {mean}")
    elif option == '3':
        variance = K_Y_stats_module.calculate_variance(numbers)
    elif option == '4':
        std_deviation = K_Y_stats_module.calculate_std_deviation(numbers)
        print(f"Standard Deviation: {std_deviation}")
    elif option == '5':
        std_error = K_Y_stats_module.calculate_std_error(numbers)
        print(f"Standard Error: {std_error}")
    elif option == '6':
        try:
            new_value = float(input("Enter a new value: "))
            z_score = K_Y_stats_module.calculate_z_score(numbers, new_value)
            print(f"Z-score: {z_score}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    elif option == '7':
        mean = K_Y_stats_module.calculate_mean(numbers)
        variance = K_Y_stats_module.calculate_variance(numbers)
        std_deviation = K_Y_stats_module.calculate_std_deviation(numbers)
        std_error = K_Y_stats_module.calculate_std_error(numbers)
        print(f"Mean: {mean}")
        print(f"Variance: {variance}")
        print(f"Standard Deviation: {std_deviation}")
        print(f"Standard Error: {std_error}")
        
    elif option == 'done':
        break
    else:
        print("Wrong choice, select a valid option")
        
