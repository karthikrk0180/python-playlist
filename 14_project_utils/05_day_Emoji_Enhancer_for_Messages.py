import string

emoji_map = {
    "love": "❤️",
    "happy": "😊",
    "code": "💻",
    "tea": "🍵"
}

def get_input():
    return input("\nEnter the message: ").lower().strip()

def enhance_with_emoji(input_text):
    enhanced_words = []
    words = input_text.split()
    
    for word in words:
        cleaned_word = word.strip(string.punctuation)
        emoji = emoji_map.get(cleaned_word,"")
        enhanced_words.append(word+emoji+" ")
        
    return " ".join(enhanced_words)

def main():
    while True:
        print("\nWelcome to Emoji Enhancer!")
        input_text = get_input()
        print("Original:", input_text)

        enhanced = enhance_with_emoji(input_text)
        print("Enhanced:", enhanced)

if __name__ == "__main__":
    main()
