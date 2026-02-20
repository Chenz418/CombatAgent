# TradingAgents/graph/propagation.py

from typing import Dict, Any
from tradingagents.agents.utils.agent_states_combat import AgentStateCombat


class PropagatorCombat:
    """Handles state initialization and propagation through the graph."""

    def __init__(self, max_recur_limit=100):
        """Initialize with configuration parameters."""
        self.max_recur_limit = max_recur_limit * 2 + 1 # Each round has a turn for both positive and negative combater

    def create_initial_state(
        self, topic: str
    ) -> Dict[str, Any]:
        """Create the initial state for the agent graph."""
        return {
            "topic": topic,
            "positive_combater_history": "",
            "negative_combater_history": "",
            "history": "",
            "current_response": "",
            "count": 0,
            "debate_status": "",
        }

    def get_graph_args(self) -> Dict[str, Any]:
        """Get arguments for the graph invocation."""
        return {
            "stream_mode": "values",
            "config": {"recursion_limit": self.max_recur_limit},
        }