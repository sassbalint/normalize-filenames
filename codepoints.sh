#!/bin/bash

while read string
do
    for ch in `echo $string | sed -e 's/\(.\)/\1\n/g'`
    do
        echo -n "$ch "
        echo -n "$ch" | iconv -f utf8 -t utf32be | \
            xxd -p | sed -r 's/^0+/0x/' | xargs printf 'U+%04X\n'
    done
done

# based on
# https://superuser.com/a/1019853/1182069
#   for converting to codepoints
# https://stackoverflow.com/a/10572879/8746466
#   for looping through a string
# https://stackoverflow.com/a/7045517/8746466
#   for reading stdin

