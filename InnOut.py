print ("Menu\n")
fmenu = {'double-double':5.50, 'regular fries':3.50, 'animal-style fries':4.25,'five-by-five':8.50,'three-by-three':'not available', 'flying-dutchman':'not available', 'double-double protein style':'not available', 'milkshake':'not available','coke':'not available'}
# k = food item
# v = cost of food item

for k, v in dict.items(fmenu):
    print (k,"$",v)
            
yourOrder = input("\nWelcome to In-N-Out Burger. \n""\n\nTake your order please?")

#double-double
if yourOrder == 'double-double' or yourOrder =='double double':
    print("\nYou want the double-double.")
    onions = input("\nDo you want onions on your double-double (yes / no)")
    onions = onions.lower()
    if onions[0] == 'y' or  onions == 'yes':
        print("\nOK, you want onions on your double-double.")
    elif onions[0] == 'n' or onions == 'no':
        print("\nOK, no onions on your double-double.")
    else:
        print("\nthat is not a valid response.")

    forHere = input("\nIs this order for here, or to go: (for here / to go)")
    forHere = forHere.lower()
    if forHere[0] == 'f' or forHere == 'for here' or forHere =="here":
        print("\nOK, you're eating here.")
    elif forHere[0] == 't' or forHere =='to go':
        print("\nOK, your order is to go.")
    else:
        print("\nThat is not a valid choice.")
        
    print("\nThank you. Your double-double is","$","%.2f." %fmenu.get("double-double"))
                   

#regular fries                    
elif yourOrder == 'regular fries' or yourOrder =='fries' or yourOrder =='regular':
    print("\nYou've ordered regular fries.")
     
    animalStyle= input("\nFor an extra .75 you can order your fries animal style. \nWould you like animal style? \n (yes / no / what is animal style)")
    animalStyle = animalStyle.lower()
     
    if animalStyle[0] == 'y' or  animalStyle == 'yes':
        print("OK, you want animal style fries.")
    elif animalStyle[0] == 'n' or animalStyle == 'no':
        print("OK, regular fries only.")
    elif animalStyle[0] == 'w' or animalStyle == 'what' or animalStyle == 'what is animal style' or animalStyle == 'what is animal style?':
        ResponseAnimal = input("Our classic hand-crafted fries with organic chedar cheese melted with onions and spread. A meal in itself. \n Care to try (yes / no)")
        if ResponseAnimal[0] == 'y' or ResponseAnimal == 'yes':
            print("Animal-style fries it is. That will be","$","%.2f" %fmenu.get("animal-style fries"))
        elif ResponseAnimal[0] == 'n' or ResponseAnimal == 'no':
            print("OK, so regular fries it is. That will be","$","%.2f" %fmenu.get("regular fries")) 
        else:
            print("Choose between regular or animal style fries.")

    forHere = input("\nIs this order for here, or to go: (for here / to go)")
    forHere = forHere.lower()
    if forHere[0] == 'f' or forHere == 'for here' or forHere =="here":
        print("OK, you're eating here.")
    elif forHere[0] == 't' or forHere =='to go':
        print("OK, your order is to go.")
    else:
        print("That is not a valid choice.")
        
                  
#animal style fries
elif yourOrder == 'animal-style fries':
    print("\n'Legend' has it that animal style fries are an ancient recipe passed down from Mr. Potato.")

    confirm = input("\nBack to your order. You want animal-style fries: (yes / no)")
    confirm = confirm.lower()
    
    if confirm[0] == 'y' or confirm == 'yes':
        print("\nOne order of animal style fries coming up. That will be","$","%.2f." %fmenu.get('animal-style fries'))
    else:
        print("\nYou canceled the order.")
        
    forHere = input("\nIs this order for here, or to go: (for here / to go)")
    forHere = forHere.lower()
    if forHere[0] == 'f' or forHere == 'for here' or forHere =="here":
        print("\nOK, you're eating here.")
    elif forHere[0] == 't' or forHere =='to go':
        print("\nOK, your order is to go")
    else:
        print("\nThat is not a valid choice")
        

 #five-by-five, eg: http://i.huffpost.com/gen/817769/images/o-INNOUTBURGER-facebook.jpg
