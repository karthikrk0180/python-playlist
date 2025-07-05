animal = input("Enter the type of Animal: ")
age = int(input("Enter the age of the Animal: "))

if animal.lower() == "dog" and age < 2:
    print("Eat Puppy Food")
elif animal.lower() == "cat" and age > 5:
    print("Cat Food")
    