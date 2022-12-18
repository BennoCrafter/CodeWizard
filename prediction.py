import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load the dataset and drop any rows with missing or invalid labels
df = pd.read_csv("code_snippets.csv")
df = df.dropna(subset=["is_for_loop"])

# Split the data into input features (X) and output labels (y)
X = df["code"]
y = df["is_for_loop"]

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocess the input features by using a CountVectorizer to convert the code snippets into numerical values
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# Train a Multinomial Naive Bayes classifier on the training data
clf = MultinomialNB()
clf.fit(X_train, y_train)

# Ask the AI whether the following code snippet is a for loop or not
code_snippet = input("Input:")
prediction = clf.predict(vectorizer.transform([code_snippet]))
if prediction[0] == 1:
    prediction = "Is for loop."
elif prediction[0] == 0:
    prediction = "is any code."
print("Prediction:", prediction)
