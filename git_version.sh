# Versionar en GIT
git init 
git add .
git status 
git commit -m "WC: File config repository"
# Crear una rama
git branch initial
# Check rama 
git checkout initial
# Crear repositorio remoto y agregar repositorio principal
git remote add ini_wc https://github.com/dcuasapaz/warncity.git
# Agregar rama a repositorio remoto
git push ini_wc initial

<< COMMENT 

Username for 'https://github.com': dcuasapaz
Password for 'https://dcuasapaz@github.com': 
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 558 bytes | 50.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
remote: 
remote: Create a pull request for 'initial' on GitHub by visiting:
remote:      https://github.com/dcuasapaz/warncity/pull/new/initial
remote: 
To https://github.com/dcuasapaz/warncity.git
 * [new branch]      initial -> initial

COMMENT
