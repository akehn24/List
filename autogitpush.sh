git add .

echo 'Enter Commit Message:'
read commitMessage

git commit -m "$commitMessage"

echo 'Enter Branch Name:'
read branchName

git push origin $branchName

read