
# Emotion Detection Web App

This is a simple Flask-based web application that uses a machine learning model to detect emotions from text input.

![App Screenshot](https://i.imgur.com/25zRN0u.png)

## 🔍 Overview

The app sends user-provided text to a remote NLP model and returns the scores of five key emotions:

-   **Anger**
    
-   **Disgust**
    
-   **Fear**
    
-   **Joy**
    
-   **Sadness**
    

It also determines the **dominant emotion** based on the highest score.

## 🚀 How to Run

1.  Make sure you have Python 3.11 installed.
    
2.  Install the required dependencies:
    
    `pip install -r requirements.txt` 
    
3.  Start the Flask server:
    
    `python3 server.py` 
    
4.  Open your browser and visit:  
    [http://localhost:5000](http://localhost:5001)

## 📁 Project Structure

```
emotion-detection/
├── .gitignore
├── LICENSE
├── README.md
├── server.py
├── EmotionDetection/
│   ├── __init__.py
│   ├── emotion_detection.py
│   └── __pycache__/
├── static/
│   └── mywebscript.js
├── templates/
│   └── index.html
├── test_emotion_detection.py
└── __pycache__/
```

    

## 🧪 Running Tests


`python3 -m unittest discover EmotionDetection` 

## ✅ Example Output

> For the given statement, the system response is  
> `'anger': 0.02`, `'disgust': 0.01`, `'fear': 0.03`, `'joy': 0.91`, `'sadness': 0.03`.  
> The dominant emotion is **joy**.

## 📬 Feedback

Feel free to fork the repo or submit issues and improvements.  
Happy coding! 😊
