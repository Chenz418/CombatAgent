from langchain_core.messages import AIMessage
import time
import json
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import os


def create_positive_combater(llm, language_style, debate_language, folder):
    def positive_node(state) -> dict:
        positive_stance = state["positive_stance"]
        negative_stance = state["negative_stance"]
        topic = state['topic']
        # Prepare the data dictionary for the prompt
        # prompt_variables = {
        #     "topic": topic,
        #     "current_response": state["current_response"],
        #     "negative_combater_history": state["negative_combater_history"],
        #     "history": state["history"]
        # }

#         debate_prompt = ChatPromptTemplate.from_messages([
#             ("system", f"""
#     You are a world-class logic-driven debater. Your goal is to dismantle the opponent's stance on: "{topic}". Please debate in {debate_language} with a {language_style} style.
#     Your stance: {positive_stance}. Your opponent's stance: {negative_stance}.

#     CONSTRAINTS (NON-NEGOTIABLE):
#     1. MAX LENGTH: Your response must be under 50 words. No long paragraphs.
#     2. PUNCHY LOGIC: Use 1-2 powerful sentences. Hit the core flaw in their reasoning immediately.
#     3. NO FLUFF: Skip greetings ("I understand your point", "Hello"). Go straight for the jugular.
#     4. THE STOPPER: If the opponent proves a logical paradox you cannot escape, respond ONLY with: [I_CONCEDE]. Remember no matter what language you use in the debate, always use [I_CONCEDE] to terminate the debate. 
#     5. If you can't see any debate history, don't worry, it is because the one to start the debate, just make your opening argument based on the topic."""),
#            ("human", """The debating process is as follows:
# 1. The very last argument of your opponent: {current_response}
# 2. The total argument history of your opponent: {negative_combater_history}
# 3. The total argument history of you and your opponent: {history}""")
#         ])
        debate_prompt = ChatPromptTemplate.from_messages([
                    ("system", f"""
            You are a world-class logic-driven debater: "Positive_Combater". Your goal is to dismantle the opponent's stance on: "{topic}". Please debate in {debate_language} with a {language_style} style.
            Your stance: {positive_stance}.

            CONSTRAINTS (NON-NEGOTIABLE):
            1. PUNCHY LOGIC: Use 1-2 powerful sentences. Hit the core flaw in their reasoning immediately.
            2. NO FLUFF: Skip greetings ("I understand your point", "Hello"). Go straight for the jugular.
            3. THE STOPPER: If the opponent proves a logical paradox you cannot escape, respond ONLY with: [I_CONCEDE]. Remember no matter what language you use in the debate, always use [I_CONCEDE] to terminate the debate. 
            4. If you can't see any debate history, don't worry, it is because the one to start the debate, just make your opening argument based on the topic.
            """),
                MessagesPlaceholder(variable_name="messages"),
                ])


        chain = debate_prompt | llm
        response = chain.invoke(state['messages']) 
        
        argument = f"Positive Combater: {response.content}"
        file_name = "combat_log.txt"
        file_path = os.path.join(folder, file_name)
        append_content = f"round{state["count"]+1}" + "\n" + "-" *20 + '\n' + argument
        with open(file_path, "a", encoding="utf-8") as file:
            # Adding a newline (\n) ensures this argument starts on its own line
            file.write(append_content + "\n")
            
            # Optional: Add a visual separator for better readability
            file.write("-" * 20 + "\n")
        argument_sealed = AIMessage(content=response.content, name="Positive_Combater")

        # new_combat_state = {
        #     "history": state["history"] + "\n" + argument,
        #     "positive_combater_history": state["positive_combater_history"] + "\n" + argument,
        #     "negative_combater_history": state["negative_combater_history"],
        #     "current_response": argument,
        #     "count": state["count"] + 1,
        # }

        # Check for concession
        if "[I_CONCEDE]" in response.content:
            print(f"Agent representing {positive_stance} has conceded.")
            return {"messages": [argument_sealed], "debate_status": "concluded"}
        
        return {"messages": [argument_sealed], "count": state["count"] + 1}
            

    return positive_node
