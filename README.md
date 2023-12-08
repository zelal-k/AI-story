# AI-Story: AI-Powered Storytelling Companion
AI-Story is an AI-powered storytelling companion that generates interactive and age-appropriate stories for children based on their interests and developmental stage. The application utilizes Generative AI principles, specifically OpenAI's GPT model, to create personalized storytelling experiences. The stories are adapted in real-time based on the child's responses and engagement.

# How to Run the AI-Powered Storytelling Companion
## Prerequisites

Before running the application, ensure you have the following installed:

- Python (version X.X)
- Flask
- OpenAI Python library
- Textblob library
## Steps

# 1- Clone the Repository:
- Navigate to the 'requirements.txt' file and ensure you have the required programs and libraries.
- Verify the versions of the programs (different versions may have differences that do not allow the successful running of the application).
- Open your command prompt (CMD).
- Navigate to your desired folder and clone the repository on your local system.
  code: 
cd file_path  # Insert your desired filepath where it says file_path
git clone https://github.com/zelal-k/AI-story.git
cd AI-story

# 2- Set Up Virtual Environment (if not already set up):
- Navigate to your desired folder path.
   code: 
cd \  # Press enter
cd file_path  # Insert your desired filepath where it says file_path
- Create a virtual environment using the venv module.
   code: 
python -m venv .env
- Activate the virtual environment.
  - For Windows:
     code:
.env\Scripts\activate
For Mac/Linux:
     code: 
source .env/bin/activate
# 3- Install Dependencies:
- Use the pip command on the requirements file.
  code: 
pip install -r requirements.txt

# 4- Set Up OpenAI API Key:
- Sign up on the OpenAI platform.
- Obtain your API key.
- Replace 'openAI Key' in 'app.py' with your actual API key.
- 
# 5- Run the Application:
- Type 'python app.py'. This will start the Flask development server.
  
# 6- Access the Application:
- Open your web browser and go to http://127.0.0.1:5000.
- Enjoy the Storytelling App!
  
# 6- Generate Stories:
- Enter a prompt in the provided form.
- Click the "Generate Story" button.
- View the generated story and sentiment score.
#### NOTE:Set Up Flask Environment
1. Set Flask Environment:
  - Type set 'FLASK_APP=app.py' (for Windows) or 'export FLASK_APP=app.py' (for Mac/Linux) and press enter.
2. Run Flask:
  - Type 'flask run' and press enter.
3. Access the Application:
 - Open your web browser and go to http://127.0.0.1:5000.
 - Enjoy the Storytelling App!
   
## Explanation of Technology
# Generative AI Principles:
Generative AI involves training models to generate new content based on patterns and information present in the training data. In this project, OpenAI's GPT (Generative Pre-trained Transformer) model is utilized. GPT, a type of transformer model, learns the structure and context of the input data, allowing it to generate coherent and contextually relevant text.

# Role of OpenAI's GPT Model:
OpenAI's GPT model is the core of the storytelling application. It takes a user prompt as input and generates a story based on its training data. The model's ability to understand and generate human-like text is crucial for creating engaging and personalized storytelling experiences for children. The integration with Flask and Python allows for real-time adaptation of the narrative based on user input.
