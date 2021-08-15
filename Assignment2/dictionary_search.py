import requests


class DictionartAPI:

    api_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"

    def __init__(self, word):
        self.word = word

    def get_meaning(self):
        response = requests.get(f"""{DictionartAPI.api_url}{self.word}""")

        result = response.json()[0]
        meanings = result.get("meanings")

        output_meanings = ""
        for meaning in meanings:
            part_of_speech, definition = meaning.values()
            output_meanings += f"""{self.word}. {part_of_speech}. {definition[0].get("definition")}\n"""

        return output_meanings


if __name__ == "__main__":
    input_word = input("Word? ")
    meanings = DictionartAPI(input_word).get_meaning()

    print(f"""Output:\n{meanings}""")
