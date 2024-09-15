class Flight:
    def __init__(self, flight_number, origin, destination, seats_available):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.seats_available = seats_available
        self.passengers = []

    def book_ticket(self, passenger):
        if self.seats_available > 0:
            self.passengers.append(passenger)
            self.seats_available -= 1
            print(f"Ticket booked for {passenger.name} on flight {self.flight_number}")
        else:
            print("No seats available.")

    def cancel_ticket(self, passenger):
        if passenger in self.passengers:
            self.passengers.remove(passenger)
            self.seats_available += 1
            print(f"Ticket for {passenger.name} has been canceled.")
        else:
            print(f"{passenger.name} does not have a ticket on flight {self.flight_number}.")

    def show_passenger_list(self):
        if len(self.passengers) == 0:
            print("No passengers on this flight.")
        else:
            print(f"Passengers on flight {self.flight_number}:")
            for passenger in self.passengers:
                print(f"- {passenger.name}")


class Passenger:
    def __init__(self, name, passport_number):
        self.name = name
        self.passport_number = passport_number


class AirportManagementSystem:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)
        print(f"Flight {flight.flight_number} added.")

    def remove_flight(self, flight_number):
        flight = self.get_flight(flight_number)
        if flight:
            self.flights.remove(flight)
            print(f"Flight {flight_number} removed.")
        else:
            print(f"Flight {flight_number} not found.")

    def get_flight(self, flight_number):
        for flight in self.flights:
            if flight.flight_number == flight_number:
                return flight
        return None

    def list_flights(self):
        if len(self.flights) == 0:
            print("No flights available.")
        else:
            print("Available flights:")
            for flight in self.flights:
                print(f"{flight.flight_number}: {flight.origin} to {flight.destination} - Seats Available: {flight.seats_available}")


def main():
    airport_system = AirportManagementSystem()

    while True:
        print("\nAirport Management System")
        print("1. Add Flight")
        print("2. Remove Flight")
        print("3. List Flights")
        print("4. Book Ticket")
        print("5. Cancel Ticket")
        print("6. Show Passenger List")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            flight_number = input("Enter flight number: ")
            origin = input("Enter flight origin: ")
            destination = input("Enter flight destination: ")
            seats = int(input("Enter number of available seats: "))
            flight = Flight(flight_number, origin, destination, seats)
            airport_system.add_flight(flight)

        elif choice == '2':
            flight_number = input("Enter flight number to remove: ")
            airport_system.remove_flight(flight_number)

        elif choice == '3':
            airport_system.list_flights()

        elif choice == '4':
            flight_number = input("Enter flight number to book: ")
            flight = airport_system.get_flight(flight_number)
            if flight:
                name = input("Enter passenger name: ")
                passport_number = input("Enter passport number: ")
                passenger = Passenger(name, passport_number)
                flight.book_ticket(passenger)
            else:
                print("Flight not found.")

        elif choice == '5':
            flight_number = input("Enter flight number to cancel: ")
            flight = airport_system.get_flight(flight_number)
            if flight:
                name = input("Enter passenger name: ")
                passenger = None
                for p in flight.passengers:
                    if p.name == name:
                        passenger = p
                        break
                if passenger:
                    flight.cancel_ticket(passenger)
                else:
                    print(f"No passenger found with name {name}.")
            else:
                print("Flight not found.")

        elif choice == '6':
            flight_number = input("Enter flight number to show passengers: ")
            flight = airport_system.get_flight(flight_number)
            if flight:
                flight.show_passenger_list()
            else:
                print("Flight not found.")

        elif choice == '7':
            print("Exiting system...")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
