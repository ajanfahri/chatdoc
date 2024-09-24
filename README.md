## Project Title
NLP Text Exploration Application

## Brief Description
This application utilizes NLP techniques to provide a user-friendly interface for exploring and querying text documents. It integrates various NLP pipelines to extract knowledge from text, including text extraction from PDFs, text chunking, vectorization, and conversational question answering.

## Key Features
- PDF Text Extraction: Extracts text from PDF documents.
- Text Chunking: Splits text into smaller chunks for efficient processing.
- Text Vectorization: Converts text into numerical vectors using Google's Generative AI Embeddings.
- Conversational Question Answering: Uses a chain-of-thought model to answer questions about the text.
- User-Friendly Interface: Provides a simple and intuitive interface for text exploration and querying.

## Basic Installation & Usage
1. Install the required dependencies:
```
pip install -r requirements.txt
```

2. Run the main application:
```
streamlit run streamlitapp.py
```

## License
MIT License

Copyright (c) [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.