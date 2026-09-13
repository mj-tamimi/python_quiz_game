name = input("What is your name? ")
game = input("Enter a game: ")

q = f"Rate '{game}' from 1 to 5: "

while True:
    rate = int(input(q))
    
    if (rate >= 1) and (rate <= 5):
        break
    else:
        print("⚠︎ Please enter a valid number from 1 to 5")
        continue


review = input("Write a short review: ")

with open("game_reviews.txt", "a") as file:
    file.write(f"{name} - {game} - {rate} - {review}\n")
    
print("Your review was saved. Thank you!")