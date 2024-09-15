import requests
from tkinter import *
from tkinter import messagebox

class NewsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("News Generator")
        self.root.geometry("600x400")

        self.api_key = "your_api_key_here"  # Replace with your own NewsAPI key

        # Create a label for the title
        Label(self.root, text="News Generator", font=("Helvetica", 16)).pack(pady=10)

        # Create a button to fetch news
        Button(self.root, text="Get Top News", command=self.fetch_news, font=("Arial", 12), bg="#32de97").pack(pady=10)

        # Create a text box to display news
        self.news_box = Text(self.root, bd=1, bg="white", width=65, height=15, font=("Arial", 12))
        self.news_box.pack(pady=10)

    def fetch_news(self):
        """Fetch top news headlines from NewsAPI."""
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={self.ab3cf51728974c2a871576a9c99cd252}"
        response = requests.get(url)

        if response.status_code == 200:
            news_data = response.json()
            articles = news_data["articles"]
            
            self.news_box.delete("1.0", END)  # Clear the news box before displaying new headlines
            
            if articles:
                for i, article in enumerate(articles[:5], 1):  # Limit to top 5 articles
                    title = article["title"]
                    description = article.get("description", "No description available.")
                    news = f"{i}. {title}\nDescription: {description}\n\n"
                    self.news_box.insert(END, news)
            else:
                self.news_box.insert(END, "No news articles found.")
        else:
            messagebox.showerror("Error", "Failed to retrieve news.")

# Create the main window
root = Tk()
news_app = NewsApp(root)
root.mainloop()
