import urllib3, json

class Challenge:
    def __init__(self):
        self.repo_url = 'https://api.github.com/orgs/adobe/repos'
    
    def getRepos(self):
        http = urllib3.PoolManager()
        response = http.request('GET', self.repo_url )
        repo_list = json.loads(response.data.decode('UTF-8'))
        # Get list of repos in sorted order based on last updated
        sorted_repo_list = sorted(repo_list, key=lambda k: k['updated_at'], reverse=True)
        print("-"*163)
        print ("{:<20} {:<32} {:<21} {:<17} {:<17} {:<23} {:<25} {:<23}".format( "| Repo ID", "Repo Name", " Size (MB)", "Stargazers", "No Forks ", "License", "Updated" , "|"))
        print("-"*163)
        for repo in sorted_repo_list:
            repo_id = repo.get("id") 
            repo_name = repo.get("name")
            repo_size = repo.get("size")
            stargazers_count = repo.get("stargazers_count")
            forks = repo.get("forks")
            updated_at = repo.get("updated_at")
            license = "Not Available"
            if(repo.get("license") != None) and (repo.get("license").get("name") != "Other"):
                license = repo.get("license").get("name")
            print ("{:<1} {:<18} {:<33} {:<20} {:<17} {:<17} {:<23} {:<25} {:<15}".format("|", repo_id, repo_name, repo_size, stargazers_count, forks, license, updated_at ,"|"))
        print("-"*163)


repos = Challenge()
repos.getRepos()
