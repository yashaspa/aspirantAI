# Aspirant AI

## Overview
Aspirant AI is dedicated to building an application that fine-tunes a Large Language Model (LLM) using course content tailored for Teaching Assistants. The primary course content utilized for training is sourced from "CSCI 1133" offered at the University of Minnesota.

## Project Goal
Our mission is to adapt a general-purpose LLM to resonate with the curriculum and nuances of CSCI 1133, thereby enhancing the capabilities of Teaching Assistants in their roles.

## Data Collection

### Internal Data Sources:
- **Yashas**: Uploading all CSCI 1133 materials from three distinct classes to the `data` folder on our GitHub repository.
- **Tim**: Converting the existing data in the `data` folder into a CSV format for easier processing.

### External Data Sources:
To enrich the model's understanding, we're incorporating external datasets:
- Parsing educational platforms like [W3Schools](https://www.w3schools.com/) and the [official Python 3 documentation](https://docs.python.org/3/).
- Exploring datasets available on platforms like GitHub.
- Specific datasets under consideration:
  - [Variables and Types from LearnPython](https://www.learnpython.org/en/Variables_and_Types)
  - [SQL Knowledge Dataset from Hugging Face](https://huggingface.co/datasets/knowrohit07/know_sql)

## Model Architecture
We've selected **Code LLama**. Tailored for code-related tasks, Code Llama provides a deep understanding of programming languages and code syntax.

## Evaluation

### Metrics:
- **Precision**: Accuracy of positive predictions.
- **Recall**: Fraction of correctly identified positive instances.
- **F1 Score**: Harmonic mean of Precision and Recall.

### Bias and Variance:
- **Bias**: Refers to the error introduced by approximating real-world complexities with a simplified model. A high bias can cause the model to miss relevant relations between features and target outputs (underfitting).
  - **Recommendation**: Regularly review the model's performance on the training set. If it's performing poorly, consider making the model more complex or incorporating more features.
  
- **Variance**: Refers to the model's sensitivity to small fluctuations in the training set. A model with high variance might perform exceptionally well on the training set but poorly on unseen data (overfitting).
  - **Recommendation**: Use techniques like regularization, dropout, or even ensemble methods to reduce variance. Also, consider increasing the training data.

## Methods

### Data Preprocessing:
- **Tokenization**: Breaking down text into smaller chunks or tokens.
- **Normalization**: Converting all text to lowercase to maintain consistency.
- **Removing Stop Words**: Eliminating commonly used words that don't add significant meaning.

### Model Training:
- **Transfer Learning**: Utilizing the pre-trained CodeBERT model and fine-tuning it on our dataset.
- **Batch Training**: Training the model in batches for better convergence and efficiency.
- **Learning Rate Scheduling**: Gradually decreasing the learning rate as training progresses to optimize convergence.

### Post-Training:
- **Model Evaluation**: Using a separate validation set to evaluate the model's performance regularly.
- **Model Saving**: Saving checkpoints of the model at regular intervals and when achieving the best performance on the validation set.

### Deployment:
- **API Creation**: Wrapping the model inside an API for easy integration into applications or platforms.
- **Continuous Monitoring**: Regularly monitoring the model's performance in real-world scenarios and collecting feedback for iterative improvement.

## Hugging Face AutoTrain Experimentation

Alongside our primary training methods, we experimented with Hugging Face's AutoTrain to evaluate its efficacy for our project. AutoTrain provided an automated approach to model training, and we wanted to assess its ease of use and performance outcomes for our specific use case.
