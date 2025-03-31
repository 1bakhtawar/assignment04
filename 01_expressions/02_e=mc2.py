def main():
    c: float = 299792458
    mass_in_kg: float = float(input("Enter kilos of mass: "))
    energy_in_joules: float = mass_in_kg * (c ** 2)
    print("e = m*c^2")
    print("Mass = " + str(mass_in_kg))
    print("C = "+ str(c) + "m/s")
    print("e = " + str(mass_in_kg * c ** 2) + "jules")
    # print(float(energy_in_joules) + " joules of energy!")

if __name__ == '__main__':
    main()