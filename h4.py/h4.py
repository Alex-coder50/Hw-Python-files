season = input("Ask me about Summer, and Winter. I will give you tips about the clothing for the season! ")

season = season.strip().capitalize()

if season == "Summer":
    print("Summer", "so you can wear a shirt, shorts and a cap!!!")
elif season == "Winter":
    print("Winter", "so you can wear a warm jacket, a winter cap, pants, and winter boots!!!")
else:
    print("Sorry, I only know about Summer and Winter.")
