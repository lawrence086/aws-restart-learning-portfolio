#!/bin/bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
    echo "Usage: bash backup_folder.sh SOURCE NEW_ARCHIVE.tar.gz" >&2
    exit 1
fi

source_dir=$(cd -- "$1" && pwd -P)
destination_dir=$(cd -- "$(dirname -- "$2")" && pwd -P)
archive_name=$(basename -- "$2")
archive="$destination_dir/$archive_name"

if [[ "$source_dir" == / || "$destination_dir" == "$source_dir" || "$destination_dir" == "$source_dir/"* ]]; then
    echo "Choose a destination outside the source folder, and do not archive /." >&2
    exit 1
fi

# Reserve the filename so an existing backup cannot be overwritten.
if ! (set -o noclobber; : > "$archive") 2>/dev/null; then
    echo "The archive already exists or cannot be created: $archive" >&2
    exit 1
fi

finished=false
cleanup() {
    if [[ "$finished" == false ]]; then
        rm -f -- "$archive"
    fi
}
trap cleanup EXIT

tar -czf "$archive" -C "$(dirname -- "$source_dir")" -- "$(basename -- "$source_dir")"
tar -tzf "$archive" > /dev/null
finished=true
printf 'Created and checked: %s\n' "$archive"
