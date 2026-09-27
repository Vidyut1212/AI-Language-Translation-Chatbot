from googletrans import Translator

def translation_bot():
    translator = Translator()
    print("--- AI Language Translation Chatbot ---")
    print("Type 'quit' to exit.")
    
    while True:
        text = input("\nYou: ")
        if text.lower() == 'quit': 
            break
            
        target_lang = input("Target language code (e.g., 'es' for Spanish, 'fr' for French): ")
        try:
            translated = translator.translate(text, dest=target_lang)
            print(f"Bot: {translated.text}")
        except Exception:
            print("Bot: Error processing translation. Please verify the language code.")

if __name__ == "__main__":
    translation_bot()
