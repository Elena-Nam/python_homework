# Write your code here.
# Task 1
def hello():
    return ("Hello!")

print("Task 1:", hello())

# Task 2
def greet(name):
    return ("Hello, " + name + "!")

print("Task 2:", greet("Elena"))

# Task  3
def calc(num1, num2, operation = "multiply"):
 try:
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
       return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise ZeroDivisionError
        return num1 / num2
    elif operation == "modulo":
       return num1 % num2
    elif operation == "//":
       if num2 == 0:
            raise ZeroDivisionError
       return num1 // num2
    else:
        return "Invalid operation"
 except TypeError:
    return "You can't multiply those values!"
 except ZeroDivisionError:
    return "You can't divide by 0!"

print("Task 3:", calc(10, 5, "add"))


# Task 4
def data_type_conversion(value, type):
   try:
    if type == "float":
        return float(value)
    elif type == "int":
        return int(value)
    elif type == "str":
        return str(value)   
    else:
       return f"The non-converted value:", {type}
   except (ValueError, TypeError):
    return f"You can't convert {value} into a {type}."

print("Task 4:", data_type_conversion(123, "float"))


# Task 5
def grade(*args):
    try:
        if not all(isinstance(arg, (int, float)) for arg in args):
            raise ValueError("Invalid data was provided.")
        total = sum(args) / len(args)
        if total >= 90:
            return "A"
        elif total >= 80:
            return "B"
        elif total >= 70:
            return "C"
        elif total >= 60:
            return "D"
        else:
            return "F"
    except ValueError as e:
        return str (e)

print("Task 5:", grade(86, 100, 90))
print("Task 5:", grade("apple", "banana", "kiwi" ))
       

# Task 6
def repeat(str, count):
    result = ""
    for _ in range (count):
      result  += str
    return result

print("Task 6:", repeat("a", 5))


# Task 7
def student_scores(*args, **kwargs):
    parameter = args [0]
    if parameter == "best":
        highest_score_student = max(kwargs, key=kwargs.get)
        return highest_score_student
    elif parameter == "mean":
        average = sum(kwargs.values()) / len(kwargs)
        return average
    else:
        return "Invalid data"

print("Task 7:", student_scores("mean", Tom=75, Dick=89, Angela=91))
print("Task 7:", student_scores("best", Tom=75, Dick=89, Angela=91))


# Task 8
def titleize(str):
   little_words = {"a", "on", "an", "the", "of", "and", "is", "in", "or", "to"}
   words = str.split()
   words[0] = words[0].capitalize()
   words[-1] = words[-1].capitalize()
   for i in range(1, len(words) - 1):
        if words[i].lower() not in little_words:
            words[i] = words[i].capitalize()
        else:
            words[i] = words[i].lower()
   return " ".join(words)
 
print("Task 8:", titleize("to be, or not to be"))


# Task 9
def hangman(secret, guess):
    guessed_word = ""
    for letter in secret:
        if letter in guess:
            guessed_word += letter  
        else:
            guessed_word += "_"
    return guessed_word

print("Task 9:", hangman("alphabet", "abc"))


# Task 10
def pig_latin(word):
    vowels = "aeiou"
    if word[0].lower() in vowels:
        return word + "ay"
    elif word[:2].lower() == "qu":
        return word[2:] + "quay"
    else:
        for i, letter in enumerate(word):
            if letter.lower() in vowels:
                return word[i:] + word[:i] + "ay"
        return word + "ay"


print("Task 10:", pig_latin("apple"))
print("Task 10:", pig_latin("banana"))
print("Task 10:", pig_latin("queue"))
print("Task 10:", pig_latin("clock"))
print("Task 10:", pig_latin("square")) # can't find the solution
