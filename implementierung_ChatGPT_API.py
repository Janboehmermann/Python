import openai

class ChatGPT:
    def __init__(self, api_key, rolle):
        openai.api_key = api_key
        self.dialog = [{"rolle": "system", "content": rolle}]

    def antworten(self, frage):
        self.dialog.append({"rolle":"user","content":frage})
        ergebnis = openai.Completion.create(
            model='davinci',
            prompt=self.dialog,
            temperature=0.7,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        antwort = ergebnis.choices[0].text
        self.dialog.append({"rolle":"assistant","content":antwort})
        return antwort