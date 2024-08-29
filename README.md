Azeem khan
Student At Aligarh Muslim University
 HEAD
git remote set-url origin https://Azeem-khan0786:<your-token>@github.com/Azeem-khan0786/MyRepository.git

From August 13, 2021, GitHub is no longer accepting account passwords when authenticating Git operations.
```
You need to add a PAT (Personal Access Token) instead, and you can follow the below method to add a PAT on your system.
// Error During push code in remote

git push origin main Username for 'https://github.com': Azeem-khan0786 Password for 'https://Azeem-khan0786@github.com':  remote: Support for password authentication was removed on August 13, 2021. remote: Please see https://docs.github.com/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication. fatal: Authentication failed for 'https://github.com/Azeem-khan0786/MyRepository.git/'
```
Create Personal Access Token on GitHub
```
From your GitHub account, go to Settings => Developer Settings => Personal Access Token => Generate New Token (Give your password) => Fillup the form => click Generate token => Copy the generated Token,
it will be something like ghp_sFhFsSHhTzMDreGRLjmks4Tzuzgthdvfsrta
```
Then use this command to push 
```
 git remote set-url origin https://Azeem-khan0786:<your-token>@github.com/Azeem-khan0786/MyRepository.git
 c2a5758244ddc2cb8f1187bb3794d508f33e25f9
```

# Remote to local 
git clone https://github.com/Azeem-khan0786/MyRepository.git (if want to clone into local)
1. cd Desktop 
2. mkdir Repository
3. cd Repository
4. git clone https://github com/Azeem-khan0786/MyRepository git
5. cd MyRepository
6. git pull origin main
7. git status
8. git add  
9. git commit -m "first commit"
10. git push origin main
11. git status
12. git branch
13. git checkout -b newbranch
14. git branch

# Local to Remote Push repository
1. cd Desktop 
2. mkdir MyRepository
3. cd MyRepository
4. git init
5. git add . 
6. git commit -m "first commit"
7. git remote add origin https://github. com/Azeem-khan0786/MyRepository. git
8. git push -u origin main
9. git status
10. git branch
11. git checkout -b newbranch
12. git branch

# Genrate personal access Tokan()
1. Go to Settings => Developer Settings => Personal Access Token => Generate New Token (Give your password)
2. Fillup the form
3. click Generate token
4. Copy the generated Token, it will be something like ghp_sFhFsSHhT
5. git remote set-url origin https://Azeem-khan0786:<your-token>@githubcom/Azeem-khan0786/MyRepository.git
6. c2a5758244ddc2cb8f1187bb3794d508f33e25f9
7. git remote -v
8. git push origin main
9. git status
10. git branch
