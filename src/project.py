import re

def analyze_text(file_path : str):
    with open(file_path, encoding='utf-8') as file:
        text = file.read()

    # count amount of sentence enders
    sentences = re.findall(r'\.\.\.|[.!?]', text)
    sentence_count = len(sentences)

    # count amount of words in text
    words = re.split(r'[ ,:;]+', text)
    words = [w for w in words if w.strip() != ''] # if no words given
    word_count = len(words)

    return word_count, sentence_count

def main():
    file_path = "C:\\Users\\Ghost\\Desktop\\Univ\\Document_data.txt"

    words, sentences = analyze_text(file_path)

    print(f"Words count: {words}")
    print(f"Sentence count: {sentences}")

main()