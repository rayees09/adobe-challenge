# adobe-challenge

Task 1 

## Coding Challenge
 
Using your preferred programming language (please avoid using bash, we tend to use python for this sort of thing) grab the list of public Adobe repos on github and print them into a table format from the command line. This table should be sorted by most recently updated. In your table output, feel free to include any fields that you think are useful. Perhaps number of stargazers? 
 
To get you started, this endpoint gets you most of the repository data.
 
```bash
curl -H "Accept: application/vnd.github.v3+json"   https://api.github.com/orgs/adobe/repos
```

