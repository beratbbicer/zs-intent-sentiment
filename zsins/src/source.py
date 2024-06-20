import os
import json
from pathlib import Path
import configparser
from tqdm import tqdm

# package_directory = os.path.dirname(os.path.abspath(__file__))
package_directory = Path(__file__).parent.parent.resolve()
# print(str(package_directory.resolve()))

# Reroute download from cache to resources folder & set it up
hf_cachepath = str(Path(package_directory).joinpath('resources').resolve())
Path(hf_cachepath).mkdir(parents=True, exist_ok=True)
Path(hf_cachepath).joinpath('__init__.py').touch(exist_ok=True)
os.environ['HF_HOME'] = hf_cachepath
# print(os.environ['HF_HOME'])

# Import after env-var is set
from transformers import pipeline

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
    configpath = Path(package_directory).joinpath('config').joinpath('config.ini')
    # print(str(configpath.resolve()))
    config.read(str(configpath.resolve()))
    classifier = pipeline("zero-shot-classification", model=config.get('model', 'model_name'))

    conversation_file = Path(package_directory).joinpath('data').joinpath('conversation.json')
    # print(str(conversation_file.resolve()))
    with open(conversation_file) as json_file:
        conversation = json.load(json_file)['conversation']

    labels_file = Path(package_directory).joinpath('data').joinpath('labels.json')
    # print(str(labels_file.resolve()))
    with open(labels_file) as json_file:
        labels = json.load(json_file)

    # Run the classifier
    results = []
    for message in tqdm(conversation):
        result = predict_sentiment_intention(classifier, message["text"], labels)
        results.append(result)
    
    # Dump
    writepath = package_directory.joinpath('data').joinpath('results.txt')
    with open(writepath, 'w') as file:
        for res in results:
            text = f"Text: {res['text']}\n\tSentiment: {res['sentiment']}\n\tEmotion: {res['emotion']}\n\tIntention: {res['intention']}"
            print(text)
            file.write(f'{text}\n')
    print(f"\nOutput path:\n{writepath}")