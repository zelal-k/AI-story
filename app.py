from flask import Flask, render_template, request, jsonify
from textblob import TextBlob
import openai
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Set your OpenAI API key
openai.api_key = 'openAI Key'  # Use your OpenAI API key here

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_story', methods=['POST'])
def generate_story():
    prompt = 'Generate a story with the following theme: '
    user_input = prompt + request.form.to_dict()['user_input']


    # Use OpenAI API to generate storytelling content
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=user_input,
        max_tokens=2000
    )

    # Extract the generated story from the API response
    generated_story = response['choices'][0]['text']

    # Perform sentiment analysis using TextBlob
    sentiment_analysis = TextBlob(generated_story)
    sentiment_score = sentiment_analysis.sentiment.polarity

    # Check if sentiment is negative
    if sentiment_score < 0:
        # If negative, consider regenerating the story or taking appropriate action
        generated_story = "Sorry, the generated content is not suitable for children."

    return jsonify({"generated_story": generated_story, "sentiment_score": sentiment_score})

if __name__ == '__main__':
    app.run(debug=True)
