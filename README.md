# Language Translation Tool

This is a language translation tool built using Flask and OpenAI's GPT-3.5-turbo model. Users can input text in one language and get the translated text in another language via a web interface.

## Getting Started

### Running Locally

1. **Clone the repository:**

   ```bash
   git clone https://github.com/tr-haider/openai-language-translation-tool.git
   cd openai-language-translation-tool

2. **Setup virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   
3. **Install required dependencies:**

   ```bash
   pip install -r requirements.txt

4. **Create environment variable file:**

   ```bash
   touch .env
   Paste the following line in .env file.Replace API_KEY with Open AI API key
   OPENAI_API_KEY="API_KEY"

5.  **Run the app:**

   ```bash
   cd web_interface
   python3 app.py
   
6. **Access the app:**
   Open your browser and navigate to http://127.0.0.1:5000/.

   
   
