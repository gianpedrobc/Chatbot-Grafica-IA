# 🤖 Chatbot Gráfica IA

Um chatbot inteligente para atendimento de uma gráfica, desenvolvido com Streamlit e Google Gemini API.

## ✨ Funcionalidades

- 🎯 Classificação automática de perguntas (camisa, caneca, banner, geral)
- 💬 Respostas inteligentes baseadas em contexto
- ⚡ Interface web simples e responsiva
- 🔒 Segurança com variáveis de ambiente

## 🚀 Início Rápido

### Pré-requisitos
- Python 3.8+
- pip

### Instalação

1. **Clone ou baixe o projeto**
```bash
cd Chatbot_grafica_ia
```

2. **Crie ambiente virtual**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Configure a chave de API**

Crie um arquivo `.env` na raiz do projeto:
```bash
GOOGLE_API_KEY=sua_chave_aqui
```

Para obter a chave, visite: [Google AI Studio](https://aistudio.google.com/app/apikey)

5. **Execute a aplicação**
```bash
streamlit run app.py
```

A aplicação abrirá em `http://localhost:8501`

## 📁 Estrutura

```
Chatbot_grafica_ia/
├── app.py                 # Aplicação principal
├── requirements.txt       # Dependências
├── README.md             # Este arquivo
├── .env                  # Variáveis de ambiente (não rastreado)
└── dados/                # Base de conhecimento
    ├── geral.txt
    ├── camisa.txt
    ├── caneca.txt
    └── banner.txt
```

## 🔄 Como Funciona

1. Usuário digita uma pergunta
2. Sistema classifica a pergunta em uma categoria (camisa/caneca/banner/geral)
3. Carrega o contexto da categoria correspondente
4. Envia pergunta + contexto para o Gemini API
5. Exibe resposta inteligente na interface

## 📦 Dependências

- **streamlit** - Interface web
- **google-generativeai** - API Gemini
- **python-dotenv** - Variáveis de ambiente

## 🔐 Segurança

- Chave de API armazenada em `.env` (não rastreado no Git)
- Acesso apenas via variáveis de ambiente
- Respostas baseadas em contexto controlado

## 🛠️ Desenvolvimento

### Adicionar Nova Categoria

1. Crie um arquivo em `dados/nova_categoria.txt`
2. Atualize o mapeamento em `escolher_arquivo_por_categoria()`
3. Adicione a categoria ao prompt de classificação

### Testar Localmente

```bash
streamlit run app.py
```

Acesse `http://localhost:8501` e teste diferentes perguntas.

## 💡 Exemplos de Uso

```
Input:  "Qual é o horário?"
Output: "Segunda a sexta: 08h às 18h, Sábado: 08h às 12h"

Input:  "Quanto custa uma camisa?"
Output: "A partir de R$ 29,90 por unidade (mínimo 10 peças)..."

Input:  "Que tipos de impressão vocês fazem?"
Output: "Silk screen, sublimação, transfer digital e DTF..."
```

## 📊 Stack

| Componente | Tecnologia |
|-----------|-----------|
| Framework | Streamlit |
| IA | Google Gemini 3 Flash |
| Linguagem | Python |
| Ambiente | python-dotenv |

## 🚧 Melhorias Futuras

- [ ] Histórico de conversa
- [ ] Banco de dados integrado
- [ ] Autenticação de usuários
- [ ] Analytics de perguntas
- [ ] Suporte a múltiplas linguagens
- [ ] Integração com WhatsApp

## 📝 Licença

Este projeto é de código aberto. Sinta-se livre para usar e modificar.

## 🤝 Contribuições

Sugestões e melhorias são bem-vindas! Abra uma issue ou pull request.

## 📞 Contato

Para dúvidas sobre a implementação, consulte a documentação oficial:
- [Streamlit Docs](https://docs.streamlit.io)
- [Google Generative AI](https://ai.google.dev)

---

**Desenvolvido com ❤️ usando Streamlit e Google Gemini**
