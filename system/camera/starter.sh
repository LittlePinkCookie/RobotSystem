#!/usr/bin/env bash

raspivid -t 0 -w "$1" -h "$2" -hf -ih -fps "$3" -o - -a 12 | nc -k -l "$4"