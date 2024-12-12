# Twitter Sentiment Analysis on IPL Content

## Project Description
This project involves sentiment analysis of tweets related to the Indian Premier League (IPL). The primary goal is to classify sentiments expressed in tweets as positive, negative, or neutral using Natural Language Processing (NLP) techniques and machine learning models.

---

## Table of Contents
1. [Dataset](#dataset)
2. [Technologies Used](#technologies-used)
3. [Steps Involved](#steps-involved)
4. [Data Preprocessing](#data-preprocessing)
5. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
6. [Model Training and Evaluation](#model-training-and-evaluation)
7. [Results](#results)
8. [Future Improvements](#future-improvements)
9. [How to Run](#how-to-run)

---

## Dataset
The dataset for this project was collected directly from Twitter using the `twikit` library. The dataset contains the following columns:
- `Username`: Twitter username of the tweet's author
- `Location`: Location of the user
- `Likes`: Number of likes on the tweet
- `Text`: The tweet content
- `Month`: Month when the tweet was posted
- `Year`: Year when the tweet was posted

---

## Technologies Used
- **Python**: Programming language
- **Libraries**: 
  - Data Analysis: `pandas`, `numpy`
  - Visualization: `matplotlib`, `seaborn`, `wordcloud`
  - NLP: `nltk`, `TextBlob`, `TfidfVectorizer`
  - Machine Learning: `scikit-learn`
- **Tools**: Twikit library for tweet collection

---

## Steps Involved

### 1. Data Collection
- Tweets were retrieved using the `twikit` library with the query `ipl lang:en`.

### 2. Data Preprocessing
- Handling missing values
- Formatting date and time
- Removing emojis, URLs, special characters, and extra spaces
- Converting text to lowercase
- Tokenization and stemming using `nltk`

### 3. Exploratory Data Analysis (EDA)
- WordCloud for most frequently used words
- Pie chart for sentiment distribution
- Bar chart showing sentiment distribution by location
- Boxplot for `Likes` vs `Sentiment`

### 4. Sentiment Classification
- Polarity-based sentiment analysis using `TextBlob`
- Classification into `positive`, `negative`, and `neutral` categories

### 5. Model Training and Evaluation
- Feature extraction using `TfidfVectorizer` with n-grams
- Models used:
  - Logistic Regression
  - Random Forest Classifier
  - Naive Bayes
- Hyperparameter tuning with GridSearchCV
- Performance evaluation using metrics like accuracy, classification report, and cross-validation scores

---

## Data Preprocessing
Key preprocessing steps:
- Removing missing values in the `Location` column
- Extracting month and year from the tweet creation date
- Cleaning text by removing unnecessary elements like emojis, URLs, and special characters

---

## Exploratory Data Analysis (EDA)
- **WordCloud**: Visualization of commonly used words in IPL tweets
- **Sentiment Distribution**: Pie chart representing the proportion of positive, negative, and neutral tweets
- **Location-based Sentiment Analysis**: Bar chart showing sentiment distribution across different locations
- **Likes vs Sentiment**: Boxplot to analyze how sentiment correlates with tweet likes

---

## Model Training and Evaluation
- **Models**:
  - Logistic Regression: Achieved accuracy of **74.58%**
  - Random Forest: Achieved accuracy of **78.89%**
  - Naive Bayes: Achieved accuracy of **70.72%**
- **Cross-Validation**: Best cross-validation accuracy using Logistic Regression was **79.61%**

---

## Results
- Random Forest Classifier performed the best with an accuracy of **78.89%**
- Logistic Regression showed competitive results with a cross-validation accuracy of **79.61%**
- Visualizations revealed insightful trends in IPL-related tweets

---

## Future Improvements
1. Include additional features like hashtags, mentions, or retweets for better sentiment analysis.
2. Experiment with deep learning models like LSTM or BERT for enhanced text classification.
3. Perform topic modeling to categorize tweets by IPL teams or players.

---
