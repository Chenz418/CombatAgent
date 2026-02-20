from langchain_core.messages import AIMessage
import time
import json
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import os

def create_negative_combater(llm, language_style, debate_language, folder):
    def negative_node(state) -> dict:
        negative_stance = state["negative_stance"]
        positive_stance = state["positive_stance"]
        topic = state['topic']
        # Prepare the data dictionary for the prompt
        # prompt_variables = {
        #     "topic": topic,
        #     "current_response": state["current_response"],
        #     "positive_combater_history": state["positive_combater_history"],
        #     "history": state["history"]
        # }

#         debate_prompt = ChatPromptTemplate.from_messages([
#             ("system", f"""
#     You are a world-class logic-driven debater. Your goal is to dismantle the opponent's stance on: "{topic}". Please debate in {debate_language} with a {language_style} style.
#     Your stance: {negative_stance}. Your opponent's stance: {positive_stance}.

#     CONSTRAINTS (NON-NEGOTIABLE):
#     1. MAX LENGTH: Your response must be under 50 words. No long paragraphs.
#     2. PUNCHY LOGIC: Use 1-2 powerful sentences. Hit the core flaw in their reasoning immediately.
#     3. NO FLUFF: Skip greetings ("I understand your point", "Hello"). Go straight for the jugular.
#     4. THE STOPPER: If the opponent proves a logical paradox you cannot escape, respond ONLY with: [I_CONCEDE]. Remember no matter what language you use in the debate, always use [I_CONCEDE] to terminate the debate. 
#     """),
#            ("human", """The past debating content is as follows:
# 1. The very last argument of your opponent: {current_response}
# 2. The total argument history of your opponent: {positive_combater_history}
# 3. The total argument history of you and your opponent: {history}""")
#         ])
        debate_prompt = ChatPromptTemplate.from_messages([
            ("system", f"""
    You are a world-class logic-driven debater: "Negative_Combater". Your goal is to dismantle the opponent's stance on: "{topic}". Please debate in {debate_language} with a {language_style} style.
    Your stance: {negative_stance}.

    CONSTRAINTS (NON-NEGOTIABLE):
    1. PUNCHY LOGIC: Use 1-2 powerful sentences. Hit the core flaw in their reasoning immediately.
    2. NO FLUFF: Skip greetings ("I understand your point", "Hello"). Go straight for the jugular.
    3. THE STOPPER: If the opponent proves a logical paradox you cannot escape, respond ONLY with: [I_CONCEDE]. Remember no matter what language you use in the debate, always use [I_CONCEDE] to terminate the debate. 
    4. If you find your opponent has already debate for your instance, you must remind your opponent and force your opponent to concede.
    """),
           MessagesPlaceholder(variable_name="messages"),
        ])

        chain = debate_prompt | llm
        response = chain.invoke(state['messages']) 
        
        argument = f"Negative Combater: {response.content}"

        file_name = "combat_log.txt"
        file_path = os.path.join(folder, file_name)
        append_content = argument
        with open(file_path, "a", encoding="utf-8") as file:
            # Adding a newline (\n) ensures this argument starts on its own line
            file.write(append_content + "\n")
            
            # Optional: Add a visual separator for better readability
            file.write("-" * 20 + "\n")

        # new_combat_state = {
        #     "topic": state["topic"],
        #     "history": state["history"] + "\n" + argument,
        #     "positive_combater_history": state["positive_combater_history"],
        #     "negative_combater_history": state["negative_combater_history"] + "\n" + argument,
        #     "current_response": argument,
        #     "count": state["count"],
        # }

        print(f"The {state['count']}th round is finished \n")
        argument_sealed = AIMessage(content=response.content, name="Negative_Combater")

        # Check for concession
        if "[I_CONCEDE]" in response.content:
            print(f"Agent representing {negative_stance} has conceded.")
            return {"messages": [argument_sealed], "debate_status": "concluded"}
        
        print("Debate continues...\n")
        
        return {"messages": [argument_sealed]}

    return negative_node
