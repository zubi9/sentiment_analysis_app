# Twitter Sentiment Analysis Web Application

A machine learning web application that classifies Twitter data into **Positive** or **Negative** sentiment using Natural Language Processing (NLP) techniques and a pre-trained model. Built with Python and Flask, and fully containerized with Docker.

---

## Features

* **Text Preprocessing Pipeline:** Handles raw text cleaning, URL and user tag normalization, emoji-to-text translation, lemmatization, and stopword removal.
* **Sentiment Prediction Engine:** Utilizes a pre-trained ML model to classify incoming text rapidly.
* **Interactive Web Interface:** Simple Flask-based UI for real-time text analysis.
* **RESTful API Endpoint:** Supports POST requests via tools like Postman for direct model interactions.
* **Dockerized Deployment:** Pre-configured Docker Compose file and Docker Hub image for hassle-free containerization.

---

## Project Architecture

### `utility.py`

Contains preprocessing utilities, NLP resources, and inference functions.

* **Text Preprocessing (`preprocess`):**
* Converts text to lowercase.
* Replaces URLs with `'URL'` and usernames with `'USER'`.
* Translates emojis into descriptive labels using an internal emoji mapping dictionary.
* Reduces consecutive repeated characters (e.g., "loooove" $\rightarrow$ "love").
* Strips non-alphabetic characters, English stopwords, and applies word lemmatization.


* **Inference Pipeline (`predict`):**
* Loads the pre-trained model pipeline (`pipeline.pickle`).
* Passes preprocessed text through the model to output human-readable labels (`Positive` / `Negative`).



### `main.py`

Drives the Flask web server and routes request traffic.

* **`/` (GET / POST):** Renders the user web interface and displays real-time sentiment predictions for form inputs.
* **API Ingestion:** Accepts input payloads via web interface or API testing clients (e.g., Postman).

---

## Quick Start

### Option 1: Local Setup

1. **Clone the Repository:**
```bash
git clone https://github.com/zubi9/sentiment_analysis_app.git
cd sentiment_analysis_app

```


2. **Install Dependencies:**
```bash
pip install -r requirements.txt

```


3. **Run the Application:**
```bash
python main.py

```


Access the web app in your browser at `http://localhost:5000`.

---

### Option 2: Docker Setup

#### Pull Pre-built Image from Docker Hub

```bash
docker pull muhammad546/sentiment_analysis_app:latest
docker run -p 5000:5000 muhammad546/sentiment_analysis_app

```

#### Build with Docker Compose

```bash
docker-compose up --build

```

---

## API Usage (Postman / cURL)

You can send raw POST requests directly to the prediction endpoint:

* **URL:** `http://localhost:5000/`
* **Method:** `POST`
* **Body:** Form Data (`text="Your tweet or sentence here"`)

---

Would you like me to add a sample `requirements.txt` template or add a step-by-step example for testing the endpoint with cURL?
