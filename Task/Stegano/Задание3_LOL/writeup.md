# Задание: LOL

![Задание33](photo/task33.png)

## Решение

**Нам дано изображение:**
![исходник](files/LOL.png)

1. Запускаем binwalk:
binwalk -e LOL.png 
![binwalk](photo/photo48.png)
И видим, что к фото прикреплено изображение с именем secret.png
2. Смотрим результат, что команда достала и видим фото:
![binwalk](photo/secret.png)

---

**Флаг:** `CTF{s3cr3t_d0gs_1s_h@ppy}`

**Автор:** [BoCoder](https://t.me/BoCoder_Python)  
**Сообщество:** [Community DailyCTF](https://t.me/+sQe0pGRw9KdlNGI6)