"""Restaurant rating lister."""


# put your code here

def ratings_res(file):
    ratings = open(file)
    rating_restaurants = {}
    for rating in ratings:
        rating = rating.rstrip()
        lines  = rating.split(":")
        rating_restaurants[lines[0]] = lines[1]
    ratings.close()

def display_res(rating_restaurants):
    key_res = sorted(rating_restaurants.items())
    for name in key_res:
        alpha_name = f"{name[0]} is rated at {name[1]}."
        

def add_res(rating_restaurants):
    prompt_res = input('Enter Restaurant Name: ')
    prompt_rating = int(input('Enter Restaurant Rating: '))
    if prompt_rating > 0 and prompt_rating <= 5:
        rating_restaurants[prompt_res] = prompt_rating
        updated_list = sorted(rating_restaurants.items())
        for name in updated_list:
            print(f"{name[0]} is rated at {name[1]}.")
    else:
        print("Invalid number.")
        prompt_rating = input("Enter a new number between 1 and 5: ")
        rating_restaurants[prompt_res] = prompt_rating
        updated_list = sorted(rating_restaurants.items())
        for name in updated_list:
            print(f"{name[0]} is rated at {name[1]}.")

ratings_res("scores.txt")