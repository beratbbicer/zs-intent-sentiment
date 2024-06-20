# Reference: https://huggingface.co/docs/transformers/v4.41.3/en/quicktour#pipeline

# Reroute download from cache to resources folder
import os
os.environ['HF_HOME'] = 'resources'

from transformers import pipeline
import configparser
import json

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
    # Setup
    config = configparser.ConfigParser()
    config.read(f'config{os.sep}config.ini')

    conversation = json.loads(config.get('data', 'conversation_file'))
    labels = json.loads(config.get('data', 'labels'))
    classifier = pipeline("zero-shot-classification", model=config.get('model', 'model_name'))
    
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

if __name__ == "__main__":
    main()