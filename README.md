# BlogWriter_Agent

This repository hosts **BlogWriter_Agent**, a multi-agent system for collaborative blog content generation using the **CrewAI** and **Ollama** frameworks. The system is designed to facilitate the creation of high-quality blog content through autonomous agents that handle content planning, writing, and editing in a coordinated workflow.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Agents](#agents)

## Introduction

**BlogWriter_Agent** automates the blog writing process using three specialized AI agents:
1. **Content Planner**: Plans the blog structure and gathers relevant information.
2. **Content Writer**: Writes content based on the planner's structure and guidelines.
3. **Content Editor**: Refines and edits the content to match stylistic and grammatical standards.

This project leverages the **CrewAI** framework to coordinate agent tasks and **Ollama** for local LLM management, with agents set up to perform tasks autonomously or in a collaborative fashion.

## Features

- **Multi-agent workflow**: Allows agents to work collaboratively, each with specialized roles.
- **LLM integration**: Easily switchable models using Ollama’s local model setup.
- **Configurable parameters**: Define agent roles, goals, and objectives with flexibility.
- **Privacy-focused**: Runs models locally, so your data never leaves your machine.

## Requirements

- **Python 3.8+**
- **Ollama** for local LLM management
- **CrewAI** for multi-agent orchestration

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/srishrachamalla7/BlogWriter_Agent.git
    cd BlogWriter_Agent
    ```

2. **Install dependencies**:
    ```bash
    pip install crewai==0.28.8 crewai_tools==0.1.6 langchain_community==0.0.29 
    ```
    OR
   ```bash
    pip install -r requirements.txt
    ```

4. **Install Ollama**:
   - Download and install the Ollama app for your operating system from [Ollama's website](https://ollama.com).
   - Set the default path for storing downloaded models or configure the path using environment variables if needed.

5. **Download the Llama 3 model**:
    ```bash
    ollama run llama3
    ```

## Usage

1. **Set up the LLM with Ollama**:
   - Create a `ModelFile` in your project directory with the following setup:
     ```Dockerfile
     FROM llama3

     PARAMETER temperature 0.3
     PARAMETER stop Result
     SYSTEM ""
     ```
   - Run the following command to set up the model in Ollama:
     ```bash
     ollama create crewai-llama3 -f .\ModelFile
     ```

2. **Configure environment variables**:
    - Make your OpenAI API Key:
      ```bash
      export OPENAI_API_KEY= 'NA'
      ```

3. **Run the script**:
   - The agents are set up in `main.py` with their respective roles. Execute the following to start the agents:
     ```bash
     python main.py
     ```

## Configuration

 where you can modify:

- **LLM model**: Set to use Meta Llama 3 by default.
- **Agent parameters**: Roles, goals, maximum iteration count, verbose logging, and more.
- **Tasks**: Define tasks to be executed by each agent.

## Agents

### Content Planner Agent
The Content Planner agent generates an outline for the blog post, including relevant topics and subtopics.

- **Role**: Content Planner
- **Goal**: Generate an informative, structured content outline.
- **Parameters**: Delegation disabled, verbose logging enabled.

### Content Writer Agent
The Content Writer uses the planner’s outline to create a comprehensive draft with factual accuracy and depth.

- **Role**: Content Writer
- **Goal**: Write high-quality content based on the outline provided by the planner.
- **Parameters**: Delegation disabled, verbose logging enabled.

### Content Editor Agent
The Content Editor refines and polishes the draft to ensure it meets professional standards and fits the publishing platform’s style guidelines.

- **Role**: Editor
- **Goal**: Edit the content for style, grammar, and adherence to journalistic standards.
- **Parameters**: Delegation disabled, verbose logging enabled.

---
