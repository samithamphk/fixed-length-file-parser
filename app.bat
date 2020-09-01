echo File Parser for Lattitude by Samitha
echo .
cd venv/Scripts/activate.bat
set /p n=Enter the number of lines to be generated for the fixed length file?:
echo %n%
cd app
python lati-sam-app.py -n %n% 
echo File specification is read
echo Generate fixed length file at  data/flf.txt
echo Parsing fixed length file.
echo See the output at data/out.csv
cmd /k