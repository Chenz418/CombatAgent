# TradingAgents/graph/conditional_logic_combat.py

from combatagents.agents.utils.agent_states_combat import AgentStateCombat


class ConditionalLogicCombat:
    """Handles conditional logic for determining graph flow."""

    def __init__(self, max_debate_rounds=100):
        """Initialize with configuration parameters."""
        self.max_debate_rounds = max_debate_rounds
    def should_continue_positive(self, state: AgentStateCombat) -> str:
        """Determine if positive combat should continue."""

        if (
            state["count"] >= self.max_debate_rounds or state["debate_status"] == "concluded"
        ):  # 3 rounds of back-and-forth between 2 agents
            print(f"Debate concluded after {state['count']} rounds after positive combater's turn.")
            return "END"
        else:
            return "positive"
    def should_continue_negative(self, state: AgentStateCombat) -> str:
        """Determine if negative combat should continue."""

        if (
            state["count"] >= self.max_debate_rounds or state["debate_status"] == "concluded"
        ):  # 3 rounds of back-and-forth between 2 agents
            print(f"Debate concluded after {state['count']} rounds after negative combater's turn.")
            return "END"
        else:
            return "negative"