# LLM Evaluations Workshop

A workshop project demonstrating how to build and evaluate LLM-powered classification systems using real-world data from Bluesky social network.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/altryne/llm-evals-workshop/blob/main/eval.ipynb) 

## Overview

This workshop explores a comprehensive methodology for productizing robust LLM applications through tracing, dataset creation, and evaluation. Using [W&B Weave](https://wandb.me/weave-workshop-jan), we'll explore how to build reliable evaluation pipelines for LLM applications.

The project showcases a practical example of building an LLM evaluation pipeline using:
- Bluesky posts as source data
- OpenAI's GPT-4 and other LLMs for classification
- Weights & Biases (Weave) for evaluation tracking and dataset versioning
- Gradio for the interactive UI

## Setup

You can run this workshop directly in Colab by clicking the badge above. To run locally:

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
WANDB_API_KEY=your-wandb-api-key-here
OPENAI_API_KEY=your-openai-api-key-here
GEMINI_API_KEY=your-gemini-api-key-here
OPENROUTER_API_KEY=your-openrouter-api-key-here
```

## Features

- **Interactive UI**: Built with Gradio for easy post classification and feedback collection
- **Evaluation Pipeline**: Uses Weights & Biases Weave for:
  - Tracing LLM calls and responses
  - Dataset versioning and management
  - Evaluation tracking and analysis
- **Dataset Creation**: Tools for building and annotating datasets from Bluesky posts
- **Multi-Model Support**: Supports multiple LLM providers (OpenAI, Gemini, OpenRouter)
- **Comprehensive Evaluation Methods**:
  - Programmatic scoring for structured outputs
  - Human-in-the-loop (HITL) annotations
  - LLM-as-judge evaluations

## Evaluation Approaches

The workshop covers three main evaluation methods:

1. **Programmatic Scoring**
   - Fast and reliable for structured outputs
   - Uses string matching and regex
   - Best for exact match or pattern-based evaluation
   - Example: Checking if LLM classification matches ground truth

2. **Human-in-the-Loop (HITL)**
   - Manual review and annotation
   - Creates high-quality ground truth data
   - Used for kickstarting evaluation datasets
   - Interactive UI for efficient annotation

3. **LLM-as-Judge**
   - Uses LLMs to evaluate other LLMs
   - Handles open-ended responses
   - Cost-effective alternative to human evaluation
   - Includes best practices and limitations

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

## Author

Created by [Alex Volkov](https://twitter.com/altryne) for Weights & Biases
