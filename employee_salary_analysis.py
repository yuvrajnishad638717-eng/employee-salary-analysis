import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed()

employees_ids = np.arange(1,11)
name = np.random.choice(
    ["Yuvraj", "Nishtha", "Raj", "Saurabh"],
    10
)
age = np.random.randint(18, 45, 10)
salary = np.random.randint(18000, 60000, 10)
department = np.random.choice(
    ["IT", 'SALES', "HR", "MANAGER", "SUPERVISOR"],
    10
)

df = pd.DataFrame(
    {
        "employees_id" : employees_ids,
        "name" : name,
        "age" : age,
        "salary" : salary,
        "department" : department
    }
)

print("--------EMPLOYEES DATA UPADTE 2026--------")
print(df)

print("\n AVERAGE_SALARY: ", np.mean(salary))
print("\n HIGHEST_SALARY: ", np.max(salary))
print("\n LOWEST_SALARY: ", np.min(salary))
print("\n AVERAGE_AGE: ", np.mean(age))

print("\n ----------PLOT CHART--------")
plt.plot(
    df["employees_id"],
    df["salary"]
)

plt.title("EMPLOYEES_SALARY_CHART")
plt.show()

print("\n ---------BAR CHART--------")

plt.bar(
    df["employees_id"],
    df["salary"]
)
plt.title("----------EMPLOYEES_SALARY----------")
plt.show()

print("\n ---------PIE CHART--------")

dept_count = df.value_counts("department")
print(dept_count)

plt.pie(
    dept_count,
    labels=dept_count.index
)

plt.title("Department Distribution")
plt.show()

df["bonus_salary"] = df["salary"] * 1.1
print(df)


