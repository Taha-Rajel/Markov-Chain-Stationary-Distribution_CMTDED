
# Markov Chain – Stationary Distribution

A Python program that calculates the stationary distribution of a Discrete-Time Markov Chain (DTMC).

### Features
- Input the number of states.
- Enter the transition matrix.
- Validate the transition matrix.
- Calculate the stationary distribution using NumPy.
- Verify that probabilities sum to 1.

### Technologies
- Python
- NumPy

### Installation

```bash
pip install -r requirements.txt
```

### Run

```bash
python main.py
```

### Mathematical Model

The program solves:

\[
\pi P = \pi
\]

Subject to:

\[
\sum_{i=1}^{n}\pi_i = 1
\]

### Author
Taha Rajel
