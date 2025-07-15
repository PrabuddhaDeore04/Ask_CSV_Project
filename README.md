# Ask Your CSV 📊

This Streamlit app allows users to upload a CSV file and ask questions about the data using natural language. It uses OpenAI's language models via LangChain's `create_csv_agent` to interact with the data intelligently.

## 🧠 Tech Stack

- **Streamlit**: Web interface for uploading CSVs and asking questions
- **LangChain**: Handles the LLM interaction and CSV parsing
- **OpenAI**: Provides the language model (GPT)
- **dotenv**: For environment variable management (API key)

## ⚙️ How It Works

1. **Upload a CSV file** through the Streamlit UI.
2. **Enter a natural language question** (e.g., "What is the average price?" or "Show the total revenue for 2023").
3. The app uses `langchain_experimental.agents.create_csv_agent` to:
   - Parse the CSV
   - Create a prompt
   - Pass it to OpenAI's LLM (GPT)
4. The response is **generated using the LLM** and shown on the screen.

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ask-your-csv.git
cd ask-your-csv
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Your OpenAI API Key

Create a `.env` file in the root folder:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. Run the App

```bash
streamlit run main.py
```

## 📁 File Structure

```
ask-your-csv/
├── main.py               # Main Streamlit app
├── requirements.txt     # Dependencies
├── .env                 # Your OpenAI API key
└── README.md            # This file
```

## 💡 Example Questions

- What is the average salary?
- How many rows are in the file?
- What are the mean of top 5 products by revenue?
- what is the stats of pikachu?