elif yourOrder == '5x5' or yourOrder =='five-by-five' or yourOrder =='5b5' or yourOrder == 'five by five':
    charitableDonation = input("\nWould you like to make a one-time tax-deductible donation to \n\n'Protectors of Fuzzy Animals That Live in the Rainforest?' \n\nThey're a non-profit helping fight rainforest deforrestation due to cattle ranching. (yes / no)")
    charitableDonation = charitableDonation.lower()

    if charitableDonation[0] == 'n' or charitableDonation =='no':
        print("\nOne of such magnitude who can command burgers of enormous power \nneedent be concerned with such pedestrian requests.")
    if charitableDonation[0] == 'y' or charitableDonation =='yes':
        howMuch = int(input("\nExcellent! How much would you like to donate: "))
        if howMuch > 0:
            print ("\nThank you so much for donating","$", "%.2f", howMuch)
        else:
            print("\nWe accept monitary donations only, so by default you will donate the cost of your meal.")
            
    confirmCheese = input("\nBack to your order. Do you want cheese on your 5x5? (yes / no / maybe)")
    confirmCheese = confirmCheese.lower()

    if confirmCheese[0] == 'm' or confirmCheese == 'maybe':
        totalCheese = int(input("\nYour restraint shows discipline worthy of a king;  \nHow many slices would you like: "))
        if totalCheese < 5 and totalCheese >= 2:
            print ("\nYou've requested", totalCheese, "slices of cheese")
            print("\nOne 5x5 with",totalCheese, "slices of cheese. That will be","$","%.2f" %fmenu.get('five-by-five'))
    elif confirmCheese[0] == 'y' or confirmCheese == 'yes':
        print("\nA meal fit for a conqueror. One 5x5 with 5 slices of cheese will be","$","%.2f" %fmenu.get('five-by-five'))
    elif confirmCheese[0] == 'n' or confirmCheese == 'no':
        areYouSure = input("\nOh magnanimous one, I beg you to reconsider.\n A 5x5 without cheese is an ocean without water. Consider all the fish.  \n Are you absolutely sure you wish to decline cheese on your 5x5? \n (Yes / No)")
        areYouSure = areYouSure.lower()
        if areYouSure[0] == 'y' or areYouSure == 'yes':
            print("\na 5x5 without cheese is against our custom at 'In N Out'. Your order is canceled!")
        elif areYouSure[0] =='n' or areYouSure == 'no':
            justKidding = int(input("\nI must confess my relief. How many slices would you like: "))
            print("\nOne 5x5 with",justKidding, "slices of cheese. That will be","$","%.2f." %fmenu.get('five-by-five'))
    else:
        print("\nIf you can't handle the order, you can't handle the burger. Order declined.")


    forHere = input("\nIs this order for here, or to go? (for here / to go)")
    forHere = forHere.lower()
    if forHere[0] == 'f' or forHere == 'for here' or forHere =="here":
        print("\nOK, you're eating here.")
        needBib = input("\nWould you like a complimentary bib: (yes / no)")
        needBib = needBib.lower()
        if needBib[0] == 'y' or needBib == 'yes':
            print("\nExcellent decision.")
        elif needBib[0] == 'n' or needBib == 'no':
            print("\nAs you wish.")
        else:
            print("\nCome again? By default, here is a complementary bib")
    elif forHere[0] == 't' or forHere =='to go':
        print("\nOK, your order is to go.")
    else:
        print("\nThat is not a valid choice.")


  
            
 
#three by three
#flying-dutchman
#double-double protein style
#milkshake
#neopolitian
#soda
    

                



