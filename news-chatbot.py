import requests

from bs4 import BeautifulSoup
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_ollama import ChatOllama

# Define Large Language Model
llm = ChatOllama(model="qwen2.5-coder")


# Define Chat bot model
class NewsBriefingBot:
    def __init__(self):
        # Define store for chat history
        self.store = {}
        self.news_cache = None
        # define prompt template for news briefing
        self.prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """You are a helpful assistant that provides news briefings.
                    
                    if someone asks you a questions in their language,
                    you have to explain in the language who asks in their langauge 
                    based on the news provided below.
             
             Today's news:
             {news}

             Please answer the user's question based on the above news.
             And if the content of the news is not in the above news, please say 
             "Sorry, the content is not available in today's news."
             """,
                ),
                MessagesPlaceholder(variable_name="history"),
                ("human", "{input}"),
            ]
        )
        # Define the chain of prompt and llm, and use StrOutputParser to parse the output as string
        self.chain = self.prompt | llm | StrOutputParser()

        # Define the chatbot with message history
        self.chatbot = RunnableWithMessageHistory(
            self.chain,
            self._get_history,
            input_message_key="input",
            history_messages_key="history",
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

    def _fetch_news(self):
        """
        Fetches the latest news from hacker news and returns it as a string.
        Returns:
        str: The latest news in string format.
        """
        try:
            response = requests.get("https://news.ycombinator.com/", timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")

            news_items = []
            for span in soup.find_all("span", class_="titleline")[
                :10
            ]:  # Get the top 10 news items
                link = span.find("a")
                if link:
                    news_items.append(f"- {link.text}")

            self.news_cache = "\n".join(news_items)
            return self.news_cache
        except Exception as e:
            print(f"Error fetching news: {e}")
            return "Sorry, I couldn't fetch the news at the moment."

    def chat(self, message: str, session_id: str = "default") -> str:
        # check cache of news
        if self.news_cache is None:
            self._fetch_news()

        # Pass the news and the message to the chatbot, and return the response.
        config = {"configurable": {"session_id": session_id}}
        return self.chatbot.invoke(
            {"input": message, "news": self.news_cache}, config=config
        )

    def refresh_news(self):
        # Refresh the news cache
        self._fetch_news()
        return "News refreshed successfully!"


# using the chatbot
bot = NewsBriefingBot()

print("=== news briefing chatbot ===")
print("Type '/refresh' to refresh the news, or type '/exit' to exit.\n")

while True:
    user_input = input("You: ").strip()

    if user_input == "/exit":
        print("Exiting the chatbot. Goodbye!")
        break
    elif user_input == "/refresh":
        print(f"Bot: {bot.refresh_news()}\n")
    else:
        response = bot.chat(user_input)
        print(f"Bot: {response}\n")
