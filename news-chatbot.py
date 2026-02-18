from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
import requests
from bs4 import BeautifulSoup

# Define Large Language Model
llm = ChatOllama(model="qwen2.5-coder")

# Define Chat bot model
class NewsBriefingBot:
    def __init__(self):
        # Define store for chat history
        self.store = {}
        self.news_cache = None
        # define prompt template for news briefing
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a helpful assistant that provides news briefings.
             
             Today's news:
             {news}

             Please answer the user's question based on the above news.
             And if the content of the news is not in the above news, please say 
             "Sorry, the content is not available in today's news."
             """),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}"),
        ])
        # Define the chain of prompt and llm, and use StrOutputParser to parse the output as string
        self.chain = self.prompt | llm | StrOutputParser()

        # Define the chatbot with message history
        self.chatbot = RunnableWithMessageHistory(
            self.chain,
            self._get_history,
            input_message_key="input",
            output_message_key="output",
        )

        def _get_history(self, session_id: str):
            """
            returns the conversation history of the user based on the session ID.            
            Args:
            session_id (str): A unique key to identify the user.
            Returns:
            ChatMessageHistory: The message history object for the session.
            """
            if session_id not in self.store:
                # If the session ID does not exist in the store, create a new InMemoryChatMessageHistory object and store it in the store with the session ID as the key.
                self.store[session_id] = InMemoryChatMessageHistory()
            return self.store[session_id]
        
