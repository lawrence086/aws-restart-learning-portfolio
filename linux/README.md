# Linux practice

My Linux labs used Amazon Linux on EC2. I connected over SSH, worked with files and editors, managed users and groups, and inspected processes.

| Topic | What I practised or learned |
| --- | --- |
| Files and folders | Created a company folder structure, then moved and copied its contents. `rmdir` only removes an empty directory. |
| Editing | Used Vim and nano. In Vim, `:wq` saves and exits, and `:q!` discards unsaved edits. A lab timeout was a reminder to save regularly. |
| Users and permissions | Created users and group memberships, then checked access as a normal user. A sudo denial helped show the permission boundary. |
| Backups | Created a compressed tar archive and logged its filename. Checking the archive is part of making the backup. |
| Processes | Used `ps` and `top` to inspect processes before setting up a scheduled audit script. |
| Scheduling | My cron entry had `SHELL=bin/bash`. I needed `SHELL=/bin/bash` with the leading slash. |

## Run the backup example

I wrote [backup_folder.sh](backup_folder.sh) to practise creating and checking a `.tar.gz` archive after the file backup lab. It requires a source directory and a new archive path. It checks the archive listing and refuses to overwrite an existing file.

```sh
mkdir -p /tmp/restart-practice/source
printf 'Backup practice\n' > /tmp/restart-practice/source/note.txt
bash linux/backup_folder.sh /tmp/restart-practice/source /tmp/restart-practice/example.tar.gz
tar -tzf /tmp/restart-practice/example.tar.gz
```

The destination directory must already exist and must be outside the source folder. Choose a different archive name for another run.

## A scheduling example

This crontab example runs the audit script at the start of each hour.

```cron
SHELL=/bin/bash
PATH=/usr/bin:/bin
0 * * * * /home/student/scripts/process-audit.sh >> /home/student/process-audit.log 2>&1
```

The script and output paths must exist and be accessible to the user running the job. I would first run the script manually, then check the job's output after its scheduled time.
