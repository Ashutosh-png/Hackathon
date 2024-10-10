import streamlit as st
from transformers import MT5ForConditionalGeneration, MT5Tokenizer
import torch

# Load the MT5 model and tokenizer
model_name = "google/mt5-base"
tokenizer = MT5Tokenizer.from_pretrained(model_name)
model = MT5ForConditionalGeneration.from_pretrained(model_name)

# Function to summarize text
def summarize_text(text):
    inputs = tokenizer(text, return_tensors='pt', max_length=1024, truncation=True, padding="max_length")
    summary_ids = model.generate(inputs['input_ids'], max_length=15000, min_length=100, length_penalty=2.0, num_beams=4, early_stopping=True)
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# Streamlit UI
st.title("Text Summarizer")
st.write("Enter your text or upload a file to summarize.")

# Text input
text_input = st.text_area("Enter your text:", height=200)

# File upload
uploaded_file = st.file_uploader("Or upload a text file:", type=["txt"])

# Button to generate summary
if st.button("Generate Summary"):
    if text_input:
        summary = summarize_text(text_input)
        st.subheader("Summary:")
        st.write(summary)
    elif uploaded_file is not None:
        file_content = uploaded_file.read().decode("utf-8")
        summary = summarize_text(file_content)
        st.subheader("Summary:")
        st.write(summary)
    else:
        st.error("Please provide text input or upload a file.")
