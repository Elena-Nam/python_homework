# 10.4 Python Closures

def make_secret(secret):
    def did_you_guess(guess):
        if guess == secret:
            print("You got it!")
        else:
            print("Nope")
    return did_you_guess

game1 = make_secret("swordfish")
game2 = make_secret("magic")

game1("magic") # Prints nope
game1("swordfish") # Prints you got it
game2("magic") # Prints you got it

# Equivalent Behavior Without Closure (using a class for comparison)
class SecretGame:
    def __init__(self, secret):
        self.secret = secret

    def did_you_guess(self, guess):
        if guess == self.secret:
            print("You got it!")
        else:
            print("Nope")

game1 = SecretGame("swordfish")
game2 = SecretGame("magic")

game1.did_you_guess("magic")
game1.did_you_guess("swordfish")
game2.did_you_guess("magic")

# with nonlocal
def make_secret(secret):
    bad_guesses = 0
    def did_you_guess(guess):
        nonlocal bad_guesses
        if guess == secret:
            print("You got it!")
        else:
            bad_guesses+=1
            print(f"Nope, bad guesses: {bad_guesses}")
    return did_you_guess

game1 = make_secret("swordfish")
game1("magic") # Prints nope, bad guesses 1
game1("magic") 

# Decorators
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius ** 2

    @property
    def diameter(self):
        return 2 * self.radius
    
c = Circle(3)
print(c.area)    
print(c.diameter) 

c.radius = 5
print("New output", c.area)