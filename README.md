# AI Study Assistant

A simple Python-based AI Study Assistant built using the OpenAI API.

This project allows the user to enter any study topic and generates a beginner-friendly explanation, a real-world example, three important points, and a quiz question.

## Features

- Takes a study topic as user input
- Uses the OpenAI API to generate a response
- Provides a simple explanation of the topic
- Gives a real-world example
- Lists three important points
- Generates one quiz question
- Uses a `.env` file to keep the API key private

## Technologies Used

- Python
- OpenAI API
- OpenAI Python SDK
- python-dotenv
- Visual Studio Code

## Project Structure

```text
openai-api-lab/
│
├── app.py
├── README.md
├── .env
├── .gitignore
└── venv/
```

## How It Works

1. The user enters a study topic.
2. The program sends the topic to the OpenAI API.
3. The AI generates a simple explanation.
4. The response also includes a real-world example, important points, and a quiz question.
5. The generated response is displayed in the terminal.

## Installation

Clone the repository and open the project folder:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd openai-api-lab
```

## API Key Setup

Create a `.env` file in the project folder and add:

```text
OPENAI_API_KEY=your_api_key_here
```

Never upload your API key to GitHub.

The `.env` file is excluded using `.gitignore`.

## How to Run

Activate the virtual environment:

```bash
source venv/bin/activate
```

Install the required packages:

```bash
pip install openai python-dotenv
```

Run the application:

```bash
python app.py
```

## Note

This project requires a valid OpenAI API key with available API credits to generate responses.

## Author

Created as a Python and OpenAI API learning project.
