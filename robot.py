'''
Dveloped by Iman Rahgozar for Quandri.
'''

from RPA.Browser.Selenium import Selenium
from RPA.Dialogs import Dialogs
import pandas as pd
from bs4 import BeautifulSoup
import re

br = Selenium()
dlg = Dialogs()



class Robot:
    '''
    Robot consists of say_hello(), say_goodbye(), open_webpage() and summary_report() methods. 
    '''

    def __init__(self, name):
        self.name = name



    def say_hello(self, scientists_list):   #scientists_list: list
        '''
        say_hello() takes as input the name of scientists. It opens up a window, introduces itself, 
        informs the user of what it can do and how the user should work with it. 
        It then lets the user to add new names to the list if they want to. It then updates the list of names and returns the updated list. 
        '''
        #First page text
        dlg.add_heading('Welcome to ' + self.name + '!')
        dlg.add_text('Hi, I am Quandrinaut, I can help you find some basic information about your favorite scientists.')
        dlg.add_text('I know, nerdy, right? But believe me, I can come in handy!')
        dlg.add_text('If you are interested to learn more about how I work, please click on Next button to go to the next page')
        
        #Buton to go to the next page
        dlg.add_dialog_next_page_button('Next')
        
        #Second page text and the text input
        dlg.add_heading('What I do')
        dlg.add_text('I need the first name and last name of the scientists first. Then, I will open wikipedia pages related to those names.'\
                     ' Additionally, I will provide a summary of the information related to that scientist (if there is any in the wikipedia'\
                     ' page) and display it to you.')
        dlg.add_text('The current list of scientists is:' + ''.join([item+', ' for item in scientists_list[0:-1]])+scientists_list[-1])    
        dlg.add_text('You can add the name of your favorite scientists to this list and separate the names with a comma (,),'\
                     ' if I could find any information on Wikipedia based on the name you provided'\
                     ' I will display it. When you are done click on Submit!')
        dlg.add_text_input(name='add',label='Enter the names here:',placeholder = 'e.g. Robert Koch, René Descartes')
         
        
        '''
        Starts opening and running the window, if the user inputs a text, it retrieves the names from the text and 
        updates the list of scientists. If the user does not input any text, it will raise an error in which case,
        nothing will be added to the list. 
        '''
        try:
            #Openning and runnning the welcome window
            input_text = dlg.run_dialog(title= 'Welcome Page')
            
            list_addition = [item.strip() for item in input_text['add'].split(',')]
            scientists_list.extend(list_addition)
            
        except: 
            pass
        
        return scientists_list                #scientists_list: list
        




    def open_webpage(self, webpages):         #webpages: list
        '''
        open_webpage() takes as input the list of webpage urls to open. It opens a window for each url using the available 
        browser of the user. It also records all of the html data of each page in page_sources and returns the list. 
        '''        
        page_sources = []
       
        #iterating through all of the urls
        for webpage in webpages: 
            br.open_available_browser(webpage)
            page_sources.append(br.get_source())

        return page_sources                   #page_sources  : list

        

        
    def summary_report(self, scientists_list,page_sources):          #scientists_list: list, page_sources  : list
        '''
        summary_report() takes as input the list of scientists names and the corresponding html data of its wikipedia page.
        It then parses the webpage and extracts the birth date, death date, image of the person and the first paragraph of
        its wikipedia page and calculates their age at the time of death. 
        Finally it opens a window for each scientist and shows the extracted information to the user. It also returns the number of windows 
        that it opened. 
        '''          
        no_of_open_windows = 0
        
        for i, name in enumerate(scientists_list) :
            
            '''
            During the parsing of each webpage, if a required info is not present, an error is raised which is handled by the following section. 
            If an error is raised, no page will be opened to show the summary as a result the number of open windows also does not get updated.
            '''
            try:
                
                #Webscraping
                soup = BeautifulSoup(page_sources[i],'html.parser')
                table = soup.find('table',"infobox biography vcard")
                image = table.find('img')
                link = 'https:'+image['src']
                bday_row = table.find('span','bday')
                death_row = bday_row.find_next('td')
                birth_date = bday_row.text
                death_date = re.search(r'\d\d\d\d-\d\d-\d\d', death_row.text).group()
                age = int(death_date[0:4]) - int(birth_date[0:4])
                paragraph = soup.find_all('p',class_ = False)[0]
                
                #Creating the window and dsplaying the extracted information 
                dlg.add_heading(name)
                dlg.add_image(link)
                dlg.add_text('Birth : ' + birth_date)
                dlg.add_text('Death : ' + death_date)
                dlg.add_text('Age at the time of Death: ' + str(age) + ' years old')
                dlg.add_text('')
                dlg.add_text('Summary:')
                dlg.add_text(paragraph.text)
                dlg.show_dialog(title = name,height=1000,width=1000)
                
                
                no_of_open_windows +=1
                
            except:
                pass
            
        return no_of_open_windows
    
    
    
     
    
    def say_goodbye(self,no_of_windows):
        '''
        say_goodbye() takes as input the number of open summary windows. 
        It waits until all of the summary windows are closed. Then it opens up a window which thanks the user and says goodbye. 
        '''        
        closed_window_counter = 0
        
        
        while closed_window_counter < no_of_windows :
            '''
            dlg.wait_all_dialogs() waits until all of the open windows are closed.
            If the user closes the window in any way other than pressing the 'close' button, dlg.wait_all_dialogs() raises an error
            which will be handled by the following section. If the user clicks on the 'close' button, no error is raised.
            '''
            try: 
                dlg.wait_all_dialogs()
                closed_window_counter += 1
            except: 
                closed_window_counter += 1
        
        #Goodbye window text
        dlg.add_text('Thank you for using me. I hope I was useful, see you next time!')
        
        #Openning and runnning the window
        dlg.show_dialog(title = 'Goodbye')   
    
    
    
