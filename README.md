# adobe-challenge

##  Task 1  -  Coding Challenge
 
Using your preferred programming language (please avoid using bash, we tend to use python for this sort of thing) grab the list of public Adobe repos on github and print them into a table format from the command line. This table should be sorted by most recently updated. In your table output, feel free to include any fields that you think are useful. Perhaps number of stargazers? 
 
To get you started, this endpoint gets you most of the repository data.
 
```bash
curl -H "Accept: application/vnd.github.v3+json"   https://api.github.com/orgs/adobe/repos
```

How to execute the code 
Step 1 : Clone this repo
Step 2 : cd adobe-challenge/challenge1
Step 3 : python3 adobe-challege1.py

Execpted Result: Resut in tabular with following fields  

         Repo ID            
         Repo Name                         
         Size (MB)            
         Stargazers       
         No Forks          
         License 
         Updated  

##  Task 2  -  Design Challenge : Option 2

Provide the design for an HTTP based service that returns the simple HTML message "Hello, Adobe!". This service will run in a container and should only expose ports needed to be accessed via http/https. 

Detailed designed document available at challenge2/design/Adobe_Challenge2.pdf
