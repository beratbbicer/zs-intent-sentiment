# Zero-Shot Sentiment and Intention Prediction

## Description
This project aims to predict sentiment and intention from a given text using a zero-shot classification model. The default model used is `facebook/bart-large-mnli` from Hugging Face.

## Project Structure
- `src/`: Contains the main system code.
- `config/`: Contains model configurations.
- `data/`: Contains the simulated data created with ChatGPT.
- `resources/`: Contains HuggingFace data after install.

## Installation
1. Clone the repository.
2. Navigate to the project directory.
3. Install the package via

```shellscript
pip install zsins-1.0.tar.gz
```

## Usage
To run the sentiment and intention prediction:
```shellscript
zsins-infer
```

## Configuration
Model configurations can be found in `config/config.ini`.