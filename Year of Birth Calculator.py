app_name = "Year Of Birth Calculator App"
visitors_name = input("What is your name?: ")
print("welcome to", app_name, visitors_name + ".")
ageq = input ("How old are you " + visitors_name + "?: ")
byearcal = 2022 - int(ageq)
byconfirmation = input("Your year of birth is "+ str(byearcal)+". " + "Is this correct " + visitors_name+"?: ")
print("Thank you for using our", app_name +"!")
print("We hope to see you again", visitors_name + ".")