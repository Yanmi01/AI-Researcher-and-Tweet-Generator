# AI Researcher and Tweet Generator

## Overview

This repository provides a command-line tool that:

1. Searches the web for a given research query.

2. Synthesizes an in-depth report based on the retrieved snippet.

3. Generates a set of concise tweets summarizing the findings.

4. Offers a human-in-the-loop approval step with automated sanity checks and audit logging.
  

It was built with:

- LangChain

- Ollama Gemma

- Serper API

- Python 3.10

## Installation

1. Clone the repo:
   ```bash
        git clone https://github.com/Yanmi01/ai-research-tweet-generator.git
        cd ai-research-tweet-generator/project
   ```
2. Create & activate a virtual environment:
   ```bash
        python -m venv venv
        source venv/bin/activate      # macOS/Linux
        venv\\Scripts\\activate     # Windows
   ```
3. Install dependencies:
   ```bash
       pip install -r requirements.txt
   ```
4. Add your Serper Api key to your .env file

##Usage
Run the CLI
```bash
        python main.py
```
The interactive prompts will guide you through:
1. Enter your sesarch query
2. Review the raw web snippets or re-enter query if unsatisfied
3. Approve or request revisions on the draft reports & Tweets
4. View final reports and tweets

Audit logs are saved to the review_log.csv file

## Before using the repo:
The repo utilizes Gemma2b via Ollama. Therefore, to be able to use the repo conveniently, ensure:
1. Ollama is running underground
2. You have pulled Gemma 2b.

You can use any model available via Ollama. Ensure you indicate the model in the `pipelines.py` file
