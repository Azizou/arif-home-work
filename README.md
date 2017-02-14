# arif-home-work
Tutorial materrial for Arif

Instruction to upload your code:
==

You might find this process a bit tedious at first, but I want you to learn the right way to do it from the start. No shortcut in your path to greatness

#Version control:
This tool allows you to keep track of the different version of your solution/programs. If you decided that you have a better solution, you make changes and what happens if the new solution does not work? You ideal want to use the old solution that was working. Instead of creating copies of your project as you make changes, this allows you to track them within the same project through versioning and braching. You should try to learn more about it in your own time.

#Install and configure git
```
sudo apt-get install git (on a debian system) will suffice to install it. Then run:
git config --global user.name “Arif Ogbone”
git config --global user.email your email@address.com
```
Only run the above command the first time you install git, not for every project

#Adding git to project and project files to git
Got into your project directory and run:
```git init
git add -A
git commit -m “Initial commit”
```
#Remote repository:
Create a github account through github.com

On your home page (github.com when logged in), click New repository (currently green button) to create a new repository
give a descriptive name like python-homeworks-solutions and hit Create repository at the bottom of the page


#Uploading the code
Go back to your command line and execute:
```
git remote add origin git@github.com:Azizou/arif-home-work.git (this should be the link of the repo you created
git push -u origin master
```
#Updating changes in git
If you make any change to the code and want to upload it, first add it, then commit and finally push the change:
```
git add -A
git commit -m “description of the change”
git push origin master
```
***NB:*** When you execute the push command, you will have to identify yourself by typing your username and password at the prompt

