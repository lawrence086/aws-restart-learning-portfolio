# AWS re/Start learning portfolio

This portfolio follows my learning through AWS re/Start, from computing and professional skills to Python, Linux, databases and AWS services.

| Area | What's here |
| --- | --- |
| [Programme coverage](learning-map.md) | Weekly topics and scheduled activities |
| [Lab index](lab-index.md) | Python, Linux, SQL and AWS exercises |
| [Python](python/README.md) | A Caesar cipher, CSV inventory summary and sequence processing exercise |
| [Linux](linux/README.md) | File backups, permissions, users, processes and a cron mistake I learned from |
| [SQL](sql/README.md) | A small shop dataset with joins, grouping and transaction practice |
| [AWS labs](aws-labs/README.md) | Write-ups covering compute, networking, storage, databases, monitoring and security |
| [Professional skills](professional-skills/README.md) | How I approach problems, explain my work and keep learning |

## Try the code

Python 3.10 or newer is enough for the Python and SQL exercises. They use the standard library and don't need an AWS account.

```sh
python3 python/caesar_cipher.py "Hello, world!" 3
python3 python/fleet_inventory.py
python3 python/insulin_sequences.py
python3 -m unittest discover -s python -v
python3 sql/verify.py
```

The [Linux example](linux/README.md) uses Bash and tar. Run it in a Linux environment or on macOS.
