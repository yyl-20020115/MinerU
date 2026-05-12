#!/bin/bash
7z a -t7z -m0=lzma2 -mx=5 -ms=on -mhe=off $1 $2
