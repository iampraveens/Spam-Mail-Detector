# Spam Mail Detector <img src="https://cdn-icons-png.flaticon.com/512/9275/9275788.png" alt="Car Price Prediction" width="50" height="50">

## Table of Contents
- [About](#about)
- [Getting Started](#getting-started)
- [Prediction](#prediction)
- [Usage](#usage)
- [Dockerized Web App](#dockerized-web-app)
- [Contributing](#contributing)
- [License](#license)

## About
This is a Spam Mail Detector project that uses machine learning to classify emails as either "Ham" (non-spam) or "Spam" (junk or malicious). It utilizes a TF-IDF vectorizer and a trained machine learning model to make predictions.

## Getting Started
To get started with this project, you'll need Python and a few libraries installed. Follow these steps:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/iampraveens/https://github.com/iampraveens/Spam-Mail-Detector.git
```
2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Prediction

```bash
streamlit run app.py
```

## Usage
- Launch the application using the instructions in the "Getting Started" section.
- Enter the email content you want to classify in the text area.
- Press "ctrl + enter" or click the "Predict" button.
- The application will classify the email as "Ham" or "Spam" and display the result.

## Dockerized Web App
You can also deploy the Spam Mail Detector web application using Docker. Build the Docker image and run the container:
```bash
docker build -t your_docker_username/spam-mail-detector .
```
- To build a docker image.

```bash
docker run -d -p 8501:8501 your_docker_username/spam-mail-detector
```
- To run as a container.

Access the web app at `http://localhost:8501` or `your_ip_address:8501` in your web browser.
Else if you want to access my pre-built container, here is the code below to pull from docker hub(Public).
```bash
docker pull iampraveens/spam-mail-detector:latest
```

## License 
This project is licensed under the MIT License - see the [License](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt) file for details.
