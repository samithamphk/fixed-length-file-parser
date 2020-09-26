# Fixed Length File Paser
This is a fixed length file parser implementation in python. 

The code do two things. 

    - Generate a fixed length file of a user given size 
    - Parse the file (<2GB)
    
## How to run the code
The code can run two scenarios
### 1. Windows without Docker
        -- Clone the repository to your local system
        -- Go to 'lati-sam' folder
        -- Double click app.bat
        -- Enter the number (n) of rows required to generate the data file
        -- See the my.txt (fixed length file ) and out.csv (parsed file) in the 'data' folder
### 2. *where with Docker 
        -- Clone the repository to your local system
        -- Open a terminal and go to 'lati-sam' folder
        -- Enter './app.sh'
        -- You will be prompted docker terminal.
        -- Enter 'python lati-sam-app.py -n <integer>'
        -- On the console you will see the contents of the specification file and the data file
