# python-debugging
Instructions
Overview
This repository contains a broken Python script designed for practising Git and GitHub workflows.
Your task is to fix the errors, commit your changes, and submit your work using a Pull Request.
This exercise teaches you how to:
•	Fork a repository
•	Clone your fork to your computer
•	Create and switch branches
•	Commit and push changes
•	Open a Pull Request to submit your work
Your Task
1.	Fork this repository to your own GitHub account
2.	Clone your fork to your computer
3.	Create a new branch with your name
4.	Fix the errors in broken_script.py
5.	Commit your changes with clear messages
6.	Push your branch to your fork
7.	Open a Pull Request back to the original repo

Step 1 — Fork the Repository
1.	At the top right of this page, click Fork
2.	Choose your GitHub account as the destination
3.	GitHub will create your own copy of this repo
You now have full control of your fork.

Step 2 — Clone Your Fork
Open VS Code, PowerShell, or Git Bash and run:
git clone https://github.com/<your-username>/<repo-name>.git
Then move into the folder:
cd <repo name>

Step 3 — Create a Branch
Create a branch with your name:
git checkout -b <your name>
Example:
git checkout -b damian 

Step 4 — Fix the Python Script
Open broken_script.py in your editor.
Fix the errors so the script runs correctly.
Take your time — commit small, meaningful changes.

Step 5 — Commit Your Changes
Stage your changes:
git add broken_script.py 
Commit them:
git commit -m "Fix errors in broken_script.py" 

Step 6 — Push Your Branch
Push your branch to your fork:
git push -u origin <your-branch-name>

Step 7 — Open a Pull Request
1.	Go to your fork on GitHub
2.	Click Compare & pull request
3.	Make sure the base repo is the college organisation repo
4.	Add a short description of what you fixed
5.	Submit the Pull Request
Your work is now ready for review.

Success Criteria
To complete this task, you must:
•	Use Git commands correctly
•	Commit with clear messages
•	Fix the Python script so it runs
•	Submit your work via a Pull Request

