from typing import Annotated, Sequence
from datetime import date, timedelta, datetime
from typing_extensions import TypedDict, Optional
from langchain_openai import ChatOpenAI
from tradingagents.agents import *
from langgraph.prebuilt import ToolNode
from langgraph.graph import END, StateGraph, START, MessagesState

class AgentStateCombat(MessagesState):
    topic: Annotated[
        str, "Debate Topic"]
    positive_stance: Annotated[
        str, "Positive stance of the agent"]
    negative_stance: Annotated[
        str, "Negative stance of the agent"]
    positive_combater_history: Annotated[
        str, "Positive Combater Conversation history"]
    negative_combater_history: Annotated[
        str, "Negative Combater Conversation history"]
    history: Annotated[str, "Conversation history"]  # Conversation history
    current_response: Annotated[str, "Latest response"]  # Last response
    count: Annotated[int, "Length of the current conversation"]
    debate_status: Annotated[str, "the status for debating process"]  # Conversation length

