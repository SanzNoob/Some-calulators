# Calculator
# Variables




mass_units = {
    "kilograms": "kg",
    "grams": "g"
}
while True:
    try:
        user_name = str(input("What's is your name?"))
        looking_for = str(input("Are you looking for the mass, the momentum, or the velocity?"))
        looking_for = looking_for.lower()
        break
    except ValueError:
        print("It seems that you did not select one of the options or mispelling one of the words. Try again.")


def come_back():
    come_ = str(input("Are you looking for the mass, the momentum, or the velocity?"))


def mass_(momentum, velocity, unit):
    result_mass = momentum / velocity
    print("The answer is {} {}".format(result_mass, unit))    


def momentum_(mass, velocity):
    result_momentum = mass * velocity
    print("The answer is {} {}". format(result_momentum, "N"))


def velocity_(momentum, mass):
    result_velocity = momentum / mass
    print("The answer is {} {}".format(result_velocity, "m/s"))
    
     
if "mass" == looking_for:
    print("Mass? Alright!")
    while True:
        try:
            unit_ = str(input("grams or kilograms?").lower().strip())
            if "grams" or "g" or "kilograms" or "kg" == unit_:
                print("{}? Okay".format(unit_))
                break
        except ValueError:
            print("Please, select one of the measuments shown. We do not provide the other ones. They will be implemented in future updates.")
    value_v = float(input("What's the velocity?"))
    value_p = float(input("What's the momentum?"))
    mass_(value_v, value_p, unit_)


if "velocity" == looking_for:
    print("Velocity? Alright!")
    value_p = float(input("What's the momentum?"))
    value_m = float(input("What's the mass?"))
    velocity_(value_p, value_m)


if "momentum" == looking_for:
    print("Momentum? Alright!")
    value_m = float(input("What's the mass?"))
    value_v = float(input("What's the velocity?"))   
    momentum_(value_m, value_v)
     