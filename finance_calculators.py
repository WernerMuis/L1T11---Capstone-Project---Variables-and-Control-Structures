import math

while True:

    # Asking the user to select either investment or bond
    user_choice = input("investment - to calculate the amount of interest you'll earn on your investment \n"
                        "bond       - to calculate the amount you'll have to pay on a home loan \n"
                        "\n"
                        "Enter either 'investment' or 'bond' from the menu above to proceed:").lower()
    
    # If investment then asking the user's inputs for the formula
    if user_choice == "investment":
        invest_amount = float(input("Please enter the amount you are investing: "))
        invest_interest_rate = int(input("Please enter the investment rate that you are investing at: "))
        invest_interest_rate = invest_interest_rate/100
        invest_years = int(input("Please enter the amount of years you would like to invest: "))

        while True:
            # Asking the user to select one of the interest types
            interest = input("Please select state what interest type you would like to make use of. \n"
                            "Simple or Compound: ").lower()
            
            # The formulas for the different interest types
            simple_interest = round(invest_amount * (1 + invest_interest_rate * invest_years), 2)
            compound_interest = round(invest_amount * math.pow((1 + invest_interest_rate), invest_years), 2)

            # If simple, then I print the one formula results
            if interest == "simple":
                print(f"The amount you'll earn using Simple interest is R{simple_interest}.")
                break

            # If compound were selected
            elif interest == "compound":
                print(f"The amount you'll earn using Compound interest is R{compound_interest}.")
                break

            else:
                print("Please make sure to either enter 'simple' or 'compound' to proceed.")      
        break

    # If initial choice was bond then asking the user's inputs for the formula
    if user_choice == "bond":
        house_value = float(input("Please enter the value of your house: "))
        bond_interest_rate = int(input("Please enter the interest rate: "))
        bond_interest_rate = bond_interest_rate/12/100
        repay_months = int(input("Please enter the amount of months you are planning on paying back the bond: "))

        # The formula for the bond
        monthly_repayment = round((bond_interest_rate * house_value) / (1 - (1 + bond_interest_rate)** (-repay_months)), 2)

        # The bond result
        print(f"Your monthly payment will be R{monthly_repayment}")
        break

    # For if the user did not initially select investment or bond     
    else:
        print("Please make sure to either enter 'investment' or 'bond' to proceed.")
