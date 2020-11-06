# programmong_part_3_lab_2
## input.py
**input_values - Додаємо в масив та сортуємо зустрічі**
Ця функція виконується після останнього елемента в масиві, видаючи сам посортований масив зустрічей
```python
        if raw_numbers == "":
            print("Unmerged meetings")
            print(merged_meetings)
            print("Your merged meetings are:")
            break
```
Тут ми не дозволяємо вписувати зустрічі в яких початок зустрічі більший ніж її кінець. Якщо зустріч не підпадає під це обмеження - вона спокійно додається в масив:
```python if int(meeting_start) > int(meeting_end):
            print("Error, not correctly added values. Your first value should be smaller")
        else:
            merged_meetings.append((int(meeting_start), int(meeting_end)))
```
## utils.py
**merge_ranges - Додаємо в масив та сортуємо зустрічі**
Створюємо output масив куди будуть передаватись вже обєднані діапазони зустрічей:
```python merged_meetings = []
```
Початок роботи, кінець роботи першого зустрічі в списку
```python
previous_meeting_start, previous_meeting_end = meetings[0]
```
Для кожної наступної зустрічі:
```python
for current_meeting_start, current_meeting_end in meetings[1:]:
```
Якщо одна команда почала працювати раніше ніж закінчила інша чи просто одна команда вирішила працювати без перерв:
порівнюється початок другої зустрічі і кінець першої
```python
        if current_meeting_start <= previous_meeting_end:
```
Якщо виявилось що друга зустріч почалась раніше ніж закінчилась перша - зустрічі обєднуються:
```python
            previous_meeting_end = max(current_meeting_end, previous_meeting_end)
```
Інакше перший зустріч залишається незмінною, і додається в новий список а її значення(позиція)присвоюється наступній
```python       else:
                      merged_meetings.append((previous_meeting_start, previous_meeting_end))
                      previous_meeting_start, previous_meeting_end = current_meeting_start, current_meeting_end
```
Обєднана зустріч додається до списку
```python
    merged_meetings.append((previous_meeting_start, previous_meeting_end))
```
Повертається масив об'єднаних значень:
```python  return merged_meetings```
