### Quick Start
#### Info
The program is meant for quiet copying of pendrives inserted into windows systems. After starting the script and inserting the pendrive the program will start copying using windows' builtin tool "robocopy". 

The robocopy command is made to exclude all directories and files by name from "excluded.txt". 

The script by default won't show any significant debug info like which folders, filese were copied nor will it display the progress or the job header thanks to \NFL \NDL \NP and \NJH flags in the subprocess command.

The script will only display the final result if the program exits with a robocopy return code that's less than 8. Otherwise it'll display an error message with the received error code.

The program copies the pendrive's files to a "!cwd" directory located in the same location as the script itself. The direcory will be created if it is missing.

#### Startup

1. Install python and uv
2. Clone the repository
git clone https://github.com/Outshader/Pendrive-AutoCopy
3. Move into directory 
cd Pendrive-AutoCopy
4. Install required packages
uv sync
5. Run the script
uv run main.py

If you want to build the project instead you need to install pyinstaller
uv add pyinstaller

And then build with it
uv run pyinstaller --onefile --windowed --disable-windowed-traceback --add-data "excluded.txt;." main.py

uv run pyinstaller --onedir --windowed --disable-windowed-traceback --add-data "excluded.txt;." main.py
