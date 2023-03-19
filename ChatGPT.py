if name=='main':
with open('api.key', 'r') as api_key:
sk_wD5wy6Mk77nJ8cboDPnYT3BlbkFJxxEv9ARGYl2AfhtDDxEp = api_key.read()
chat_gpt = ChatGPT(sk_wD5wy6Mk77nJ8cboDPnYT3BlbkFJxxEv9ARGYl2AfhtDDxEp, "Sei ein Hacker!")
while (frage := input('\n> ' )) != 'X':
    antwort = chat_gpt.antworten(frage)
    print (antwort)