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

## Acknowledgements

This project is built upon the foundational architecture of the **TradingAgents** framework. We highly appreciate the original authors for their contribution to the Multi-Agent LLM community.

If you find this work or the underlying framework helpful, please reference:

> **TradingAgents: Multi-Agents LLM Financial Trading Framework** > *Yijia Xiao, Edward Sun, Di Luo, and Wei Wang (2025).* > [arXiv:2412.20138](https://arxiv.org/abs/2412.20138) | [Original Repository](https://github.com/YijiaXiao/TradingAgents)

---
