def paying_debt_off_in_a_year(balance,interest):
    lower = balance/12.0
    upper = balance*((1.0+interest)**12)/12.0
    monthly_unpaid_balance = balance
    while abs(monthly_unpaid_balance) > 0.000001:
        minimun_monthly_payment =  (lower+upper)/2.0
        monthly_interest_rate = interest / 12.0
        update_balance_each_month = balance
        for i in range(12):
            monthly_unpaid_balance = update_balance_each_month - minimun_monthly_payment
            update_balance_each_month = monthly_unpaid_balance + monthly_interest_rate * monthly_unpaid_balance
        if monthly_unpaid_balance>0:
            lower = minimun_monthly_payment
        else:
            upper = minimun_monthly_payment
    print('Lowest Payment: %.2f' % minimun_monthly_payment)

paying_debt_off_in_a_year(balance,annualInterestRate)
