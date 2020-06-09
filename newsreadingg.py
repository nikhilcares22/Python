import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak= Dispatch("SAPI.SpVoice")
    speak.Speak(str)
if __name__ == '__main__':
    speak("News for today")
    url="http://newsapi.org/v2/top-headlines?country=in&apiKey=448bbeb6e5404f0985aa6b3309efc546"
    news = requests.get(url).text
    news_dict = json.loads(news)
    print(news_dict["articles"])
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        print(article['title'])

        speak("moving on to the next news.... listen carefully")
