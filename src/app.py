import os
import openai
import gradio as gr
from voice_chat import WhisperChatbot
from utils.models_and_path import KNOWLEDGE_BASE_PATH, MODEL_NAME
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
openai.api_key = os.environ["OPENAI_API_KEY"]

whisper_chatbot = WhisperChatbot(
    model_name=MODEL_NAME, knowledge_base_path=KNOWLEDGE_BASE_PATH
)

interface = gr.Interface(
    title="Multi-lingual Voice based RAG chatbot",
    fn=whisper_chatbot.response,
    inputs=[gr.components.Audio(source="microphone", type="filepath")],
    outputs=[
        gr.components.Textbox(label="Transcribed Text"),
        gr.components.Textbox(label="Translated Text"),
        gr.components.Textbox(label="Language"),
        gr.components.Textbox(label="English Result"),
        gr.components.Textbox(label="Translated Result"),
    ],
    live=False,
).launch()

# if __name__ == "__main__":
#     interface.launch(
#         debug=True,
#         share=True,
#         enable_queue=True,
#     )
