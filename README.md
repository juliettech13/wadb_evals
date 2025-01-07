# LLM Evaluations Workshop

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/altryne/llm-evals-workshop/blob/main/eval.ipynb) [![Weights & Biases](https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-gradient.svg)](https://wandb.ai)

A workshop project demonstrating how to build and evaluate LLM-powered classification systems using real-world data from Bluesky social network.

## Overview

This project showcases a practical example of building an LLM evaluation pipeline using:
- Bluesky posts as source data
- OpenAI's GPT-4 for classification
- Weights & Biases (Weave) for evaluation tracking
- Gradio for the interactive UI

The system classifies Bluesky posts into three categories:
- **Doomer**: Users who express strong negative sentiment towards AI, often using derogatory language
- **Boomer**: Users who show lack of understanding about AI/data collection, often requesting data removal
- **Neither**: Users with neutral or positive responses

## Setup

1. Clone the repository:
```bash
git clone https://github.com/altryne/llm-evals-workshop
```

2. Install dependencies:
```bash
pip install uv
uv pip install -r requirements.txt
```

3. Set up environment variables:
Copy `.env.example` to `.env` and fill in your credentials:
```
WANDB_API_KEY=your-wandb-key
OPENAI_API_KEY=your-openai-key
GEMINI_API_KEY=your-gemini-key
```

## Features

- **Interactive UI**: Built with Gradio for easy post classification and feedback collection
- **Evaluation Pipeline**: Uses Weights & Biases Weave for tracking model performance
- **Dataset Creation**: Tools for building annotated datasets from Bluesky posts
- **Multi-Model Support**: Supports multiple LLM providers (OpenAI, Gemini)

## Usage

1. Run the Jupyter notebook:
```bash
jupyter notebook eval.ipynb
```

2. Use the Gradio interface to:
   - View random Bluesky posts
   - See AI classifications
   - Provide human annotations
   - Build evaluation datasets

## Project Structure

- `eval.ipynb`: Main notebook with implementation and UI
- `templates/`: HTML templates for post display
- `data/`: JSON files containing Bluesky posts
- `.env`: Configuration for API keys and credentials

## Contributing

Feel free to open issues or submit pull requests with improvements.

## License

[Add your license information here] 