annual_salary = float(input("Enter your annual salary: "))
total_cost = 1000000
semi_annual_raise = 0.07

portion_down_payment = .25
down_payment = portion_down_payment * total_cost

r = 0.04 # Annual return
monthly_salary = annual_salary/12.0

low = 0
high = 10000
guess = (low + high)//2
numGuesses = 0

while low < high:
    
    portion_saved = guess/10000.0
    monthly_salary_saved = monthly_salary * portion_saved
    count = 1
    current_savings = 0.0
    numGuesses += 1
    
    while count <= 36:
        if (count-1)%6 == 0 and (count-1)>0:
            monthly_salary_saved += (monthly_salary_saved * semi_annual_raise)
        
        return_investment = (current_savings * r)/12.0
        current_savings += (return_investment + monthly_salary_saved)
        count += 1
    
    if abs(current_savings - down_payment) < 100.0:
        if current_savings >= down_payment:
            print("Best savings rate:", portion_saved)
            print("Steps in bisection search:", numGuesses)
            break
        
   
    if current_savings < down_payment:
        low = guess
    else:
        high = guess
        
    guess = (low + high)//2
    
    if numGuesses > 13:
        print("It is not possible to pay the down payment in three years.")
        break

