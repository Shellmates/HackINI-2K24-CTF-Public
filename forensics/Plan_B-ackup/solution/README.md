# Plan B-ackup

## Write-up

- Given the Ansible playbook, we can conclude that it archives a folder, encrypt it using `my_secret.txt` which is the vault password and finally push it to a github repository.
  
>Ansible is an automation tool that is widely used for tasks such as application deployment, updates on workstations and servers ... etc.

- Let's clone the mentioned [repository](https://github.com/4NG3L-4/Backeup.git). We can find the Ansible vault and a deleted `my_secret.txt`

- Looking into the commits, we can extract the vault password using:
```python
import git

Secret = ''
repo = git.Repo('/path/to/cloned/repo')
for commit in repo.iter_commits():
    try:
        for diff_added in commit.diff(commit.parents[0]).iter_change_type('A'):
            Added = diff_added.b_blob.data_stream.read().decode('utf-8')
            Secret += Added[0]

        for diff_modified in commit.diff(commit.parents[0]).iter_change_type('M'):
            Modified = diff_modified.b_blob.data_stream.read().decode('utf-8')
            Secret += Modified[0]
    except Exception as e:
        pass

vault_pass = ''.join(reversed(Secret))
print(vault_pass[1:])
```

- We decrypt the ansible vault using the password `q7St!e@5BAy6jBAy` and the command:
```bash
ansible-vault decrypt --ask-for-password Backup.tar.gz
```

- We extract it, the folder `Library/FamilyPics` contains an interesting JPEG that has `johnwatson is my login password` as a comment in its EXIF data. Let's keep a note of.

- Then, We are looking into some interesting macOS directories and files like *.Trash*, *Keychains*, *.DS_Store*.
 
>DS_Store files are invisible files on the macOS operating system that stores custom attributes and metadata of its containing folders, such as folder view options, icon positions, and other visual information. 

>Keychain is a secure storage system that stores sensitive information such as passwords, certificates, and keys. Generally, the user login password unlocks the keychain. 

>The interesting fact about macOS trash is that it has also a .DS_Store file, which, even after you empty the trash the files attributes remain stored in that file.

- Let's parse *.DS_Store* files using [DSStoreParser](https://github.com/nicoleibrahim/DSStoreParser). We check the `DS_Store-Miscellaneous_Info_Report-*-*.tsv`. We extract the `record_filename` column. We extract all the filenames, decode from base64 and we get the first part of the flag.

- Moving to the Keychains, The keychains password is as same as the user login password which is in this case `johnwatson`. We can dump it using [chainbreaker](https://github.com/n0fate/chainbreaker). We find the secure note `flag part 02` in `login.keychain-db`.

## Flag

`shellmates{NaV1gAT3_tH3_unS33n_WHEre_F1l3$_gAThEr_T0_c0nv3Ne}`
