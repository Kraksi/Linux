#!/bin/bash

# Находим все файлы с расширением .txt в текущей директории
txt_files=$(find . -maxdepth 1 -type f -name "*.txt")

# Проверяем, найдены ли файлы
if [ -z "$txt_files" ]; then
  echo "Файлы с расширением .txt не найдены в текущей директории."
else
  echo "Найдены следующие .txt файлы:"
  echo "$txt_files"
fi
