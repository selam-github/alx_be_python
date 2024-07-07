#shopping_list_manager.py
def display_menu():
        print("Shopping List Manager")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View List")
        print("4. Exit")
def main(): 
   shopping_list = []
   while True:
        display_menu()
        choice = input("Enter your choice (1-4): ") # select from the above condition      if choice == '1':
         item = input("Enter the  item to add:")
         shopping_list.append(item)
         print(f"'{item}' has been added to the list.")
      elif choice == '2':
         if shopping_list == 0:
             print("The list is empty.")
         else:
             item = input("Enter item to remove: ")
              if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"'{item}' has been removed from the list.")
              else:
                     print(f"'{item}' is not in the list.")
      elif choice == '3':
           if shopping_list == 0:
               print("The list is empty.")
           else:
               print("Shopping List:")
                 for item in shopping_list:
                     print(f"- {item}")
      elif choice == '4':
                 print("Exiting the Shopping List Manager. Goodbye!")
                             break
      else:
            print("Invalid choice. Please enter a number from 1 to 4.")
        
if __name__ == "__main__":
        main()


