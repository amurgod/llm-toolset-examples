#!/bin/env python3
import os
import time
import tempfile
import streamlit as st
from streamlit_chat import message
from rag import ChatPDF

st.set_page_config(page_title="ChatPDF with Model Selection")


def display_messages():
    st.subheader("Chat")
    for i, (msg, is_user) in enumerate(st.session_state["messages"]):
        message(msg, is_user=is_user, key=str(i))
    st.session_state["thinking_spinner"] = st.empty()


def process_input():
    if (
        st.session_state["user_input"]
        and len(st.session_state["user_input"].strip()) > 0
    ):
        user_text = st.session_state["user_input"].strip()
        with st.session_state["thinking_spinner"], st.spinner("Thinking"):
            agent_text = st.session_state["assistant"].ask(user_text)

        st.session_state["messages"].append((user_text, True))
        st.session_state["messages"].append((agent_text, False))


def read_and_save_file():
    st.session_state["assistant"].clear()
    st.session_state["messages"] = []
    st.session_state["user_input"] = ""

    for file in st.session_state["file_uploader"]:
        with tempfile.NamedTemporaryFile(delete=False) as tf:
            tf.write(file.getbuffer())
            file_path = tf.name

        with st.session_state["ingestion_spinner"], st.spinner(
            f"Ingesting {file.name}"
        ):
            t0 = time.time()
            st.session_state["assistant"].ingest(file_path)
            t1 = time.time()

        st.session_state["messages"].append(
            (
                f"Ingested {file.name} in {t1 - t0:.2f} seconds",
                False,
            )
        )
        os.remove(file_path)


def change_model():
    """Change the model when user selects a different one"""
    if "assistant" in st.session_state:
        new_model = st.session_state["model_selector"]
        success = st.session_state["assistant"].change_model(new_model)
        if success:
            st.success(f"✅ Switched to model: {new_model}")
            # Clear messages when changing models
            st.session_state["messages"] = []
        else:
            st.error(f"❌ Failed to switch to model: {new_model}")


def page():
    if len(st.session_state) == 0:
        st.session_state["messages"] = []
        # Initialize with a default model (will be overridden by selector)
        st.session_state["assistant"] = ChatPDF(llm_model="mistral:latest")

    st.header("ChatPDF with Model Selection 🤖")

    # Model Selection Section
    st.subheader("Select Your Model")
    
    # Get available models
    available_models = ChatPDF.get_available_models()
    
    if not available_models:
        st.error("❌ No Ollama models found. Please install models with 'ollama pull <model_name>'")
        st.stop()
    
    # Create model selector
    default_model = "mistral:latest" if "mistral:latest" in available_models else available_models[0]
    
    selected_model = st.selectbox(
        "Choose your Ollama model:",
        options=available_models,
        index=available_models.index(default_model) if default_model in available_models else 0,
        key="model_selector",
        on_change=change_model
    )
    
    # Show model info
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**Current Model:** {selected_model}")
    with col2:
        if "assistant" in st.session_state:
            model_info = st.session_state["assistant"].get_model_info()
            if model_info["model_available"]:
                st.success("✅ Model Available")
            else:
                st.error("❌ Model Not Available")

    # Document Upload Section
    st.subheader("Upload a document")
    st.file_uploader(
        "Upload document",
        type=["pdf"],
        key="file_uploader",
        on_change=read_and_save_file,
        label_visibility="collapsed",
        accept_multiple_files=True,
    )

    st.session_state["ingestion_spinner"] = st.empty()

    # Chat Section
    display_messages()
    st.text_input("Message", key="user_input", on_change=process_input)

    # Sidebar with additional info
    with st.sidebar:
        st.header("ℹ️ Information")
        st.write("**Available Models:**")
        for model in available_models:
            st.write(f"- {model}")
        
        st.write("**Model Recommendations:**")
        st.write("- **mistral:latest**: Good general purpose")
        st.write("- **llama3.2:latest**: Latest Llama model")
        st.write("- **llama2-uncensored**: Less restricted responses")
        
        if st.button("🔄 Refresh Models"):
            st.rerun()


if __name__ == "__main__":
    page()
