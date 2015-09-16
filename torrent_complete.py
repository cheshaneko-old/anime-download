#!/usr/bin/python3
import os
import re
import argparse

def main(tr_dir, tr_name):
    # qbittorrent give path with torrent 
    tr_dir = os.path.dirname(tr_dir)
    # transmission way
    #tr_dir = os.environ['TR_TORRENT_DIR']
    #tr_name = os.environ['TR_TORRENT_NAME']
    pattern = re.compile("""
        (\[.+\])?       # release group name 
        \s*
        (?P<name>.+?)   # anime name
        \s*
        -               # separator
        \s*
        \d+             # episod number
        .+              # some other staff
        (mkv)|(mp4)     # format
    """, re.VERBOSE)
    if pattern.match(tr_name):
        folder_name = pattern.match(tr_name).group('name')
        folder_name = os.path.join(tr_dir, folder_name)
        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)
        old_path = os.path.join(tr_dir, tr_name)
        new_path = os.path.join(folder_name, tr_name)
        os.rename(old_path, new_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("tr_dir", help="Torrent path")
    parser.add_argument("tr_name", help="Torrent name")
    args = parser.parse_args()
    main(args.tr_dir, args.tr_name)
