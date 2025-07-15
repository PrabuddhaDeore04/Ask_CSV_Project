from langchain_experimental.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st


def main():
    load_dotenv()

    # Load the OpenAI API key from the environment variable
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")

    st.set_page_config(page_title="Ask your CSV")
    st.header("Talk with your CSV 📈")

    csv_file = st.file_uploader("Upload a CSV file", type="csv")
    if csv_file is not None:
        user_que = st. text_input("Ask any question about your CSV: ")
        
        llm = OpenAI (temperature=0)
        agent = create_csv_agent(llm, csv_file, verbose=True, allow_dangerous_code=True)

        if user_que is not None and user_que != "":
            response = agent.run(user_que)
            
            st.write(response)



if __name__ == "__main__":
    main()  