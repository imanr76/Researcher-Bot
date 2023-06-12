The 2 main files related to this project: 
1. robotics.py 
2. main.py 

Quandrinaut robot is designed to provide infomration about scientists to the user, it does so by following the next steps: 

1. When the robot is run, it opens up a window, saying hello to the user, introduces itself, and gives 
some information about itself and how it works. 

2. After greetings, it shows the user the default list of scientists. It also has a text input which the user could use to input 
the name of any other scientists that they would like to add to the list (the names should be separated by commas) 
or they could skip this step if they are fine with the current list. 

3. After the user submits the new names or closes the window, the robot uses the updated list, opens up a browser window
(whatever is already installed) and navigates to the wikipedia page of the scientist. 

4. Next, it extract the image, date of birth, date of death, age and the first wikipedia webpage paragraph of the scientists from 
wikipedia. It then opens a window for each scientist and displays the extracted information.

5. the robot then waits until the user closes all of the opened summary windows. Afterwards, it sends a message to the user
to say goodbye.

Note: If the user inputs a name for which a wikipedia page does not exist or if the page does not have the same structure as the 
scientists page, the robot will still navigate to that wikipedia page (which basically tells the user that this 
page does not exist) but no summary page will be displayed. 

Room for improvement and future work: 
1. A more interactive environment could be provided for the user to add, remove, or select more scientists 
(from a long list of available names).

2. More information could be added to the summary window, such as achievements, place of birth and death etc.

3. Giving the user the option of which items or information they want to be extracted. 

4. The representation of the information could be more user friendly and aesthetically pleasant. 