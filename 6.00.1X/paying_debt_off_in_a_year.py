def paying_debt_off_in_a_year(balance,interest):
    minimun_monthly_payment = 0
    update_balance_each_month = balance
    while update_balance_each_month > 0:
        minimun_monthly_payment +=10 
        monthly_interest_rate = interest / 12.0
        update_balance_each_month = balance
        for i in range(12):
            monthly_unpaid_balance = update_balance_each_month - minimun_monthly_payment
            update_balance_each_month = monthly_unpaid_balance + monthly_interest_rate * monthly_unpaid_balance
    print('Lowest Payment: %i' % minimun_monthly_payment)

paying_debt_off_in_a_year(balance,annualInterestRate)
