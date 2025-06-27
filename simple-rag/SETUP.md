# Setup Guide: PDF Chat with Ollama on Mac

This guide will help you set up and run the PDF chat application locally on your Mac using Python 3.11/3.12 and Ollama.

## Prerequisites

- macOS (tested on macOS 13+)
- Homebrew (for installing pyenv)
- At least 8GB RAM (16GB recommended for larger models)
- At least 10GB free disk space

## Step 1: Install Python 3.11 or 3.12

The project requires Python 3.11 or 3.12 due to compatibility issues with Python 3.13 and some AI/ML libraries.

### Option A: Using pyenv (Recommended)

1. **Install pyenv** (if not already installed):
   ```bash
   brew install pyenv
   ```

2. **Add pyenv to your shell** (add to `~/.zshrc` or `~/.bash_profile`):
   ```bash
   echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
   echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
   echo 'eval "$(pyenv init -)"' >> ~/.zshrc
   ```

3. **Restart your terminal** or run:
   ```bash
   source ~/.zshrc
   ```

4. **Install Python 3.11.9**:
   ```bash
   pyenv install 3.11.9
   ```

5. **Set Python version for this project**:
   ```bash
   cd /Users/murgod/work/apps/local-assistant-examples/simple-rag
   pyenv local 3.11.9
   ```

### Option B: Using Python.org Installer

1. Download Python 3.11.9 from [python.org](https://www.python.org/downloads/)
2. Install the downloaded package
3. Verify installation:
   ```bash
   python3.11 --version
   ```

## Step 2: Install Ollama

1. **Download and install Ollama** from [ollama.ai](https://ollama.ai/)
2. **Verify installation**:
   ```bash
   ollama --version
   ```

3. **Pull a model** (we'll use qwen2.5 as specified in the code):
   ```bash
   ollama pull qwen2.5
   ```

## Step 3: Set Up Python Environment

1. **Navigate to the project directory**:
   ```bash
   cd /Users/murgod/work/apps/local-assistant-examples/simple-rag
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   ```bash
   source venv/bin/activate
   ```

4. **Upgrade pip**:
   ```bash
   pip install --upgrade pip
   ```

5. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Step 4: Run the Application

1. **Make sure Ollama is running**:
   ```bash
   ollama serve
   ```
   (Keep this running in a separate terminal)

2. **Start the Streamlit application**:
   ```bash
   streamlit run app.py
   ```

3. **Open your browser** and go to the URL shown in the terminal (usually `http://localhost:8501`)

## Step 5: Using the Application

1. **Upload a PDF document** using the file uploader
2. **Wait for ingestion** (you'll see a progress message)
3. **Ask questions** about the document in the chat interface
4. **Get AI-powered answers** based on the document content

## Troubleshooting

### Common Issues

1. **Python version issues**:
   - Make sure you're using Python 3.11 or 3.12
   - Check with: `python --version`

2. **Ollama connection issues**:
   - Ensure Ollama is running: `ollama serve`
   - Check if the model is downloaded: `ollama list`

3. **Memory issues**:
   - Close other applications to free up RAM
   - Consider using a smaller model if you have limited RAM

4. **Port conflicts**:
   - If port 8501 is in use, Streamlit will automatically use the next available port
   - Check the terminal output for the correct URL

### Model Options

You can change the model in `rag.py` by modifying the `llm_model` parameter:

```python
def __init__(self, llm_model: str = "qwen2.5"):
```

Available models include:
- `qwen2.5` (default, good balance of speed and quality)
- `mistral` (faster, smaller)
- `llama3.2` (larger, higher quality)
- `codellama` (good for technical documents)

To use a different model:
1. Pull it: `ollama pull <model_name>`
2. Update the code or pass it as a parameter

## Project Structure

```
simple-rag/
├── app.py              # Streamlit web interface
├── rag.py              # RAG implementation
├── requirements.txt    # Python dependencies
├── README.md          # Original project documentation
├── SETUP.md           # This setup guide
└── venv/              # Virtual environment (created during setup)
```

## Features

- **PDF Document Upload**: Upload and process PDF files
- **Vector Storage**: Uses Chroma for efficient document storage
- **Semantic Search**: FastEmbed embeddings for document retrieval
- **Chat Interface**: Streamlit-based web UI
- **Local Processing**: Everything runs locally on your machine
- **Persistent Storage**: Document embeddings are saved between sessions

## Next Steps

Once you have the basic application running, you can:

1. **Experiment with different models** by changing the `llm_model` parameter
2. **Upload larger documents** to test the system's capabilities
3. **Customize the prompt** in `rag.py` for different use cases
4. **Add conversation memory** to maintain context across multiple questions
5. **Implement multi-document support** for comparing information across files

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Ensure all prerequisites are installed correctly
3. Verify Python version compatibility
4. Check that Ollama is running and the model is downloaded

Happy chatting with your PDFs! 📚🤖 