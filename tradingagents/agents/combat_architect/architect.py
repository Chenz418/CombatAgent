from langchain_core.messages import AIMessage
import time
import json
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import os

def create_debate_architect(llm, folder, language):
    def debate_architect_node(state) -> dict:
        topic = state['topic']

        debate_prompt = ChatPromptTemplate.from_messages([
            ("system", f"""You are a Debate Architect. Your job is to take a general question or topic and extract two diametrically opposed, clearly stated stances.
             Please constitute the stances in {language}.
    
    OUTPUT FORMAT:
    You must return your response in the following structured format:
    POSITIVE_STANCE: [The first clear position]
    NEGATIVE_STANCE: [The opposing clear position]
    
    RULES:
    1. Be direct: Avoid phrases like "One side argues that..." or "On the other hand...".
    2. Be balanced: Ensure both stances sound equally authoritative.
    3. Use assertive language: Phrases like "is superior to" or "is more effective than" are preferred.
    4. For every stance, it is the debater's responsibility to find the evidence. Hence, you just provide the opinions without any supporting evidence or reason.
       For instance, if the topic is "Which anminal is stronger, Lion or Tiger?", you are supposed to output "POSITIVE_STANCE: Lion is stronger than Tiger. NEGATIVE_STANCE: Tiger is stronger than Lion."
    """),
           ("human", f"Topic: {topic}"),
        ])
        chain = debate_prompt | llm
        response = chain.invoke({"topic": topic})
        content = response.content
        positive_stance = content.split("POSITIVE_STANCE:")[1].split("NEGATIVE_STANCE:")[0].strip()
        negative_stance = content.split("NEGATIVE_STANCE:")[1].strip()

        if not positive_stance or not negative_stance:
            raise ValueError("Failed to extract stances from the debate architect response.")
        file_name = "combat_log.txt"
        file_path = os.path.join(folder, file_name)
        append_content = f"Topic: {topic}\nPositive Stance: {positive_stance}\nNegative Stance: {negative_stance}\n"
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(append_content + "\n")
            file.write("-" * 40 + "\n")
        return {
            "topic": topic,
            "positive_stance": positive_stance,
            "negative_stance": negative_stance,
        }
    return debate_architect_node