# CombatAgents/graph/setup.py

from typing import Dict, Any
from langchain_openai import ChatOpenAI
from langgraph.graph import END, StateGraph, START
from langgraph.prebuilt import ToolNode

from tradingagents.agents import *
from tradingagents.agents.utils.agent_states_combat import AgentStateCombat

from .conditional_logic_combat import ConditionalLogicCombat


class GraphSetupCombat:
    """Handles the setup and configuration of the agent graph."""

    def __init__(
        self,
        llm_engine: ChatOpenAI,
        conditional_logic: ConditionalLogicCombat,
        language_style: str,
        debate_language: str,
        folder: str
    ):
        """Initialize with required components."""
        self.llm = llm_engine
        self.conditional_logic = conditional_logic
        self.language_style = language_style
        self.debate_language = debate_language
        self.folder = folder
    def setup_graph(
        self):
        """Set up and compile the agent workflow graph.
        """
         # Create researcher and manager nodes
        debate_architect_node = create_debate_architect(
            self.llm,
            self.folder,
            self.debate_language,
        )
        positive_combater_node = create_positive_combater(
            self.llm,
            self.language_style,
            self.debate_language,
            self.folder,
        )
        negative_combater_node = create_negative_combater(
            self.llm,
            self.language_style,
            self.debate_language,
            self.folder,
        )
        # Create workflow
        workflow = StateGraph(AgentStateCombat)
        workflow.add_node("positive", positive_combater_node)
        workflow.add_node("negative", negative_combater_node)
        workflow.add_node("debate_architect", debate_architect_node)

        workflow.add_edge(START, "debate_architect")
        workflow.add_edge("debate_architect", "positive")
        workflow.add_conditional_edges("positive",
                                        self.conditional_logic.should_continue_negative, 
                                        {"negative": "negative",
                                         "END": END})
        workflow.add_conditional_edges("negative",
                                        self.conditional_logic.should_continue_positive,    
                                        {"positive": "positive",
                                         "END": END})
        return workflow.compile()
