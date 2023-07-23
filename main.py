from bs4 import BeautifulSoup
import requests
import tkinter as tk
from keybert import KeyBERT
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import tkinter.font as tkFont
from tkinter import messagebox

class App:
    def __init__(self, root):
        root.title("Company Review App")
        global scrapedreviews
        global sentimentreviews
        scrapedreviews = []
        sentimentreviews = []
        sentimentreviews = []
        width=1077
        height=714
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.get_data = tk.Button(root)
        self.get_data["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.get_data["font"] = ft
        self.get_data["fg"] = "#000000"
        self.get_data["justify"] = "center"
        self.get_data["text"] = "Get Data"
        self.get_data.place(x=60, y=620, width=280, height=50)
        self.get_data["command"] = self.get_data_command

        self.company_name_entry = tk.Entry(root)
        self.company_name_entry["bg"] = "#ffffff"
        self.company_name_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.company_name_entry["font"] = ft
        self.company_name_entry["fg"] = "#333333"
        self.company_name_entry["justify"] = "center"
        self.company_name_entry["text"] = "Company Name"
        self.company_name_entry.place(x=60, y=30, width=180, height=34)

        self.search_company = tk.Button(root)
        self.search_company["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.search_company["font"] = ft
        self.search_company["fg"] = "#000000"
        self.search_company["justify"] = "center"
        self.search_company["text"] = "Search"
        self.search_company["relief"] = "ridge"
        self.search_company.place(x=260, y=30, width=80, height=34)
        self.search_company["command"] = self.search_company_command

        self.list_company = tk.Listbox(root)
        self.list_company["bg"] = "#ffffff"
        self.list_company["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=10)
        self.list_company["font"] = ft
        self.list_company["fg"] = "#333333"
        self.list_company["justify"] = "center"
        self.list_company.place(x=60, y=90, width=280, height=504)

        self.reviews_box = tk.Text(root)
        self.reviews_box.configure(state='normal')
        self.reviews_box.configure(wrap='word')
        self.reviews_box.tag_configure('left', justify='left')
        self.reviews_box.place(x=425, y=90, width=280, height=504)

        self.keywords_box = tk.Text(root, width=50, height=10)
        self.keywords_box.place(x=750, y=90, width=280, height=504)

        self.sentiment_box = tk.Text(root)
        self.sentiment_box.configure(state='normal')
        self.sentiment_box.configure(wrap='word')
        self.sentiment_box.tag_configure('left', justify='left')
        self.sentiment_box.place(x=425, y=30, width=280, height=45)

    def get_data_command(self):
        scrapedreviews = []
        sentimentreviews = []
        keywords = []
        self.keywords_box.delete(1.0, tk.END)
        self.reviews_box.delete(1.0, tk.END)
        self.sentiment_box.delete(1.0, tk.END)
        def sentiment_scores(sentence):
            sid_obj = SentimentIntensityAnalyzer()
            sentiment_dict = sid_obj.polarity_scores(sentence)
            if sentiment_dict['compound'] >= 0.05 :
                sentimentreviews.append(1)
            elif sentiment_dict['compound'] <= - 0.05 :
                sentimentreviews.append(-1)
            else :
                sentimentreviews.append(0)

        if len(self.list_company.curselection())==0:
            messagebox.showerror("Error", "Please search a company and choose the website from the list!")

        for i in self.list_company.curselection():
            companyname = self.list_company.get(i)

        for i in range (2):
            if i == 0:
                url = "https://uk.trustpilot.com/review/" +  companyname
            else:
                url = "https://uk.trustpilot.com/review/" + companyname + "?page=" + str(i)
            r = requests.get(url)
            soup = BeautifulSoup(r.content, features="html.parser")
            reviews = soup.find_all("div", class_="styles_reviewcardinner__ewdq2")
            words = soup.find_all("p", class_="typography_color-black__5LYEn")
            for i in range(2, len(words) - 2):
                scrapedreviews.append(words[i].get_text())
            for i in range(len(scrapedreviews)):
                scrapedreviews[i] = scrapedreviews[i].encode('unicode-escape').decode('utf-8')
            for review in scrapedreviews:
                self.reviews_box.insert(tk.END, review + '\n' + '\n',  'left')
            combined_reviews = ' '.join(scrapedreviews)
            model = KeyBERT()
            keywords = model.extract_keywords(combined_reviews, top_n=10)
            for keyword in keywords:
                self.keywords_box.insert(tk.END, str(keyword[0]) + "\n",  'left')
        for i in range(len(scrapedreviews)):
            sentiment_scores(scrapedreviews[i])
        if sentimentreviews.count(1) > sentimentreviews.count(-1):
            self.sentiment_box.insert(tk.END,"The reviews of this company were " + str(round(sentimentreviews.count(1)/len(scrapedreviews) * 100, 2)) + "% positive")
        elif sentimentreviews.count(1) < sentimentreviews.count(-1):
            self.sentiment_box.insert(tk.END,"The reviews of this company were " + str(round(sentimentreviews.count(-1)/len(scrapedreviews) * 100, 2)) + "% negative")

    def search_company_command(self):
        self.list_company.delete(0, tk.END)
        for i in range (2):
            if i == 0:
                search_url = "https://uk.trustpilot.com/search?query=" + self.company_name_entry.get()
            else:
                search_url = "https://uk.trustpilot.com/search?" + "page=" + str(i) + "&query=" + self.company_name_entry.get()
            search = requests.get(search_url)
            searchcompanies = BeautifulSoup(search.content, features="html.parser")
            companies = searchcompanies.find_all("span", class_="styles_websiteUrl__bs958")
            for i in range(len(companies) -1 ):
                self.list_company.insert(tk.END,str(companies[i].text))

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()




