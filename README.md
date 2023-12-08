# AI-story
AI-powered storytelling companion that generates interactive and age-appropriate stories for children based on their interests and developmental stage. 
The application uses Generative AI, specifically OpenAI's GPT model, to create personalized storytelling experiences. The stories are adapted in real-time based on the child's responses and engagement.
 through the integration of Generative AI principles and OpenAI's GPT model, aims to provide a valuable and engaging storytelling experience for children, with a focus on language development and creativity. Considerations for ethical implications and emotional connections highlight a thoughtful approach to the application's development.
 ## How to Run the AI-Powered Storytelling Companion AI
Prerequisites
Before running the application, ensure you have the following installed:

- Python (version X.X)
- Flask
- OpenAI Python library
- textblob library

# Steps
# 1- Clone the Repository:
1. Navigate to the requirements.txt file and ensure you have the required programs and library's
- Make sure you have the programs in the stated version (different versions may have differences that do not allow the successful running of the application)
2. Navigate to your command prompt (CMD)
3. Navigate to your desired folder and clone the repository on your local system
- Type "cd\" press enter
- Type "cd file_path" press enter (Insert your desired filepath where it says file_path)
- Go to the Github Repository, Click on Code in the repository on the Github Website and copy the given Github URL
- Type git clone https://github.com/zelal-k/AI-story.git
4. Navigate to this new folder in your filepath
- Type "cd\" press enter
- Type "cd file_path" press enter.

# 2- Install Dependencies:

- Use the pip command on the requirements file.
- "pip install -r requirements.txt"


# 3- Set Up OpenAI API Key:

* Sign up on the OpenAI platform.
* Obtain your API key.
* Replace 'openAI Key' in app.py with your actual API key.

# 4- Run the Application:

- Type python app.py
This will start the Flask development server.

# 5- Access the Application:
- Open your web browser and go to http://localhost:5000/.
- Enjoy the Storytelling App!
# 6- Generate Stories:

Enter a prompt in the provided form.
Click the "Generate Story" button.
View the generated story and sentiment score.

# Explanation of Technology
Generative AI Principles
Generative AI involves training models to generate new content based on patterns and information present in the training data. In this project, OpenAI's GPT (Generative Pre-trained Transformer) model is utilized. GPT, a type of transformer model, learns the structure and context of the input data, allowing it to generate coherent and contextually relevant text.

# Role of OpenAI's GPT Model
OpenAI's GPT model is the core of the storytelling application. It takes a user prompt as input and generates a story based on its training data. The model's ability to understand and generate human-like text is crucial for creating engaging and personalized storytelling experiences for children. The integration with Flask and Python allows for real-time adaptation of the narrative based on user input.
