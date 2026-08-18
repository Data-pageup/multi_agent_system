# Multi-Research Agent

A research-focused multi-agent system built with **LangChain**.

The main purpose of this project is to perform research by finding information from multiple sources, extracting relevant content, generating a report, and having a critic review the result.

## Workflow

    User
      ↓
    Search Agent
      ↓
    Reader Agent
      ↓
    Writer Chain
      ↓
    Critic Chain
      ↓
    Research Report

## Components

### 1. Search Agent

Performs the initial web research and finds relevant sources for the given topic.

Output:

    search_results

### 2. Reader Agent

Works with the search results and identifies useful sources.

It uses a URL scraping tool to extract deeper content from selected webpages.

Output:

    scraped_content

### 3. Writer Chain

Combines the search results and scraped content to generate a structured research report.

Output:

    report

### 4. Critic Chain

Reviews the generated report and provides feedback instead of directly accepting the Writer's output.

Output:

    feedback

## State

A shared state is used to pass information between different stages of the workflow.

    State
    ├── topic
    ├── search_results
    ├── scraped_content
    ├── report
    └── feedback

This allows each stage to access information produced by previous stages.

## Tools

The project currently uses tools for:

- Web searching
- URL scraping

These tools allow the agents to retrieve external information instead of relying entirely on the LLM's existing knowledge.

## Project Structure

    Multi_Research_agent/
    │
    ├── src/
    │   ├── agents/
    │   │   └── agents.py
    │   │
    │   ├── pipeline/
    │   │   └── pipeline.py
    │   │
    │   └── tools/
    │       └── tools.py
    │
    ├── main.py
    ├── .env
    ├── .gitignore
    ├── pyproject.toml
    └── README.md

## Tech Stack

- Python
- LangChain
- LLM
- Web Search
- Web Scraping
- Multi-Agent Architecture

For more complex agent workflows, frameworks such as **LangGraph** and **CrewAI** can be used to manage agents, tools, state, and execution flow.

## Example

A research question such as:

    Why did NVIDIA become dominant in the generative AI era
    while Intel and AMD failed to capture the same opportunity?

can go through the complete pipeline:

    Research Question
           ↓
       Web Search
           ↓
     Relevant Sources
           ↓
      Source Scraping
           ↓
     Research Content
           ↓
    Report Generation
           ↓
      Critical Review
           ↓
    Final Research Report

## Current Status

This project is currently a local prototype.

It has not been deployed because a multi-agent workflow can generate multiple LLM/API calls during a single research task, which can significantly increase API usage and cost.

## Future Improvements

- Persistent storage
- Conversational research
- Better source ranking
- Parallel research agents
- Improved report evaluation
- Web interface
- Deployment
- Cost and token optimization

## Author

**Amirtha Ganesh R**
