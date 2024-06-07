from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="bert-base-uncased")

classification = classifier("This movie was awesome!")
print(classification) 