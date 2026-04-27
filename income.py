income_per_annum=1000000
health_insurance=5000
tax =income_per_annum*0.10
health_insurance=5000
income_per_annum-=tax+health_insurance
income_per_mnth=income_per_annum/12
print("cash after expenses is rupees",income_per_mnth)