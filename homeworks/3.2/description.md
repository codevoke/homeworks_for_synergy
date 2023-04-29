# Задачи

---
Дана библиотека, написанная на Python - Geometric Lib. Файловая структура данной
библиотеки представлена ниже: 

![lib_structure](git_struct.png)
1. Необходимо объединить два коммита в ветке “develop” одной и той же тематики "L-04:
Add calculate.py", "L-04: Update docs for calculate.py" и написать к нему пояснение
# Решение

--- 

Выполним задачу:

Переходим на ветку `develop`
```
git checkout develop
```

Просматриваем историю коммитов ветки `develop`  
Коммиты b5b0fa и d76db2 можно объединить
```
git log
```
![git log](git_log.jpg)

Просматриваем текущее состояние
``` 
git status
```
![git status](git_status.jpg)

**Делаем объединяющий коммит**
``` 
git commit -c ORIG_HEAD
```
![git commit result](commit_result.jpg)

Убеждаемся что в истории появился еще один коммит фа2е624  
Который объединяет в себе коммиты b5b0fa и d76db2
``` 
git log
```
![git final log](git_final_log.jpg)
[Назад](../../readme.md)