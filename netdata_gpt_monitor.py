import os
import requests
import json
import openai

# Set up OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Function to get data from Netdata
def get_netdata_data(metric):
    response = requests.get(f'http://localhost:19999/api/v1/data?chart={metric}')
    return response.json()

# Function to analyze data using GPT
def analyze_data_with_gpt(data):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Analyze the following network metrics and provide feedback: {json.dumps(data)}",
        max_tokens=150
    )
    return response.choices[0].text

# Function to log feedback to a file
def log_feedback(message):
    with open("/tmp/netdatagpt.log", "a") as log_file:
        log_file.write(message + "\n")

# Example usage
metrics = ['system.cpu', 'system.ram', 'net.packets']

for metric in metrics:
    netdata_data = get_netdata_data(metric)
    feedback = analyze_data_with_gpt(netdata_data)
    log_feedback(f"Feedback for {metric}: {feedback}")

