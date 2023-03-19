if __name__ == '__main__':
    with open('api.key', 'r') as api_key:
        API_KEY = api_key.read()
        chat_gpt = ChatGPT(API_KEY, "Sei ein Hacker!")
    while (frage := input('\n> ' )) != 'X':
        antwort = chat_gpt.antworten(frage)
        print(antwort)