# Задание: Колобок

![Задание35](photo/task35.png)

## Решение

**Нам дано изображение:**
![исходник](files/kolobok.jpg)

1. **Анализ:** Проверяем метаданные файла с помощью утилиты `exiftool`:
   ```bash
   exiftool kolobok.jpg
   ```
   ![res](photo/photo50.png)
2. В полях `Description`, `Title` и `XP Title` обнаруживаем захардкоженный флаг: `CTF{KOLOBOK_BEST_FILM}`.

---

**Флаг:** `CTF{KOLOBOK_BEST_FILM}`

**Автор:** [BoCoder](https://t.me/BoCoder_Python)  
**Сообщество:** [Community DailyCTF](https://t.me/+sQe0pGRw9KdlNGI6)
