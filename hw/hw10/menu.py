from waitlist import Waitlist
class Menu:
    """A class representing the menu for the restaurant reservation program"""

    def __init__(self):
        """Initialize the menu with the waitlist object"""
        self.waitlist = Waitlist()

    def run(self):
        """Print the main menu"""
        print("Welcome to the Restaurant Reservation System!")
        print("==============================================")
        print("Please select an option:")
        print("1. Add a customer to the waitlist")
        print("2. Seat the next customer")
        print("3. Change the time of a customer's reservation")
        print("4. Peek at the next customer")
        print("5. Print the reservation list")
        print("6. Quit")
        print("")
        while True:
            
            choice = input("Enter your choice (1-6): ")
            print("*************************************************")
            #Each one of these options should call a method from Waitlist class 
            if choice == "1":
                #TODO """Add a customer to the waitlist"""
                name = input("Enter the customer's name: ")
                time = input("Enter the time of the reservation (HH:MM): ")
                self.waitlist.add_customer(item, Time(time[0:1], time[3:4]))
                print(str(name) + " has been added to the waitlist at " + str(time))

            elif choice == "2":
                #TODO"""Seat the next customer"""
                i = self.waitlist.seat_customer()
                print("Seated customer: " + str(i[0]) + ", reservation time: " + str(i.time))

            elif choice == "3":
                #TODO"""Change the time of a customer's reservation"""
                name = input("Enter the customer's name:")
                new_time = input("Enter the new time of the reservation (HH:MM): ")
                self.waitlist.change_reservation(name, Time(new_time[0:1], new_time[3:4]))
                print(str(name) + "'s reservation time has been changed to " + str(new_time))

            elif choice == "4":
                #TODO"""Peek at the next customer"""
                print("The next customer on the waitlist is: " + str(self.waitlist.peek()[0]) + ", reservation time: " + str(self.waitlist.peek()[1]))

            elif choice == "5":
                #TODO"""Print the waitlist"""
                print_reservation_list(self)

            elif choice == "6":
                """exit the program at any time"""
                print("Thank you for using the Restaurant Reservation System!")
                break

            else:
                print("Invalid choice. Try again.")
    
s = Menu()
s.run()