#!/bin/bash

# Проверяем, что файлы существуют
if [[ ! -f "file2.txt" || ! -f "file3.txt" || ! -f "file4.txt" ]]; then
  echo "Один или несколько файлов (file2.txt, file3.txt, file4.txt) не найдены!"
  exit 1
fi

# Объединяем содержимое файлов в новый файл combined.txt
cat file2.txt file3.txt file3.txt > combined.txt

# Проверяем успешность операции
if [[ $? -eq 0 ]]; then
  echo "Файлы успешно объединены в combined.txt"
else
  echo "Ошибка при объединении файлов"
  exit 1
fi
