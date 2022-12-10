Gross_income = int(input("Income = "))
Number_of_Dependents = int(input("Number Of Dependents = "))
Standard_Deduction = 10000
Dependent_Deduction = 3000
Tax_Rate = 0.2
Taxable_Income =  Gross_income - Standard_Deduction - (Dependent_Deduction * Number_of_Dependents)
Tax = Taxable_Income * Tax_Rate
print("Your Tax is " , Tax)









