import os
import re
import codecs
import glob
import subprocess
import argparse

def remove_links(content):  
    #find and replace ' structID="LinkTarget_*********"'
    content = re.sub(r'(\s*)(structID.\"LinkTarget.\d+\")', r' structID="LinkTarget_0000"', content)
    #find and replace ' id="LinkTarget_****">'
    content = re.sub(r'(\s*)(id.\"LinkTarget_\d+\")', ' id="LinkTarget_0000"', content)
    return content

def remove_lang(content):
    #find and replace ' xml:lang="**"'
    content = re.sub(r'(\s*)(xml:lang.\"\w+\")', r'', content)
    return content

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Strip Off Unecessary Tag Atrributes from Tag Files')
    parser.add_argument('-i', '--input_directory', type=str, required=True, help='Input Tags Directory')
    args = parser.parse_args()

    input_directory = args.input_directory
    
    tag_glob = os.path.join(input_directory, '*.tag')
    for file_path in glob.glob(tag_glob):
        print(f"Processing file: {os.path.basename(file_path)}")
        with codecs.open(file_path, 'r', 'utf-8', 'surrogateescape') as fp:
            content = fp.read()
        content = remove_links(content)
        content = remove_lang(content)
        with codecs.open(file_path, 'w', 'utf-8', 'surrogateescape') as fp:
            fp.write(content)