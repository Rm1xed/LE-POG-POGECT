high_income = True
good_credit = True
student = False
if (high_income or good_credit) and not student:
    print("eligible")
else:
    print("not elibgible")