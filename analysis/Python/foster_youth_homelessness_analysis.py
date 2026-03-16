<\> Bash

import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------
# 1. Youth Aging Out vs Youth Homelessness
# --------------------------------

# Load datasets
national_trends = pd.read_csv("Cleaned/national_trends_master.csv")
youth_outcomes = pd.read_csv("Cleaned/youth_outcomes_master.csv")

print(national_trends.head())
print(youth_outcomes.head())

print(national_trends.columns)
print(youth_outcomes.columns)

# Visualization: Youth Aging Out vs Youth Homelessness
plt.figure()

plt.plot(
    national_trends["Year"],
    national_trends["Youth Aging Out"],
    marker="o",
    label="Youth Aging Out"
)

plt.plot(
    national_trends["Year"],
    national_trends["Youth Homeless 18-24"],
    marker="o",
    label="Youth Homeless 18-24"
)

plt.title("Youth Aging Out vs Youth Homelessness (2020-2024)")
plt.xlabel("Year")
plt.ylabel("Number of Youth")

plt.xticks(national_trends["Year"])

plt.legend()

plt.savefig("Visualizations/youth_aging_out_vs_homelessness.png")

plt.show()

# --------------------------------
# 2. Youth Homelessness Trend
# --------------------------------
plt.figure()

plt.plot(
    national_trends["Year"],
    national_trends["Youth Homeless 18-24"],
    marker = "o"
)

plt.title("Youth Homelessness Trend (2020-2024)")
plt.xlabel("Year")
plt.ylabel("Youth Homeless 18-24")

plt.xticks(national_trends["Year"])

plt.savefig("Visualizations/youth_homeless_trend.png")
plt.show()

# --------------------------------
# 3. Employment and Educational Outcomes
# --------------------------------
plt.figure()

x = range(len(youth_outcomes["Cohort"]))
width = 0.35

plt.bar(
    [i - width / 2 for i in x],
    youth_outcomes["Employment Rate"],
    width=width,
    label="Employment Rate"
)

plt.bar(
    [i + width / 2 for i in x],
    youth_outcomes["Education Attainment"],
    width=width,
    label="Education Attainment"
)

plt.xticks(list(x), youth_outcomes["Cohort"])
plt.title("Employment and Education Outcomes")
plt.xlabel("Cohort")
plt.ylabel("Percent")
plt.legend()

plt.savefig("Visualizations/employment_education_outcomes.png")
plt.show()

# --------------------------------
# 4. Homelessness Risk and Health Coverage
# --------------------------------
plt.figure()

x = range(len(youth_outcomes["Cohort"]))
width = 0.35

plt.bar(
    [i - width / 2 for i in x],
    youth_outcomes["Homelessness Risk"],
    width=width,
    label="Homelessness Risk"
)

plt.bar(
    [i + width / 2 for i in x],
    youth_outcomes["Health Coverage"],
    width=width,
    label="Health Coverage"
)

plt.xticks(list(x), youth_outcomes["Cohort"])
plt.title("Homelessness Risk and Health Coverage")
plt.xlabel("Cohort")
plt.ylabel("Percent")
plt.legend()

plt.savefig("Visualizations/homelessness_risk_health_coverage.png")
plt.show()
