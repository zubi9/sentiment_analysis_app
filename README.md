### Utility.py

Sentiment analysis of Twitter data involves analyzing tweets to determine the overall sentiment expressed, typically as positive, negative. Leveraging natural language processing techniques, machine learning models are trained on labeled datasets to classify sentiments. Twitter, being a microblogging platform, provides a rich source of diverse opinions and emotions, making it ideal for sentiment analysis tasks. This analysis finds applications in understanding public opinion, brand monitoring, market research, and gauging social trends. Moreover, sentiment analysis on Twitter data contributes to sentiment-driven decision-making processes in various domains, ranging from business to politics and beyond

![Sentiment Analysis app](../sentiment_analysis_app/RAD_files/data/web_ui.png)

#### Purpose:

The `utility.py` file contains functions for preprocessing text data and making sentiment predictions using a pre-trained model. It also includes a dictionary mapping emojis to their meanings and a list of English stopwords.

#### Functions:

1. **Preprocessing Function (`preprocess`):**
   - This function preprocesses text data by performing the following steps:
     - Converting text to lowercase.
     - Replacing URLs with 'URL'.
     - Replacing emojis with their respective meanings.
     - Replacing usernames with 'USER'.
     - Removing non-alphabetic characters.
     - Reducing consecutive characters to two.
     - Removing stopwords.
     - Lemmatizing words.

2. **Prediction Function (`predict`):**
   - This function predicts the sentiment of input text using a pre-trained model.
   - It preprocesses the input text using the `preprocess` function.
   - It then makes predictions using the pre-trained model.
   - Predictions are converted to human-readable labels ('Negative' or 'Positive').

#### Emojis and Stopwords:

- **Emojis Dictionary:**
  - The file includes a dictionary mapping emojis to their respective meanings. This mapping is used during preprocessing to replace emojis with descriptive labels.

- **Stopwords List:**
  - A list of English stopwords is defined in the file. These stopwords are removed during preprocessing to focus on important words for sentiment analysis.

#### Usage:

- The functions in `utility.py` can be imported into other Python scripts or used interactively.
- To make predictions, first, load the pre-trained pipeline from the provided pickle file (`pipeline.pickle`), and then use the `predict_pipeline` function with input text.
- If used interactively, sample text data is provided within the `__main__` block, and predictions are printed to the console.

### Main.py

#### Purpose:

The `main.py` file contains the Flask application setup and routes for handling user requests. It integrates the sentiment prediction functionality provided by the `predict_pipeline` function from the `utilities.py` module.

#### Flask Application Setup:

- The Flask application is initialized with `Flask(__name__)`.

#### Sentiment Prediction Function:

- A placeholder function `predict_sentiment` is defined to predict sentiment based on input text.
- This function utilizes the `predict_pipeline` function from the `utilities.py` module to make sentiment predictions.
- Input text is passed to the `predict_pipeline` function, and the prediction result is returned.

#### Routes:

1. **Index Route (`/`):**

   - This route handles both GET and POST requests.
   - In the case of a POST request, it retrieves the input text from the form data.
   - It then calls the `predict_sentiment` function to obtain the sentiment prediction for the input text.
   - The prediction result is passed to the `index.html` template for rendering.
   - If there's any error during prediction (e.g., empty input text), an error message is returned.

#### Running the Flask App:

- The Flask app is started with `python main.py` method. It listens on all public IPs (`0.0.0.0`) and enables debug mode for development.

you can also run Docker container after pull from the docker hub or clone github repository.

[GITHUB Repo](https://github.com/zubi9/sentiment_analysis_app.git)

Doker image can be build using the `Docker-compose.yml` file in the repo.

To run docker container you need to :`docker pull muhammad546/sentiment_analysis_app`

#### Note:

- he `predict_pipeline` function is expected to be available in the `utilities.py` file, providing sentiment prediction functionality.
- The template `index.html` is assumed to be present in the `templates` directory for rendering the web interface.
ignore app.py for this code you have manually send post request form the api service tools like **postman**