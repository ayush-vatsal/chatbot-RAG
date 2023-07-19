# RAG Chatbot

The Retrieval Augmented Generation Chatbot is a project that includes two chatbots: the Baseline Chatbot and the Multi-lingual Voice Chatbot.
Try them out here: 
1. [Baseline Chatbot](https://ayush-vatsal-rag-chatbot.hf.space/)
2. [Multi-Lingual Voice based RAG Chatbot](https://ayush-vatsal-multi-lingual-voice-based-rag-chatbot.hf.space/)
##### This README provides a guide on how to set up and run both chatbots.
### Examples:
![baseline_chatbot](https://github.com/ayush-vatsal/chatbot-RAG/assets/57457066/cb394f53-1bf0-4cb6-a252-368be3531be1)
Baseline Chatbot

![multi-lingual-english](https://github.com/ayush-vatsal/chatbot-RAG/assets/57457066/7f881d9b-5f3f-4a11-8782-fe45a81c0351)
Multi-Lingual Voice based RAG Chatbot (English)

![multi-lingual-hindi](https://github.com/ayush-vatsal/chatbot-RAG/assets/57457066/a2df6852-b943-4f36-8026-22e3b44af664)
Multi-Lingual Voice based RAG Chatbot (Using translations, Hindi)


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
python gradio app.py
```

This command will launch a Gradio web application, allowing you to interact with the Baseline Chatbot in your browser.

## Multi-lingual Voice Chatbot

The Multi-lingual Voice Chatbot is designed to respond to user queries in multiple languages using voice input. The Multi-lingual Voice Chatbot is located in the "voice-feature" branch.
It understands more than 30 different languages however its performance is dependent on Whisper's performance.
### Performance of Whisper model on different languages
![language-breakdown](https://github.com/ayush-vatsal/chatbot-RAG/assets/57457066/f62da70a-e7f0-411b-9deb-dc5bbef14608)
###### (Taken from Whisper Github Readme)
 To run the Multi-lingual Voice Chatbot, follow these steps:
### Prerequisites

Before running the Multi-lingual Voice Chatbot, ensure you have the following installed:

1. Python (version 3.10.5)
2. Jupyter Notebook
3. Other dependencies specified in the requirements.txt file

### Installation

1. Clone this repository to your local machine.
2. Navigate to the voice_feature branch
3. Install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

### Usage

To run the Baseline Chatbot, navigate to the "src" directory and execute the following command:

```bash
python gradio app.py
```

This command will launch a Gradio web application, allowing you to interact with the Multi Lingual Voice Chatbot in your browser.

### Usage

To run the Multi-lingual Voice Chatbot, follow these steps:

1. Launch Jupyter Notebook.
2. change directories to Notebooks
3. Open the "multi_lingual_voice_chatbot.ipynb" notebook.
4. Follow the instructions in the notebook to interact with the Multi-lingual Voice Chatbot using voice input.

Please note that the Multi-lingual Voice Chatbot requires additional models like the whisper model, which can be downloaded as instructed in the notebook. ALso, the chatbots use OpenAI's GPT 3.5 model, so you will need a paid API key.

