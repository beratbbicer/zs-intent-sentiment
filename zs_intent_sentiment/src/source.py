# Reference: https://huggingface.co/docs/transformers/v4.41.3/en/quicktour#pipeline

# Reroute download from cache to resources folder
import os
os.environ['HF_HOME'] = 'resources'

from transformers import pipeline
import configparser
import json
from pathlib import Path

def predict_sentiment_intention(classifier, text, labels):
    # Predict sentiment
    sentiment_result = classifier(text, labels['sentiment_labels'])
    sentiment = sentiment_result['labels'][0]

    # Predict emotion
    emotion_result = classifier(text, labels['emotion_labels'])
    emotion = emotion_result['labels'][0]

    # Predict intention
    intention_result = classifier(text, labels['intention_labels'])
    intention = intention_result['labels'][0]

    return {
        "text": text,
        "sentiment": sentiment,
        "emotion": emotion,
        "intention": intention
    }

def main():
    localdir = Path(__file__).parent.resolve()
    # Path.cwd()

    # Setup
    config = configparser.ConfigParser()
    configpath = Path(localdir).joinpath('config').joinpath('config.ini')
    print(str(configpath.resolve()))
    config.read(str(configpath.resolve()))
    classifier = pipeline("zero-shot-classification", model=config.get('model', 'model_name'))

    conversation_file = Path(localdir).joinpath('data').joinpath('conversation_file')
    print(str(conversation_file.resolve()))
    conversation = json.loads(str(conversation_file.resolve()))
    
    labels_file = Path(localdir).joinpath('data').joinpath('labels')
    print(str(labels_file.resolve()))
    labels = json.loads(str(labels_file.resolve()))
    
    print(conversation)
    print(labels)
    return

    # Run the classifier
    results = []
    for message in conversation:
        if message.get("role") == "customer":
            result = predict_sentiment_intention(classifier, message["text"], labels)
            results.append(result)
        else:
            pass

    for res in results:
        print(f"Text: {res['text']}\n\tSentiment: {res['sentiment']}\n\tEmotion: {res['emotion']}\n\tIntention: {res['intention']}")