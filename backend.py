#main functions for the chatbot
def correct_sentence(user_input):
    joined = "\n".join(user_input)
    prompt = f"Correct the following sentence in German:\n{joined}"
    return prompt