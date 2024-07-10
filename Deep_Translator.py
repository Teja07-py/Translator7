!pip install deep_translator
from deep_translator import GoogleTranslator


def translate_text(text, target_language='en'):
    translator = GoogleTranslator(target=target_language)
    translation = translator.translate(text)
    return translation


def main():
    print("Language Translator")
   
    while True:
        user_input = input('Enter text to translate (or type "quit" to exit): ')
       
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
       
        target_language = input('Enter target language code (e.g., "en" for English): ')
       
        try:
            translated_text = translate_text(user_input, target_language)
            print(f'Translation ({target_language}): {translated_text}')
        except Exception as e:
            print(f"Translation failed. Error: {str(e)}")


if __name__ == "__main__":
    main()
