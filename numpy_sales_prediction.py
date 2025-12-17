import numpy as np
days= np.array(["Mon","Tue","Wed","Thurs","Frid","sat","sun"])
sales=[]
print("ENTER THE SALES FOR EACH DAYS:")
for day in days:
    value=float(input(f"{day}: "))
    sales.append(value)
sales=np.array(sales)
print("---COMPANY SALES ANALYSIS FOR DAYS---")
print("TOTAL SALES OF THE WEEK:",np.sum(sales),"$")
print("AVERAGE DAILY SALARY:",np.mean(sales),"$")
print("HIGHEST SALES:",np.max(sales),"$")
print("LOWEST SALES :",np.min(sales),"$")

BEST_DAY= days[np.argmax(sales)]
WORST_DAY= days[np.argmin(sales)]
print("BEST_DAY :",BEST_DAY)
print("WORST_DAY :",WORST_DAY)

above_avg=days[sales> np.mean(sales)]
below_avg=days[sales> np.mean(sales)]
print("ABOVE_AVG_DAYS :",above_avg)
print("BELOW_AVG_DAYS :",below_avg)

