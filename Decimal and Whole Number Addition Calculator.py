app_name = "Decimal and Whole Numbers Addition Calculator"
dnrh = "Decimal Number here: "
wnrh = "Whole Number here: "
nameq = input("What is your name?: ")
print("Welcome to", app_name, nameq + "!")
print(nameq, ", please enter your Decimal Number.")
dnrie = input("Example: ""10.1"" " + dnrh)
print("Now, enter your While, Whole Number.")
wnrie = input("Example: ""20"" " + wnrh)
print("Please wait while calculate the addition of", dnrie, "+", wnrie, "= ? Calculating...")
rescaln = float(dnrie) + int(wnrie)
print("Dear", nameq, "we have successfully calculated", dnrie, "+", wnrie, "=  Loading your answer.....")
print("Your answer is:", dnrie, "+", wnrie, "=", rescaln)