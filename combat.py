from tradingagents.graph.trading_graph_combat import TradingAgentsGraphCombat
from tradingagents.default_config_combat import DEFAULT_CONFIG

from dotenv import load_dotenv
import time
# Load environment variables from .env file
load_dotenv()

# Create a custom config
config = DEFAULT_CONFIG.copy()
config["deep_think_llm"] = "gpt-4o-mini"  # Use a different model
config["quick_think_llm"] = "gpt-4o-mini"  # Use a different model
config["max_debate_rounds"] = 100  # Increase debate rounds


# Initialize with custom config
ta = TradingAgentsGraphCombat(debug=True, config=config)

# forward propagate
decision = ta.propagate(config["topic"])
print(decision)

# Memorize mistakes and reflect
# ta.reflect_and_remember(1000) # parameter is the position returns
