print(
    "Welcome to the COVID 19 support service. Please select an option "
    "below:\n1.Statistics\n2.Prevention\n3.Symptoms\n4.Treatment\n5.Report case\n6.Exit")

choice = int(input("Enter choice( 1 / 2 / 3 / 4 / 5 / 6 ): "))
numChoice = [1, 2, 3, 4, 5, 5, 6]
yesno = ["y", "Y", "n", "N"]
bool1 = True
bool2 = True
for x in numChoice:
    if choice != x:
        bool1 = False
        continue
    else:
        bool1 = True
        break
if bool1 == False:
    print("input is not valid")
if choice == 1:
    print(
        "\nCurrently in SA there are 27403 Confirmed cases\nCurrently in USA there are 1700000 Confirmed cases\nCurrently in china there are 82995 Confirmed cases")
elif choice == 2:
    print("\nHere is how to prevent COVID-19"
          "\n"
          "\nTo prevent the spread of COVID-19"
          "\nClean your hands often. Use Soap and water, or alcohol-based hand rub."
          "\nMaintain a safe distance from anyone who is coughing or sneezing."
          "\nDon't touch your eyes, nose or mouth."
          "\nCover your nose and mouth with your bent elbow or a tissue when you cough or sneeze."
          "\nStay home if you feel unwell."
          "\nIf you have a fever, cough and difficulty breathing ,seek medical attention. Call in advance"
          "\nFollow the directions of your local health authority.")

elif choice == 3:
    print("\nthe Confirmed Symptoms are ="
          "\nMost common symptoms: "
          "\nfever"
          "\ndry cough"
          "\ntiredness"
          "\n"
          "\nLess common symptoms: "
          "\naches and pains"
          "\nsore throat"
          "\ndiarrhoea"
          "\nconjunctivitis"
          "\nheadache"
          "\nloss of taste or smell"
          "\na rash on skin, or discolouration of fingers or toes"
          "\n"
          "\nSerious symptoms:"
          "\ndifficulty breathing or shortness of breath"
          "\nchest pain or pressure"
          "\nloss of speech or movement")
elif choice == 4:
    print("\nthe Treatment are ="
          "\n"
          "\nif you feel sick you should rest, drink plenty of fluid, and eat nutritious food. stay in a separate room"
          "\nfrom other family members, and use a dedicated bathroom if possible. Clean and disinfect"
          "\nfrequently touched surfaces.")
elif choice == 5:

    print("in which country are you, select a option below")
    list = ["1.SA", "2.USA", "3.China"]
    print(list[0])
    print(list[1])
    print(list[2])
    Option = int(input("Enter option(1/2/3):"))
    if Report_c == "y" or Report_c == "Y":
        print("you have COVID-19 please see treatment")
    elif Report_c == "n" or Report_c == "N":
        print("You don't have COVID-19")

elif choice == 6:
    print("\nThank You Goodbye ")
    exit()

randomCountry = input("\nWould you like to see the Confirmed cases for a random country? y/n: ")
for x in yesno:
    if randomCountry != x:
        bool2 = False
        continue
    else:
        bool2 = True
        break
if bool2 == False:
    print("input is not valid")

if randomCountry == "y" or randomCountry == "Y":
    country = input("\nTo select a random country, type a number from 0 to 9: ")
    if country == "0":
        print("ireland has 271443 confirmed cases")
    if country == "1":
        print("japan has 795000 confirmed cases")
    if country == "2":
        print("Wales has 4737943 confirmed cases")
    if country == "3":
        print("Brazil has 18464134 confirmed cases")
    if country == "4":
        print("Italy has 4260838 confirmed cases")
    if country == "5":
        print("Spain has 3780000 confirmed cases")
    if country == "6":
        print("Sweden has 1090000 confirmed cases")
    if country == "7":
        print("India has 30250040 confirmed cases")
    if country == "8":
        print("France has 5772128 confirmed cases")
    if country == "9":
        print("Germany has 3730488 confirmed cases")
