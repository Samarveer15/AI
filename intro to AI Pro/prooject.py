import random
class AI:
    def __init__(self, name="AI"):
        self.name = name
        self.emotions = ["happy", "curious", "thoughtful", "excited", "calm"]
        self.topics = [
            "artificial intelligence",
            "space exploration",
            "favorite books",
            "technology trends",
            "hobbies"
        ]
        self.current_emotion = random.choice(self.emotions)
    def greet(self):
        return f"Hello, I am {self.name}! Today, I feel {self.current_emotion}."
    def suggest_topic(self):
        topic = random.choice(self.topics)
        return f"Would you like to talk about {topic}?"
    def interact(self):
        print(self.greet())
        print(self.suggest_topic())
        user_input = input("What would you like to talk about? ")
        if any(topic in user_input.lower() for topic in self.topics):
            print(f"Great! I love discussing {user_input}.")
        else:
            print("That's interesting! Tell me more.")
if __name__ == "__main__":
    ai = AI()
    ai.interact()