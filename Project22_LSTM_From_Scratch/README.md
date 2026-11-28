# Project 22 – LSTM From Scratch Using NumPy

## Overview
An educational Long Short-Term Memory network implemented from scratch using NumPy for binary sequence classification.

## Features
- Synthetic sequential dataset
- Input gate
- Forget gate
- Output gate
- Candidate cell memory
- Cell state and hidden state
- Forward propagation
- Cross-entropy loss
- Backpropagation Through Time (BPTT)
- Gradient clipping
- Gradient descent
- Test accuracy evaluation
- Model and prediction saving

## Architecture
- Input size: 1
- Hidden size: 12
- Output size: 2
- Sequence length: 5

## Technologies
- Python
- NumPy

## Run
```bash
python -m pip install -r requirements.txt
python main.py
```

## Learning Outcomes
Understand LSTM gates, memory management, cell states, hidden states, sequence learning, and backpropagation through time.

## Limitations
This is a small educational LSTM trained on synthetic data. It is not a production forecasting or language-generation model.