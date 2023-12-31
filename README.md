# Journey In The Dream
Путешествие во сне — игра в жанре RPG, в которой главная героиня попадает в мир своих снов. Чтобы не остаться здесь навсегда, ей нужно как можно скорее вернуться в реальность! Помогите ей преодолеть опасности, встречающиеся на её пути...

Для прохождения игры нужно продвигаться по сюжету, решая пятнашки, выдоваемые разными персонажами.
С продвижением дальше по сюжету будет расти сложность пятнашек (увеличится число сегментов).

### Техническое задание:
- Регистрация (сохранение в БД имени пользователя)
- Сохранение времени прохождения в БД
- Если хватит времени, добавление системы достижений и сохранение полученных достижений в БД
- **7+ окон:**
  - Начальное окно (окно регистрации и входа в игру)
  - Финальное окно с результатами
  - 3 сюжетных окна
  - Окно-помощь (управление и пр.)
  - Окно с пятнашками
- Фоновая музыка, звуки взаимодействия
- Таймер (подсчет общего времени прохождения, ограничение времени в пятнашках)
- Возможно, будет инвентарь
- Подсчет количества жизней, снятие жизней за превышение времени таймера пятнашек

### Управление:
- клавиши WASD для передвижения
- клавиша F для взаимодействия
- левая кнопка мыши для игры в пятнашки

[//]: # (### Описание окон:)

[//]: # (- Стартовое окно:)

[//]: # (  - Ввод имени пользователя)

[//]: # (  - Кнопка "Начать игру")

[//]: # (- Финальное окно:)

[//]: # (  - Вывод результатов)

[//]: # (- Окно-помощь:)

[//]: # (  - Описание управления)

[//]: # (  - 🚩*Подсказки?*)

[//]: # (- Сюжетные окна:)

[//]: # (  - Перемещение по окну)

[//]: # (  - Взаимодествие с персонажами и предметами)

[//]: # (- Окно с пятнашками:)

[//]: # (  - Окно с головоломкой, которую нужно решить, чтобы пройти дальше по сюжету )

### Подсчёт очков:
Очки будут подсчитаны исходя из полученных достижений и времени, затраченного на прохождение.
Кроме того, очки будут сниматься за смерть персонажа (потеря всех очков здоровья / сердец)


### Визуальное оформление:
Фоновое изображение, спрайты персонажей и предметов будут отрисованы вручную. Во время диалогов, при ходьбе и при прохождении уровня в пятнашках будут вопсроизводиться анимации.
Персонаж не будет проходить сквозь другие объекты на экране и НПС


