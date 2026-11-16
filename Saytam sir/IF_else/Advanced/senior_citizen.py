age = int(input("Enter the number: "))
member = input("Are you a member? (yes/no): ").lower()


if age >= 60:
    print("Eligible for senior citizen discount")
elif age >=55 and member == "yes":
    print("Eligible for senior citizen discount")
else:
    print("Not Eligible for senior citizen discount")
