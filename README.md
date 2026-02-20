⚔️ CombatAgent: Multi-Agent Debate System
**CombatAgent** is a beginner-friendly project where two LLMs-based Agents debate with each other on a specified topic.

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone [https://github.com/Chenz418/CombatAgent.git](https://github.com/Chenz418/CombatAgent.git)
cd CombatAgent
```

### 2. Environment Setup
```bash
conda create -n combatagent python=3.13
conda activate combatagent
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Configuration
Multiple LLM providers are supported. Set the API key for your chosen provider:
```bash
export OPENAI_API_KEY=...          # OpenAI (GPT)
export GOOGLE_API_KEY=...          # Google (Gemini)
export ANTHROPIC_API_KEY=...       # Anthropic (Claude)
export XAI_API_KEY=...             # xAI (Grok)
```
