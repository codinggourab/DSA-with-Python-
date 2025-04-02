class Polynomial:
    def __init__(self):
        self.coefficients = []

    def create(self):
        # Input polynomial coefficients
        degree = int(input("Enter the degree of the polynomial: "))
        self.coefficients = []

        for i in range(degree + 1):
            coeff = float(input(f"Enter the coefficient of x^{i}: "))
            self.coefficients.append(coeff)

    def display(self):
        # Display the polynomial in a human-readable form
        poly_str = ""
        degree = len(self.coefficients) - 1

        for i in range(degree, -1, -1):
            coeff = self.coefficients[i]
            if coeff != 0:
                if i == degree:
                    poly_str += f"{coeff}x^{i}" if i != 0 else f"{coeff}"
                else:
                    if coeff > 0:
                        poly_str += f" + {coeff}x^{i}" if i != 0 else f" + {coeff}"
                    elif coeff < 0:
                        poly_str += f" - {-coeff}x^{i}" if i != 0 else f" - {-coeff}"

        if poly_str == "":
            print("The polynomial is 0.")
        else:
            print(f"The polynomial is: {poly_str}")

    def add(self, other):
        # Add two polynomials by adding their coefficients
        max_len = max(len(self.coefficients), len(other.coefficients))

        # Pad the smaller polynomial with zeros
        self_coeffs = self.coefficients + [0] * (max_len - len(self.coefficients))
        other_coeffs = other.coefficients + [0] * (max_len - len(other.coefficients))

        # Add the coefficients
        result_coeffs = [self_coeffs[i] + other_coeffs[i] for i in range(max_len)]

        # Return a new Polynomial object with the result
        result_poly = Polynomial()
        result_poly.coefficients = result_coeffs
        return result_poly


def menu():
    poly1 = Polynomial()
    poly2 = Polynomial()

    while True:
        print("\nMenu:")
        print("1. Create First Polynomial")
        print("2. Create Second Polynomial")
        print("3. Display First Polynomial")
        print("4. Display Second Polynomial")
        print("5. Add Polynomials")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            poly1.create()
        elif choice == 2:
            poly2.create()
        elif choice == 3:
            poly1.display()
        elif choice == 4:
            poly2.display()
        elif choice == 5:
            result = poly1.add(poly2)
            print("The sum of the two polynomials is:")
            result.display()
        elif choice == 6:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

# Run the menu-driven program
menu()
