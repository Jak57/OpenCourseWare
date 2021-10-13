# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory
class NewsStory(object):
    
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
        
    def get_guid(self):
        return self.guid
    
    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description
    
    def get_link(self):
        return self.link
    
    def get_pubdate(self):
        return self.pubdate

#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger

class PhraseTrigger(Trigger):
    
    def __init__(self, phrase):
        self.phrase = phrase
        
    def get_phrase(self):
        return self.phrase
        
    def is_phrase_in(self, text):
        
        phrase = self.get_phrase()
        phrase = phrase.lower()
        phrase_list = phrase.split()
        
        text = text.lower()
        punctuations = string.punctuation
        text_without_punc = ""
        
        for char in text:
            if char in punctuations:
                text_without_punc += " "
            else:
                text_without_punc += char
        
        word_list = text_without_punc.split()
        # clean_text = " ".join(word_list)
        
        # return phrase in clean_text
        i = 0
        found = False
        
        while i < len(word_list):
            j = 0
            k = i
            match = 0
            
            while(j < len(phrase_list) and k < len(word_list)):
                if word_list[k] == phrase_list[j]:
                    match += 1
                    j += 1
                    k += 1
                else:
                    break
            
            if match == len(phrase_list):
                # print("match:", match)
                found = True
                break
            i += 1
        
        return found

# Problem 3
# TODO: TitleTrigger

class TitleTrigger(PhraseTrigger):
    
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)
        
    # def get_phrase(self):
    #     return self.phrase
    
    def evaluate(self, story):
        # print(story)
        return self.is_phrase_in(story.get_title())

# Problem 4
# TODO: DescriptionTrigger

class DescriptionTrigger(PhraseTrigger):
    
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)
        
    # def get_phrase(self):
    #     return self.phrase
    
    def evaluate(self, story):
        # print(story)
        return self.is_phrase_in(story.get_description())

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.

class TimeTrigger(Trigger):
    def __init__(self, datetime_string):
        format = "%d %b %Y %H:%M:%S"
        
        now = datetime.strptime(datetime_string, format)
        
        now = now.replace(tzinfo=pytz.timezone("EST"))
        
        self.triggered_time = now

# Problem 6
# TODO: BeforeTrigger and AfterTrigger

class BeforeTrigger(TimeTrigger):
    def __init__(self, datetime_string):
        TimeTrigger.__init__(self, datetime_string)
        
    def get_triggered_time(self):
        return self.triggered_time
    
    def evaluate(self, story):
        # pubdate = story.get_pubdate()
        now = story.get_pubdate()
        now = now.replace(tzinfo=pytz.timezone("EST"))
        
        pubdate = now
        triggered_time = self.get_triggered_time()
        
        return pubdate < triggered_time


class AfterTrigger(TimeTrigger):
    def __init__(self, datetime_string):
        TimeTrigger.__init__(self, datetime_string)
        
    def get_triggered_time(self):
        return self.triggered_time
    
    def evaluate(self, story):
        # pubdate = story.get_pubdate()
        now = story.get_pubdate()
        now = now.replace(tzinfo=pytz.timezone("EST"))
        
        pubdate = now
        
        triggered_time = self.get_triggered_time()
        
        return pubdate > triggered_time
        
    


# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger

class NotTrigger(Trigger):
    
    def __init__(self, other_trigger):
        self.other_trigger = other_trigger
        
    def get_other_trigger(self):
        return self.other_trigger
    
    
    
    def evaluate(self, story):
       
        other_trigger = self.get_other_trigger()
        
        return not other_trigger.evaluate(story)
# Problem 8
# TODO: AndTrigger

class AndTrigger(Trigger):
    
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
        
    def get_trigger1(self):
        return self.trigger1
    
    def get_trigger2(self):
        return self.trigger2
    
    def evaluate(self, story):
        trigger1 = self.get_trigger1()
        trigger2 = self.get_trigger2()
        
        return trigger1.evaluate(story) and trigger2.evaluate(story)

# Problem 9
# TODO: OrTrigger

class OrTrigger(Trigger):
    
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
        
    def get_trigger1(self):
        return self.trigger1
    
    def get_trigger2(self):
        return self.trigger2
    
    def evaluate(self, story):
        trigger1 = self.get_trigger1()
        trigger2 = self.get_trigger2()
        
        return trigger1.evaluate(story) or trigger2.evaluate(story)

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    return stories



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers

    print(lines) # for now, print it so you see what it contains!



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        # triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

   

