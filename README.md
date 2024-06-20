# Zero-Shot Sentiment and Intention Prediction

## Description
This project aims to predict sentiment and intention from a given text using a zero-shot classification model. The model used is `facebook/bart-large-mnli` from Hugging Face.

## Project Structure
- `src/`: Contains the main system code.
- `config/`: Contains model configurations.
- `data/`: Contains the simulated data created with ChatGPT.
- `resources/`: Contains the zero-shot model loader.

## Installation
1. Clone the repository.
2. Navigate to the project directory.
3. Install the package via

```shellscript
pip install {name of archive}
```

## Usage
To run the sentiment and intention prediction:
```shellscript
predict
```

## Configuration
Model configurations can be found in `config/config.ini`.