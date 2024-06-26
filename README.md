# Vulnerable Flask LLM App

This is a Flask application that is purposefully vulnerable to LLM1 and LLM2 - prompt injection and insecure output handling from [OWASP Top 10 for LLM](https://genai.owasp.org/llm-top-10).

The application is intended for demonstration purposes only, and should not be used in a production environment.

## Purpose

The application is a Curriculum Vitae (CV) evaluator that allows users to upload their CV in PDF format, and then generates a summary and evaluation of the CV using OpenAI's GPT API. The summaries are stored in a MySQL database, and users can view the summary again on the `/summaries` endpoint.

## Vulnerabilities

The application is intentionally vulnerable to the following vulnerabilities from OWASP:

* LLM01 - Prompt Injection: The application generates a summary and evaluation of the CV using OpenAI's GPT-4 API, but does not properly sanitize the input. This allows an attacker to inject malicious commands into the prompt, which could then be executed by the API and provide incorrect scoring.
* LLM02 - Insecure Hutput handling: The application displays the summaries on the `/summaries` endpoint without properly sanitizing the output. This allows an attacker to inject malicious JavaScript code into the summaries, which could then be executed by a user's browser.

## Usage

To run the application, you will need to install the dependencies using Poetry:
```
poetry install
```

Now, set up the Database by executing the `install.sql` script.

You will also need to create a `.env` file in the root directory of the project with the following content:
```
DATABASE_URI=mysql+pymysql://root:password@localhost/cv_evaluator
OPENAI_API_KEY=enter-key-here
```

You can then start the application using the following command:
```
poetry run python run app.py
```
The application will be available at `http://localhost:5000`.

## Disclaimer

This application is for demonstration purposes only, and should not be used in a production environment.
The vulnerabilities in the application are intentionally left unpatched, and should not be used as a basis for securing a real-world application.
