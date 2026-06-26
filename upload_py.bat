@echo off
REM === Navigate to your cloned repo ===
cd C:\Users\HP\FS-Bot-V4

REM === Copy all .py files from FS Bot folder into the repo ===
xcopy "C:\Users\HP\OneDrive\Desktop\FS Bot\*.py" "C:\Users\HP\FS-Bot-V4\" /Y

REM === Stage all .py files ===
git add *.py

REM === Commit with a message ===
git commit -m "Initial upload of Python files"

REM === Set your Git identity (only needed once) ===
git config --global user.name "arefinkn-ship-it"
git config --global user.email "arefinkn@gmail.com"

REM === Ensure branch is named main ===
git branch -M main

REM === Push to GitHub ===
git push -u origin main

echo Done! Your files should now be uploaded to:
echo https://github.com/arefinkn-ship-it/FS-Bot-V4
pause
