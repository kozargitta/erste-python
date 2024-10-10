yearly_salaries = [11_000, 22_300, 45_000, 35_800, 50_000]
# high, if graeter than 40_000
high_salarie_limit = 40_000
sum_high_salaries = 0
sum_low_salaries = 0

for salary in yearly_salaries:
    if salary > high_salarie_limit:
        sum_high_salaries += salary
    else:
        sum_low_salaries += salary

# for i in range(len(yearly_salaries)):
#     if yearly_salaries[i] > high_salarie_limit:
#         sum_high_salaries += yearly_salaries[i]
#     else:
#         sum_low_salaries += yearly_salaries[i]

print(f"Sum of high salaries: {sum_high_salaries}")
print(f"Sum of low salaries: {sum_low_salaries}")
