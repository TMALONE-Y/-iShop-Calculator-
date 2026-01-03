'''
This project was made by 

yazan abushareefih

university -------> Jordan University of Science and Technology (JUST)
'''

items = []
price = []

print("Welcom to ishop calculater ")

number_of_item = int(input("How many items in ur bastek today ? "))

if number_of_item > 0:
    
    print("\nlet's get to counting them ...... ")
    
    for i in range (0,number_of_item):
        
        name = input(f"\nplz tell me the name of the item number {i + 1}:  ") 
        items.append(name)
        
        price_of_item = float (input(f"\nPlz tell me price of the {name} $: "))
        price.append(price_of_item)
    
    choice = input("\nIF u want to see ur entire basket items: (yes/no) ").lower().strip()
    if choice == 'yes':
        print(items)
    else:
        print("\nThank u to use the ishop calculater ")
        
    sum_price = input("\nWould you like to see how much it'll cost? (yes/no) ").lower().strip()
    if sum_price == 'yes':
       total = sum(price)
       print(f"\nBuying these items will cost: {total:.2f} $")
       
    else:
        print("\nThank u to use the ishop calculater ")
        
else:
    print("Oops! You haven't bought anything yet.")