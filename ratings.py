"""Restaurant rating lister."""


# put your code here
def ratings_res(file):
    ratings = open(file)
    rating_restaurants = {}
    for rating in ratings:
        rating = rating.rstrip()
        lines  = rating.split(":")
        for line in lines:
            rating_restaurants[lines[0]] = lines[1]
    ratings.close()
    key_res = sorted(rating_restaurants.items())
    for name in key_res:
        print(f"{name[0]} is rated at {name[1]}.")
    prompt_res = input('Enter Restaurant Name: ')
    prompt_rating = input('Enter Restaurant Rating: ')
    rating_restaurants[prompt_res] = prompt_rating
    updated_list = sorted(rating_restaurants.items())
    for name in updated_list:
        print(f"{name[0]} is rated at {name[1]}.")

ratings_res("scores.txt")