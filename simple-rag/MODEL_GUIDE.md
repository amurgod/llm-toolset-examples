# Ollama Model Guide for Your System

Based on your `ollama list` output, here are the models available on your Mac and how to use them effectively.

## Your Available Models

| Model | Size | Best For | Characteristics |
|-------|------|----------|-----------------|
| `mistral:latest` | 4.1 GB | General purpose | Balanced performance, good reasoning |
| `llama3.2:latest` | 2.0 GB | Latest features | Newest Llama model, good coding |
| `llama2-uncensored:latest` | 3.8 GB | Creative tasks | Less restricted, more creative responses |
| `llama3.2-k8s-gpt:latest` | 2.0 GB | Kubernetes/GPT | Specialized for K8s and GPT topics |
| `nomic-embed-text:latest` | 274 MB | Embeddings only | Not for chat, used for document embeddings |

## How to Use Different Models

### 1. **mistral:latest** (Recommended Default)
```python
# In your code
chat_pdf = ChatPDF(llm_model="mistral:latest")
```

**Best for:**
- General PDF analysis
- Balanced responses
- Good reasoning capabilities
- Stable performance

### 2. **llama3.2:latest** (Latest Features)
```python
chat_pdf = ChatPDF(llm_model="llama3.2:latest")
```

**Best for:**
- Technical documents
- Code-related content
- Latest AI capabilities
- Structured responses

### 3. **llama2-uncensored:latest** (Creative)
```python
chat_pdf = ChatPDF(llm_model="llama2-uncensored:latest")
```

**Best for:**
- Creative writing
- Less restricted topics
- Alternative viewpoints
- Experimental content

### 4. **llama3.2-k8s-gpt:latest** (Specialized)
```python
chat_pdf = ChatPDF(llm_model="llama3.2-k8s-gpt:latest")
```

**Best for:**
- Kubernetes documentation
- GPT-related content
- Technical infrastructure
- DevOps topics

## Model Switching in the App

### Using the Web Interface

1. **Start the app:**
   ```bash
   streamlit run app.py
   ```

2. **Select your model:**
   - Use the dropdown menu to choose your preferred model
   - The app will automatically switch models
   - Chat history will be cleared when switching models

3. **Model recommendations:**
   - **For general use**: `mistral:latest`
   - **For technical docs**: `llama3.2:latest`
   - **For creative content**: `llama2-uncensored:latest`

### Using Python Code

```python
from rag_improved import ChatPDF

# Initialize with a specific model
chat_pdf = ChatPDF(llm_model="mistral:latest")

# Switch models dynamically
chat_pdf.change_model("llama3.2:latest")

# Check available models
available_models = ChatPDF.get_available_models()
print(f"Available: {available_models}")

# Get model info
info = chat_pdf.get_model_info()
print(f"Current: {info['current_model']}")
```

## Performance Considerations

### Memory Usage
- **mistral:latest** (4.1 GB): Highest memory usage, best performance
- **llama2-uncensored:latest** (3.8 GB): High memory, creative responses
- **llama3.2:latest** (2.0 GB): Moderate memory, good balance
- **llama3.2-k8s-gpt:latest** (2.0 GB): Moderate memory, specialized

### Speed vs Quality Trade-offs
- **Faster responses**: `llama3.2:latest`, `llama3.2-k8s-gpt:latest`
- **Better quality**: `mistral:latest`, `llama2-uncensored:latest`

## Testing Your Models

Run the test script to verify all models work:

```bash
python test_models.py
```

This will:
- Test model switching functionality
- Verify each model responds correctly
- Show performance characteristics

## Model-Specific Prompts

### For mistral:latest
```
"Please provide a comprehensive analysis of this document, focusing on key insights and actionable recommendations."
```

### For llama3.2:latest
```
"Analyze this technical document and provide structured insights with clear sections."
```

### For llama2-uncensored:latest
```
"Give me a creative interpretation of this content, including alternative perspectives."
```

### For llama3.2-k8s-gpt:latest
```
"Focus on the technical aspects, especially any Kubernetes or GPT-related content."
```

## Troubleshooting

### Model Not Found
```bash
# Pull a specific model
ollama pull mistral:latest
ollama pull llama3.2:latest
```

### Model Loading Issues
```bash
# Check if Ollama is running
ollama serve

# List available models
ollama list
```

### Memory Issues
- Close other applications
- Use smaller models for large documents
- Consider using `llama3.2:latest` for better memory efficiency

## Recommendations

### For Different Use Cases

1. **Academic Papers**: `mistral:latest`
2. **Technical Documentation**: `llama3.2:latest`
3. **Creative Writing**: `llama2-uncensored:latest`
4. **Kubernetes/DevOps**: `llama3.2-k8s-gpt:latest`
5. **General Business**: `mistral:latest`

### For Different Document Types

- **PDFs with tables/data**: `llama3.2:latest`
- **Narrative content**: `mistral:latest`
- **Technical manuals**: `llama3.2-k8s-gpt:latest`
- **Creative content**: `llama2-uncensored:latest`

## Next Steps

1. **Test all models** with your specific documents
2. **Compare responses** to find your preferred model
3. **Optimize prompts** for each model's strengths
4. **Consider document type** when choosing models

Happy experimenting with your models! 🚀 