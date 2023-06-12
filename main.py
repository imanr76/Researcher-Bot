'''
Dveloped by Iman Rahgozar for Quandri.
'''

from robotics import Robot

SCIENTISTS_DEFAULT = ["Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin"]  #Default list of scientists

robot = Robot("Quandrinaut")


def introduce_yourself(SCIENTISTS__DEFAULT):                #SCIENTISTS__Default: list
    '''
    introduce_yourself() calls say_hello() from robot. It takes the list of default scientists as input and passes it to say_helo in the robots,
    introduces the robot and how it works to the user, adds possible new scientists to the list and returns the updated list of scientists. 
    '''    
    SCIENTISTS = robot.say_hello(SCIENTISTS_DEFAULT)
    return SCIENTISTS                                       #SCIENTISTS: list



def open_webs(SCIENTISTS):              #SCIENTISTS: list
    '''
    open_webs() first creates a list of wikipedia page urls based on the name of te scientists in the list passed to it.
    It then opens a browser window for each scientist and opens the respective url.
    Finally, it reads the html data of each webpage and returns them as a list. 
    '''
    webpages = ['https://en.wikipedia.org/wiki/'+name.replace(' ','_') for name in SCIENTISTS]
    page_sources = robot.open_webpage(webpages)
    return page_sources                 #page_sources: list



def create_summaries(SCIENTISTS,page_sources):                        #SCIENTISTS: list, page_sources: list
    '''
    create_summaries() takes as input the list of scientists and the html data related to each one. It then passes these lists to the 
    summary_report() in the robot which extracts the information from each webpage, creates a window and displays the info related to each scientist. 
    It also returns the number of created windows. 
    '''    
    no_of_windows = robot.summary_report(SCIENTISTS,page_sources)
    return no_of_windows                                              #no_of_windows: int



def goodbye(no_of_windows):            #no_of_windows: int
    '''
    goodbye() takes as input the number of opened windows. It then passes the number of opened windows to say_goodbye() in robot. 
    say_goodbye() waits for the user to close all of the opened windows before it shows the goodbye message. 
    '''    
    robot.say_goodbye(no_of_windows)
    


def main(SCIENTISTS_DEFAULT):   
        '''
        1. Creates a window, introduces itself, gives the user information about how it works and what they should do.
        2. Gives the user the ability to add new names to the list.
        3. Once the welcome window is submitted or closed, opens webpages for all of the names in the list and opens windows 
        with some info about each person (if any info exists).
        4. Once all of the summary windows are closed, opens a goodbaye window.
        '''   
        SCIENTISTS = introduce_yourself(SCIENTISTS_DEFAULT)
        page_sources = open_webs(SCIENTISTS)
        no_of_windows = create_summaries(SCIENTISTS,page_sources)
        goodbye(no_of_windows)



if __name__ == "__main__":
    main(SCIENTISTS_DEFAULT)
    