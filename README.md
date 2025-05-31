# 🇬🇧 English version 
## Crosshair Overlay

### The project creates a semi-transparent crosshair overlay on top of all windows, including fullscreen games. The crosshair does not interfere with interaction with other applications.

### 📌 Features
- Red crosshair in the center of the screen
- Works on top of all windows (including games)
- Does not block clicks (you can play/work)
- Adjustable size and color (via code)
- Compact .exe file for convenient usage

### ⚙️ Technologies
- Python 3.x
- PyWin32 (for working with Windows API)
- PyInstaller (for building into .exe)

### 📦 Installing dependencies
```bash
pip install pywin32 pyinstaller
```

### 🔨 Building the project
- Save the code to a file named `crosshair.py`

Run the command:

```bash
pyinstaller --onefile --windowed crosshair.py
```
- The compiled .exe will be located in the `dist` folder

### ⚡ Usage
- Run `crosshair.exe` from the `dist` folder
- To close: Task Manager → End `crosshair.exe`

### 🛠 Configuration
- In the `crosshair.py` file, you can modify:

```python
pen = win32gui.CreatePen(win32con.PS_SOLID, 2, win32api.RGB(255, 0, 0))
size = 6  # Crosshair size

# Color (R, G, B)
#RGB(255, 0, 0)  # Red

# Line thickness (in pixels)
#PS_SOLID, 2

# Crosshair size
#size = 6
```

### 📜 License
- Free for personal use

---

# 🇷🇺 Русская версия
## Crosshair Overlay

### Проект создает полупрозрачный прицел поверх всех окон, включая полноэкранные игры.  Прицел не мешает взаимодействию с другими приложениями.

### 📌 Особенности
- Красный прицел в центре экрана
- Работает поверх всех окон (включая игры)
- Не блокирует клики (можно играть/работать)
- Настраиваемый размер и цвет (через код)
- Компактный .exe файл для удобного использования

### ⚙️ Технологии
- Python 3.x
- PyWin32 (для работы с Windows API)
- PyInstaller (для сборки в .exe)

### 📦 Установка зависимостей
```bash
pip install pywin32 pyinstaller
```

### 🔨 Сборка проекта
- Сохраните код в файл crosshair.py

Выполните команду:

```bash
pyinstaller --onefile --windowed crosshair.py
```
- Готовый .exe будет в папке dist

### ⚡ Использование
- Запустите crosshair.exe из папки dist
- Для закрытия: Диспетчер задач → Завершить crosshair.exe

### 🛠 Настройка
- В файле crosshair.py можно изменить:

```python
pen = win32gui.CreatePen(win32con.PS_SOLID, 2, win32api.RGB(255, 0, 0))
size = 6  # Размер прицела

# Цвет (R, G, B)
#RGB(255, 0, 0)  # Красный

# Толщина линий (в пикселях)
#PS_SOLID, 2

# Размер прицела
#size = 6
```

### 📜 Лицензия
- Свободно для личного использования