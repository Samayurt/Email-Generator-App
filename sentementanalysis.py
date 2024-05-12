from transformers import pipeline

# Load the sentiment analysis pipeline using GPT-2
sentiment_analysis = pipeline("sentiment-analysis", model="model/llama-2-7b-chat.ggmlv3.q8_0.bin")

# Example text for sentiment analysis
text = "I love using large language models for natural language processing tasks."

# Perform sentiment analysis
result = sentiment_analysis(text)

# Print the result
print(result)
