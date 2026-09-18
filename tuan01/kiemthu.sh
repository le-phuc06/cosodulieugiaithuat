#!/bin/bash
# Ten lenh Python khac nhau giua cac he dieu hanh:
# Linux va macOS dung python3, Windows dung python.
PY=python

for i in $(seq 1 200); do
    $PY sinh.py $i > tam.txt
    ./tong < tam.txt > kq1.txt
    $PY vetcan.py < tam.txt > kq2.txt
    if ! diff -q kq1.txt kq2.txt > /dev/null; then
        echo "SAI o bo du lieu $i:"; cat tam.txt
        echo "chuong trinh cua ban: $(cat kq1.txt)"
        echo "dap an dung:         $(cat kq2.txt)"
        exit 1
    fi
done
echo "Da chay 200 bo du lieu ngau nhien, khong tim thay bo nao sai."