# RAG Chatbot

The Retrieval Augmented Generation Chatbot is a project that includes two chatbots: the Baseline Chatbot and the Multi-lingual Voice Chatbot. This README provides a guide on how to set up and run both chatbots.

## Baseline Chatbot

The Baseline Chatbot is a text-based chatbot that uses Retrieval Augmented Generation using GPT 3.5 to respond to user queries. 
### Features
1. Custom separators for splitting the knowledge base into chunks (Since the knowledge base is formatted like a markdow, using MarkdownHeaderSplitter to get complete question and description in each embedding chunk)
2. Prevent hallucination by using RAG and a custom prompt template.

To run the Baseline Chatbot, follow these steps:

### Prerequisites

Before running the Baseline Chatbot, ensure you have the following installed:

1. Python (version 3.10.5)
2. Other dependencies specified in the requirements.txt file

### Installation

1. Clone this repository to your local machine.
2. Install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

### Usage

To run the Baseline Chatbot, navigate to the "src" directory and execute the following command:

```bash
python gradio_app.py
```

This command will launch a Gradio web application, allowing you to interact with the Baseline Chatbot in your browser.

## Multi-lingual Voice Chatbot

The Multi-lingual Voice Chatbot is designed to respond to user queries in multiple languages using voice input. The Multi-lingual Voice Chatbot is located in the "voice-feature" branch. To run the Multi-lingual Voice Chatbot, follow these steps:

### Prerequisites

Before running the Multi-lingual Voice Chatbot, ensure you have the following installed:

1. Python (version 3.10.5)
2. Jupyter Notebook
3. Other dependencies specified in the requirements.txt file

### Installation

1. Clone this repository to your local machine.
2. Navigate to the "multi_lingual_voice_chatbot" directory.
3. Install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

### Usage

To run the Multi-lingual Voice Chatbot, follow these steps:

1. Launch Jupyter Notebook.
2. Open the "multi_lingual_voice_chatbot.ipynb" notebook.
3. Follow the instructions in the notebook to interact with the Multi-lingual Voice Chatbot using voice input.

Please note that the Multi-lingual Voice Chatbot requires additional models like the whisper model, which can be downloaded as instructed in the notebook.

