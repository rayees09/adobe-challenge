# adobe-challenge

Task 1 

## Coding Challenge
 
Using your preferred programming language (please avoid using bash, we tend to use python for this sort of thing) grab the list of public Adobe repos on github and print them into a table format from the command line. This table should be sorted by most recently updated. In your table output, feel free to include any fields that you think are useful. Perhaps number of stargazers? 
 
To get you started, this endpoint gets you most of the repository data.
 
```bash
curl -H "Accept: application/vnd.github.v3+json"   https://api.github.com/orgs/adobe/repos
```

How to execute the code 
Step 1 : Clone this repo
Step 2 : cd adobe-challenge/challenge1
Step 3 : python3 adobe-challege1.py

Execpted Result: 

-------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Repo ID            Repo Name                         Size (MB)            Stargazers        No Forks          License                 Updated                   |                      
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
| 2935735            brackets                          92974                33733             8264              MIT License             2021-09-13T10:39:40Z      |              
| 7567904            balance-text                      696                  1063              81                Not Available           2021-09-13T07:27:01Z      |              
| 3675253            adobe.github.com                  8137                 976               319               MIT License             2021-09-12T16:32:28Z      |              
| 4591454            GLS3D                             800                  103               51                Not Available           2021-09-10T16:38:11Z      |              
 


