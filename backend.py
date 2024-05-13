#main functions for the chatbot
import openai
import os

key = input("Enter the API key")
key_str = str(key)
os.environ["API_KEY"] = key_str
openai.api_key = os.getenv("API_KEY")
class GermanTeacher:
    def __init__(self):
        print("Hey, I am Lisa, your German teacher...\n")

    def correct_sentence(self, user_input):
        prompt = f"Correct the following sentence in German:{user_input}"
        return prompt

    def explain_mistake(self, user_input):
        prompt = f"Compare both the sentences and explain the mistakes:{user_input}"
        return prompt

    def translate_to_german(self, sentence):
        prompt = f"Translate the following sentence to german:{sentence}"
        return prompt

    def create_random_sentence(self):
        response = openai.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt="Generate a random english sentence that is used in everyday conversation",
            temperature=0.9,
            max_tokens=200,
        )
        return response.choices[0].text

    def response_gpt(self, sentence):
        response = openai.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=sentence,
            temperature=0.1,
            max_tokens=200,
        )
        return response.choices[0].text
    
    def generate_image(self):
        response = openai.images.generate(
            model = "dall-e-3",
            prompt = "an everyday scenario",
            size = "1024x1024",
            quality = "standard",
            n = 1,
        )
        return response.data[0].url


    def start(self):
        while True:
            print("Choose an option:")
            print("1. Generate a random English sentence to translate.")
            print("2. Generate a scene and describe it in German.")
            print("3. Enter a sentence in German.")
            print("4. Exit")

            choice = input("Enter your choice (1/2/3/4): ")

            if choice == "1":
                random_sen = self.create_random_sentence()
                print("English Sentence:", random_sen)
                user_input = input("Enter the translated sentence in German: (type 'exit' to leave): ")

            elif choice == "2":
                scene = self.generate_image()
                print("Describe the scene in German:", scene)
                user_input = input("Your description in German: (type 'exit' to leave): ")

            elif choice == "3":
                user_input = input("Enter a sentence in German: (type 'exit' to leave): ")

            elif choice == "4":
                print("Exiting program.")
                break

            if user_input.lower() == "exit":
                print("Exiting program.")
                break

            corrected_sentence = self.correct_sentence(user_input)
            response_from_gpt = self.response_gpt(corrected_sentence)

            if "no mistakes" in response_from_gpt.lower():
                print("Good Job! Your sentence has no mistakes.")
            else:
                print("I will explain where you went wrong...")
                print("Here is the corrected sentence :)")
                print(response_from_gpt)

                corrected_with_user_input = user_input + " " + response_from_gpt
                explanation = self.explain_mistake(corrected_with_user_input)
                response_from_gpt = self.response_gpt(explanation)
                print(response_from_gpt)
            

if __name__ == "__main__":
    german_teacher = GermanTeacher()
    german_teacher.start()
