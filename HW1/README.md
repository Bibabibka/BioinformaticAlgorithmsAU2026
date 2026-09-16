# Homework 1
ФИО: Виноградов Дмитрий Михайлович
Группа: 402
## Выполненные задачи
- Reverse Complement
- Neighbors
- Frequent Words with Mismatches and Reverse Complements
## Git commands
- `git status` — посмотреть состояние файлов
- `git diff` — посмотреть изменения
- `git add FILE` — подготовить файл к коммиту
- `git commit -m "MESSAGE"` — создать коммит
- `git push` — отправить коммиты на GitHub
- `git log --oneline` — посмотреть историю
## Branching and revert
### Состояние после первого слияния
После выполнения `git merge --no-ff testing` в ветку `HW1` были объединены изменения из двух веток. 
В `HW1` находились:
- `HW1/README.md` и `HW1/reverse_complement.py`
- `HW1/neighbors.py` 
### Состояние после отмены слияния
После выполнения `git revert -m 1 <hash>` из ветки `HW1` были отменены все изменения, пришедшие из ветки `testing`. 
- `HW1/neighbors.py` был удален из ветки `HW1`
- Файлы, созданные  в ветке `HW1` сохранились
### Вопросы

1. **Какой результат вы ожидали?**  
   Ожидалось, что при повторном слиянии ветки `testing` в `HW1` файл `HW1/neighbors.py` восстановится в ветке `HW1`

2. **Что произошло на самом деле?**  
   Ветка `testing` слилась без конфликтов, однако файл `HW1/neighbors.py` не появился в `HW1`.

3. **Почему файл neighbors.py не восстановился?**  
   Git отслеживает изменения последовательных коммитов. Ранее слияние уже происходило и коммит `git revert -m 1` 
   отменил изменения из `testing` (включая добавление `neighbors.py`). 
   При повторном слиянии Git увидел отсутстиве изменений и наложил отмену на `neighbors.py`

4. **Какой командой вы восстановили его?**  
   Файл был восстановлен путем отмены отменяющего коммита:  
   `git revert <HASH_REVERT_COMMIT>`

### Справочник Git-команд
- `git branch NAME` — создать ветку
- `git switch NAME` — перейти в другую ветку
- `git switch -c NAME` — создать ветку и перейти в неё
- `git merge BRANCH` — выполнить слияние
- `git merge --no-ff BRANCH` — выполнить слияние с обязательным созданием merge-коммита
- `git revert -m 1 HASH` — отменить merge-коммит
- `git revert HASH` — отменить обычный коммит
- `git log --oneline --graph --all` — показать историю и ветвление
- `git branch -d NAME` — удалить локальную ветку
- `git push origin --delete NAME` — удалить удалённую ветку
- `git add FILE` — добавить файл в индекс (staging area)
- `git commit -m "MESSAGE"` — зафиксировать изменения
- `git push origin BRANCH` — отправить изменения в удаленный репозиторий
- `git status` — проверить текущее состояние рабочей директории и индекса