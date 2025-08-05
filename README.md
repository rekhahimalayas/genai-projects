GEN AI & LLM Projects – Agentic AI Workflows

This repository is a curated collection of hands-on projects exploring the development of Generative AI (GenAI), Large Language Models (LLMs), and Agentic AI workflows 
using cutting-edge tools and technologies like LangChain, LangGraph, Streamlit, MCP, Gemini, RAG and Chroma.

These projects demonstrate how to build intelligent, autonomous agents capable of reasoning, planning, tool use, and interacting with multimodal environments.

-----------------------------------------------------------------------------------------------------------------------------

Features

	• LangGraph-based chatbots and agent workflows
	• Prebuilt and custom tool integrations
	• Retrieval-Augmented Generation (RAG) with Chroma
	• Streamlit UI for chat and multimodal interaction
	• MCP integration for filesystem and GitHub access
	• Custom MCP server implementations
	• Multi-agent systems (Supervisor and Swarm architectures)
	• Gemini-powered image generation and captioning

-----------------------------------------------------------------------------------------------------------------------------

Getting Started

	# Create virtual environment
	python -m venv venv
	source venv/bin/activate  # Mac/Linux
	# OR
	venv\Scripts\activate      # Windows
	
 	# Install dependencies
	pip install -r requirements.txt

	## Environment Variables
	Create a `.env` file with the following keys:
	```ini
	OPENAI_API_KEY=your_openai_key  
	GROQ_API_KEY=your_groq_key  
	GITHUB_TOKEN=your_github_token  
	GOOGLE_API_KEY=your_google_api_key 
	
-----------------------------------------------------------------------------------------------------------------------------

Projects Included

	• LangGraph-Based Chatbot
		○ Implements a LangGraph-powered agent that handles multi-turn conversations.
		○ Integrates memory and reasoning over tool outputs.
		○ Having structured responses
		○ Leveraging MCP architecture for tools to build agents 
		○ Tools/Aprroaches Used: LangChain, LangGraph, GROK, OPENAI.
		○ Used prebuilt tools and custom tool
		○ Created MCP Server and MCP Client for Agent development

	• Structured Responses
		○ Generate structured replies using Pydantic models
		○ Examples: email generation, travel itineraries, health reports

	• MCP Integrations
		○ Connect to GitHub and filesystem MCP servers
		○ List files, create/edit files, execute file operations securely
   
	• Custom MCP Server
		○ Create tools like addFile() and addFolder() with FastMCP
		○ Use in agent workflows to manipulate local directories

	• Multi-Agent Architectures
		○ Supervisor Architecture
			§ Example agents:
				□     Resume Reviewer
				□     Mock Interviewer
				□     Feedback Generator
				□     Document Validator

		○ Swarm Architecture
			§ Example agents:
				□     Researcher
				□     Summarizer
				□     Critic
				□     Fact Checker

		○ Related repositories:
			§ LangGraph Supervisor
			§ LangGraph Swarm

	• Local Model Execution with Ollama
		○     Run LLaMA, Mistral, Gemma models offline
		○     No internet needed after model download
		○     More at:  https://ollama.com
		
	• Documentation and References
		○ LangChain
		○ LangGraph
		○ MCP Protocol
		○ Streamlit
		○ Gemini API
		○ HuggingFace

-----------------------------------------------------------------------------------------------------------------------------
