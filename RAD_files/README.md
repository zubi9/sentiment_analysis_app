### Code Description:

#### Cell 1:

- Importing necessary libraries such as `re`, `pickle`, `numpy`, `pandas`, `WordNetLemmatizer` from `nltk`, and various models and utilities from `sklearn`.
- Setting up configurations like dataset columns, dataset encoding, and loading the dataset from a CSV file.
- Preparing the dataset by selecting relevant columns, replacing values, and storing data in lists.
- Defining dictionaries for emojis and a list of stopwords.
- Downloading necessary NLTK resources.

#### Cell 2:

- Initializing `WordNetLemmatizer` for lemmatization.
- Defining a function `preprocess()` to preprocess text data which involves tasks like replacing URLs with 'URL', replacing emojis with their meanings, replacing usernames with 'USER', removing non-alphabetic characters, reducing consecutive characters, removing stopwords, and lemmatizing words.
- Preprocessing the text data and splitting it into train and test sets.
- Vectorizing the text data using `TfidfVectorizer`.

#### Cell 3:

- Defining a function `model_evaluate()` to evaluate models using classification report.
- Training a Bernoulli Naive Bayes model, evaluating its performance, and printing the classification report.
- Training a Linear Support Vector Classifier (SVC) model, evaluating its performance, and printing the classification report.
- Training a Logistic Regression model, evaluating its performance, and printing the classification report.

#### Cell 4:

- Importing `Pipeline` from `sklearn.pipeline`.
- Splitting the preprocessed text data into train and test sets.
- Creating a pipeline consisting of vectorization and Bernoulli Naive Bayes model, fitting the pipeline on the training data, and evaluating its performance.
- Saving the pipeline to a pickle file.

#### Cell 5:

- Loading the saved pipeline from the pickle file.
- Evaluating the loaded pipeline's performance using the `model_evaluate()` function.

#### Cell 6:

- Defining a function `predict()` to predict sentiment for given text using the loaded pipeline.
- Providing a list of sample text for sentiment prediction.
- Making predictions using the `predict()` function and printing the results.