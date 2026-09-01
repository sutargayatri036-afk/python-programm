import random

characters = ["a brave astronaut", "a mysterious wizard", "a clever detective", "a friendly robot"]
places = ["on Mars", "in an enchanted forest", "under the ocean", "inside a haunted castle"]
events = [
    "discovered a hidden treasure",
    "met a talking dragon",
    "found a secret portal",
    "accidentally became the king"
]

character = random.choice(characters)
place = random.choice(places)
event = random.choice(events)

print("🎲 RANDOM ADVENTURE 🎲")
print(f"One day, {character} was exploring {place}.")
print(f"Suddenly, they {event}!")
print("What happens next? Nobody knows! 😄")
