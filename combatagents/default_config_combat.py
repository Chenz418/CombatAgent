import os

DEFAULT_CONFIG = {
    "project_dir": os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
    "results_dir": os.getenv("TRADINGAGENTS_RESULTS_DIR", "./results"),
    "data_dir": "/Users/yluo/Documents/Code/ScAI/FR1-data",
    "data_cache_dir": os.path.join(
        os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
        "dataflows/data_cache",
    ),
    #combat settings
    "language_style": "casual",
    "debate_language": "English",
    'topic': "Stephen Curry vs Lebron James, who is the better basketball player?",
    # LLM settings
    "llm_provider": "openai",
    "llm_positive": "gpt-4o-mini",
    "llm_negative": "gpt-4o-mini",
    "backend_url": "https://api.openai.com/v1",
    # Debate and discussion settings
    "max_debate_rounds": 100
}
