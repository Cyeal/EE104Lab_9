Glenn Francisco
Due: 5-17-2023
EE104
Professor Christopher Pham
============================================================================================================================================================
Disclaimer: 
This file contains instructions and descriptions for the following programs. It includes steps for successfully operating each program without encountering errors, as well as video demonstrations for those who prefer visual aids. Please note that users who wish to run the programs will need to install previously uploaded libraries to Python to access a wider range of commands and programs.
============================================================================================================================================================
Youtube Links:
https://youtu.be/Bx8t9Vb5TLY

Github Links:


============================================================================================================================================================
References through this project:
https://www.edureka.co/blog/interview-questions/python-interview-questions/
https://intellipaat.com/blog/interview-question/python-interview-questions/?US
https://www.simplilearn.com/tutorials/python-tutorial/python-interview-questions
https://mindmajix.com/python-interview-questions
https://interviewing.io/mocks/apple-python-count-islands
https://www.interviewbit.com/python-interview-questions/
https://www.datacamp.com/blog/top-python-interview-questions-and-answers
https://codesubmit.io/interview/python-interview-questions
https://www.interviewkickstart.com/interview-questions/advanced-python-interview-questions
https://data.sccgov.org/browse?category=COVID-19
http://www.creditriskanalytics.net/datasets-private2.html

============================================================================================================================================================
The following modules should already be installed, but still useful to recommend:
-numpy
-scipy
-math
-matplotlib
-pint
-pandas
-pgzrun
-pygame
-pgzero
-sympy
-random
-heartpy
-tensorflow
-keras
-CUDA
-UPDATE NUMPY
============================================================================================================================================================
Download the necessary libraries, users should open their Anaconda Powershell and follow the steps outlined below:
1) Open Anaconda Powershell Prompt
2) Type "pip install (missing module name)"
3) Allow the Powershell to install the module
4) Repeat the same steps for other modules
5) Once the module finishes downloading, the program should be ready to go!
6) If the program encounters any issues, try updating Spyder or restarting the IDE.
============================================================================================================================================================
Description and Brief Instructions of the following Programs:
============================================================================================================================================================
Data Science - Risk Factor

This Python script analyzes loan data to identify risk factors based on default rates. It performs several steps, including reading loan data from a CSV file, analyzing the data, calculating the default rate for each loan type, determining the risk level for each loan type based on the default rate, adding a new column to the loan data with the risk level for each loan type, applying risk level recommendations based on the analysis results, writing the analyzed data to a new CSV file with additional columns, and printing a summary of the analysis results and risk level recommendations.

Instructions: 
1. Reads loan data from a CSV file.
2. Analyzes the loan data and calculates the default rate for each loan type.
3. Determines the risk level for each loan type based on the default rate.
4. Adds a new column to the loan data with the risk level for each loan type.
5. Applies risk level recommendations based on the analysis results.
6. Writes the analyzed data to a new CSV file with additional columns.
7. Prints a summary of the analysis results and risk level recommendations.
============================================================================================================================================================
Data Science - Trend Prediction

At times, it is necessary to make predictions based on historical information available. If the prediction outcome does not match the actual outcome, you may need to help government or company executives implement measures to increase or decrease certain outcomes by conducting what-if analyses. One possible application of this is to enforce social distancing measures to control the spread of Covid-19.

For instance, suppose you have access to six months of data. In this case, you can use data from the first three months to create a curve fit and equation. Then, you can use this equation to predict the outcome for the next three months and compare it to the actual data. This process can help you determine if the curve fit is accurate and can be used to make further predictions.

In your documentation, you can discuss the process of creating a curve fit and using it to predict future outcomes. Additionally, you can describe how to compare the projected curve to the actual data and what steps to take if there is a discrepancy between the two. By following these steps, you can make informed decisions and take appropriate actions to help achieve your goals.

Instrcutions:
1. Open a web browser and go to https://data.sccgov.org/browse?category=COVID-19
2. Scroll through the datasets and select the one that covers the desired timeframe. For this example, let's use the dataset "COVID-19 Cases and Deaths by  3. County and City" for Santa Clara County.
4. Click on the dataset to view the details and download options.
5. Download the dataset in CSV format by clicking on the "Export" button and selecting "CSV".
6. Open a spreadsheet software like Microsoft Excel or Google Sheets.
7. Open the downloaded CSV file in the spreadsheet software.
8. Create a new sheet and copy and paste the data from the downloaded CSV file into the new sheet.
9. Sort the data by date column, so that the data is ordered chronologically.
10. Delete any unnecessary columns that are not relevant to the analysis, such as the columns for age group or gender.
11. Create a new column for the cumulative cases or deaths for the entire county by summing up the values for each city or region.
12. Create a line chart with the date on the x-axis and the cumulative cases or deaths on the y-axis. The chart should show the data from January to June.
13. Use a curve fitting tool to fit a curve to the data for January to June. This will generate an equation that describes the trend in the data.
14. Use the equation to project the trend for the rest of the year, from July to December.
15. Create a second chart that compares the projected curve with the actual data for July to December.
============================================================================================================================================================
Game Development – Dance Challenge 
============================================================================================================================================================
This dance game is an interactive game where players are challenged to follow a sequence of dance moves. The game tests players' ability to match the displayed dance moves using arrow keys or W, A, S, D keys. It incorporates music, visual elements, and scoring to create an engaging experience. To run the game, open a terminal or command prompt and navigate to the directory containing the game files. Then, execute the command: python dance_game.py. The game includes instructions for gameplay, controls, scoring, and customization.
Note:
    This game uses Pygame Zero, a simple game framework for Python, which provides an abstraction layer for game development.
    The game is optimized for a screen resolution of 800x600. Adjustments may be required for different resolutions.

To Run the Game:
        Open a terminal or command prompt and navigate to the directory containing the game files.
        Execute the command: python dance_game.py.

Game Instructions:
    Gameplay:
        The game is designed for two players, taking turns to follow the dance moves.
        The dance moves are displayed as arrows on the screen.
        Each arrow corresponds to a specific key or arrow key (up, right, down, left).
        When the dance moves appear, players must press the corresponding keys before the time runs out.

    Controls:
        Player 1: Use arrow keys (up, right, down, left) to match the dance moves.
        Player 2: Use W, D, S, A keys to match the dance moves.

    Scoring:
        Each correct dance move earns the player a point.
        The game displays the score for each player.
        If a player fails to match a dance move correctly, the game ends and the final scores are shown.

    Restarting the Game:
        To restart the game, close the game window and run the game again.

Customization:
    Dance Length:
        By default, the dance sequence length is set to 4 moves. You can modify this by changing the dance_length variable in the code.

    Music:
        The game plays an 8-bit music track by default. You can replace the music file with your own by replacing the "song" file in the game directory.

    Dance Moves and Visuals:
        The game uses predefined dance move images and visuals. If you want to customize or add new dance moves, modify the image files in the game directory.


============================================================================================================================================================
Job interview Q&A 
============================================================================================================================================================
This list of interview questions covers various aspects of Python programming, including basic programming concepts, machine learning, OPENAI, game development, and fundamental Python functions. It assesses the candidate's knowledge and proficiency in these areas, providing a comprehensive evaluation of their programming skills, problem-solving abilities, and familiarity with important Python topics.
============================================================================================================================================================