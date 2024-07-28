# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

def suggestFood(species, age):
    if species.lower() == "dog" and age < 2:
        return "Puppy food"
    elif species.lower() == 'cat' and age > 5:
        return "Senior cat food"
    else: 
        return "Not Available"
    
species = input('Enter the specie of the animal: ')
age = int(input('Enter the age of the animal: '))
print(suggestFood(species, age))