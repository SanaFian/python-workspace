# ============================================
# Project 02: Simple Text Analyzer
# ============================================

def analyze_text():
    text = input("Enter a sentence to analyze: ")

    if not text:
        print("Please enter something!")
        return

    # 1. Length of string
    print(f"\nTotal characters (including spaces): {len(text)}")

    # 2. Split into words
    words = text.split()
    print(f"Total words: {len(words)}")

    # 3. String Slicing (Reverse)
    print(f"Reversed text: {text[::-1]}") 

    # 4. Uppercase & Lowercase
    print(f"Uppercase: {text.upper()}")
    print(f"Lowercase: {text.lower()}")

    # 5. Checking for specific word
    target = input("\nEnter a word to check if it exists: ")
    if target in text:
        print(f"Yes, '{target}' is in the text.")
    else:
        print(f"No, '{target}' was not found.")

if __name__ == "__main__":
    analyze_text()
