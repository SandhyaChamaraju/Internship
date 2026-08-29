class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def get_status(self):
        print(f"--- Train Status: {self.name} ---")
        print(f"Available Seats: {self.seats}")

    def get_fare_info(self):
        print(f"Ticket Fare per person: ₹{self.fare}")

    def book_ticket(self):
        if self.seats > 0:
            print(f"Ticket successfully booked for {self.name}!")
            self.seats -= 1 
            print(f"Remaining seats: {self.seats}\n")
        else:
            print(f"Sorry, {self.name} is fully booked.\n")

rajdhani = Train("Rajdhani Express (12301)", fare=2500, seats=2)

rajdhani.get_status()
rajdhani.get_fare_info()

rajdhani.book_ticket()
rajdhani.book_ticket()  
rajdhani.book_ticket()  
