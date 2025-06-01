import nltk
import re
import heapq
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('punkt')
nltk.download('stopwords')
def summarize_text(text, num_sentences=3):
    text = re.sub(r'\s+', ' ', text).strip()
    sentences = sent_tokenize(text)
    if len(sentences) < num_sentences:
        num_sentences = len(sentences)
    stop_words = set(stopwords.words('english'))
    word_freq = {}
    for word in word_tokenize(text.lower()):
        if word.isalnum() and word not in stop_words:
            word_freq[word] = word_freq.get(word, 0) + 1
    max_freq = max(word_freq.values(), default=1)
    for word in word_freq:
        word_freq[word] /= max_freq
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
              sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_freq[word]
    summary_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    return ' '.join(summary_sentences)
if __name__ == "__main__":
    print("========== TEXT SUMMARIZATION TOOL ==========")
    input_text = input("\nPaste your article or paragraph:\n\n")
    summary = summarize_text(input_text, num_sentences=3)

    print("\n========== SUMMARY ==========")
    print(summary)
