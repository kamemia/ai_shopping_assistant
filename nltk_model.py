import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Preprocess text by removing stop words, punctuation, and stemming or lemmatizing words
def preprocess_text(text):
    # Tokenize the text into words
    words = word_tokenize(text)

    # Remove stop words and punctuation
    filtered_words = [word.lower() for word in words if word.lower() not in stopwords.words('english') and word.isalnum()]

    # Lemmatize words
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]

    # Join the preprocessed words back into a string
    preprocessed_text = ' '.join(lemmatized_words)

    return preprocessed_text

# Define a sample customer query
query = "What is the price of the iPhone 12 on your website?"

# Preprocess the query text
preprocessed_query = preprocess_text(query)

# Define a labeled dataset
dataset = [("What is the price of the iPhone 12 on your website?", {"category": "price", "product": "iPhone 12"}),
           ("Do you have any discounts on Samsung phones?", {"category": "discounts", "product": "Samsung phones"}),
           ("Can you recommend a good laptop for gaming?", {"category": "recommendation", "product": "laptop"})]

# Extract features from the preprocessed text
def extract_features(text):
    features = {}

    # Add features for individual words and word pairs
    for word in text.split():
        features[word] = True
    for word1, word2 in nltk.bigrams(text.split()):
        features[word1 + ' ' + word2] = True

    return features

# Train an SVM classifier on the labeled dataset
featuresets = [(extract_features(preprocess_text(text)), label) for (text, label) in dataset]
classifier = nltk.classify.SklearnClassifier(nltk.classify.SVC()).train(featuresets)

# Test the classifier on the preprocessed query
query_features = extract_features(preprocessed_query)
predicted_category = classifier.classify(query_features)

print(f"The predicted category for the query '{query}' is '{predicted_category}'.")
