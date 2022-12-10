import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def scrape_chat_conversation(html_code):
    soup = BeautifulSoup(html_code, "html.parser")
    conversation = soup.find_all("div", class_="chat-message")
    for chat in conversation:
        sender = chat.find("span", class_="chat-message-username").text
        if sender == "Person 1":
            message = chat.find("span", class_="person1-message").text
            print("<div class='person1'>" + sender + ": " + message + "</div>")
        else:
            message = chat.find("span", class_="person2-message").text
            print("<div class='person2'>" + sender + ": " + message + "</div>")



website = get_html("https://chat.openai.com/chat")
scrape_chat_conversation(website)