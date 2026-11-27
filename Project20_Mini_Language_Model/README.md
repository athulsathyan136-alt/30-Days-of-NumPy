# Project 20 – Mini Character-Level Language Model Using NumPy

## Overview
A small trainable character-level bigram language model implemented from scratch using NumPy.

## Features
- Character-level tokenization
- Vocabulary creation
- Next-character prediction
- Softmax probability calculation
- Cross-entropy loss
- Gradient descent training
- Text generation
- Model and output saving

## Technologies
- Python
- NumPy

## Model Architecture
The model uses a vocabulary-sized weight matrix to learn the probability of the next character given the previous character.

## Limitation
This is a bigram language model, not a GPT or Transformer. It uses only one previous character as context and is trained on a small educational dataset.

## Run
```bash
python -m pip install -r requirements.txt
python main.py
```

## Learning Outcomes
Understanding tokenization, probability distributions, loss functions, gradient descent, and next-character prediction.