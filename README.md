FitBuddy – AI Fitness Plan Generator

 1.1: Research and Select the Appropriate Generative AI Model

For the FitBuddy project, we researched different generative AI models capable of generating structured text responses for workout plans.

# Models Considered
1. OpenAI GPT
2. Google Gemini
3. Meta LLaMA

# Selected Model: Google Gemini

Google Gemini was selected for this project because:

- Strong natural language generation
- Easy API integration with Python
- Free tier available for development
- Suitable for generating structured fitness plans

# Role of Gemini in FitBuddy

Gemini is used to:
- Generate personalized -> 7-day workout plans
- Modify workout plans based on -> user feedback
- Provide -> nutrition and recovery tips

This allows the application to create dynamic and personalized fitness guidance.


# 🏋️ Fit-Buddy-AI Project Workflow

## 1. Initiation
- Define vision and goals
- Identify stakeholders
- Establish success metrics

## 2. Planning
- Break down features
- Create roadmap
- Assign roles
- Set milestones

## 3. Development
- AI model training
- App development
- UI/UX design
- Integration with wearables

## 4. Testing
- Unit testing
- Beta testing
- Collect feedback
- Bug fixes

## 5. Launch
- Release MVP
- Marketing & onboarding

## 6. Monitoring & Improvement
- Track engagement
- Collect feedback
- Release updates
- Scale infrastructure

## 7. Closure & Reflection
- Document lessons learned
- Celebrate milestones
- Plan next-gen features

#Activity 5.1 – Preparing the Application for Local Deployment objective
Prepare the FitBuddy application so that it can be run and tested on a local machine for development and debugging.

Step 1: Clone the Repository
First download the project from GitHub.
-git clone https://github.com/<repository-link>
Then move into the project folder.
-cd fit-buddy-ai

Step 2: Create a Virtual Environment
Create a virtual environment to manage dependencies.
-python -m venv venv
Activate the virtual environment.
-Windows
venv\Scripts\activate
-Mac/Linux
source venv/bin/activate

Step 3: Install Required Dependencies
Install the libraries listed in requirements.txt.
-pip install -r requirements.txt
These dependencies include:
-FastAPI
-Uvicorn
-Google Generative AI SDK
-SQLAlchemy
-Jinja2

Step 4: Configure Environment Variables
Create a .env file in the project root.
Add the Gemini API key:
-> GEMINI_API_KEY=your_api_key_here
This key allows the application to connect with the Google Gemini AI model.

Step 5: Run the FastAPI Application
Start the application using Uvicorn.
uvicorn app.main:app --reload
The --reload flag enables automatic server restart during development.

Step 6: Access the Application
Open a browser and go to:
-http://127.0.0.1:8000
You can also access the API documentation at:
-http://127.0.0.1:8000/docs
This interface allows testing the API endpoints.
 
