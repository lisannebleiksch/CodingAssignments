# Add your code after this line

def greet(name, greeting="Hello, <name>!"):
    x = greeting.replace("<name>", name)
    return x


def force(mass, body='earth'):
    gravity_dictionary = {
        'sun': 274,
        'jupiter': 24.9,
        'neptune': 11.2,
        'saturn': 10.4,
        'earth': 9.8,
        'uranus': 8.8,
        'venus': 8.8,
        'mars': 3.7,
        'mercury': 3.7,
        'moon': 1.6,
        'pluto': 0.6
    }
    if body not in gravity_dictionary:
        raise ValueError(f"Unknown body: {body}")
    force = mass * gravity_dictionary[body]
    return round(force, 2)


def pull(m1, m2, d):
    if d <= 0:
        raise ValueError("Distance must be greater than 0")
    G = 6.674 * 10**-11
    gravitional_pull = G * ((m1*m2)/d**2)
    return gravitional_pull


def main():
    print(greet("Bob"))
    print(force(70))
    print(pull(1800, 1500, 3))
    
# look this up
if __name__ == '__main__':
    main()