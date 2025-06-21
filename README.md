# 📊 Impedance Data Manager

Инструмент для загрузки, обработки и выгрузки данных импедансной спектроскопии из `.z`-файлов с автоматическим извлечением параметров материалов из структуры каталогов и сохранением в базу данных PostgreSQL.

## 🧩 Основной функционал

- 📂 **Добавление данных** из иерархии папок с файлами измерений (`adding_data.py`)
- 🧪 Автоматическое определение параметров материала из названия папки
- 📊 Сохранение результатов измерений (Re, Im, Частота) в PostgreSQL
- 📤 **Фильтрация и выгрузка данных** по критериям (`unloading_processing_data.py`)
- 🧱 Использование ORM SQLAlchemy и DataFrame-инструментов `pandas`

## 📁 Структура проекта

```
├── adding_data.py               # Сканирование директорий и добавление данных в БД
├── unloading_processing_data.py # Выгрузка отфильтрованных данных из БД
├── connection.py                # Определение моделей SQLAlchemy и подключение к PostgreSQL
├── processing_dir.py            # Обработка названий директорий и чтение .z файлов
├── requirements.txt             # Зависимости проекта
```

## ⚙️ Установка

```bash
git clone https://github.com/your_username/impedance-data-manager.git
cd impedance-data-manager
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate на Windows
pip install -r requirements.txt
```

Также требуется установленный PostgreSQL с БД:

- имя: `Impedance_db`
- пользователь: `postgres`
- пароль: `1234`

(Можно изменить в `connection.py`)

## 🚀 Использование

### Добавление данных

1. Запусти `adding_data.py`
2. В появившемся окне выбери директорию с подпапками.  
   Каждая подпапка должна быть названа в формате:
   ```
   YYYY-MM-DD_E1_P1_P1%_P2_P2%_starch%_thickness
   ```
   Например: `2024-05-19_Li_20_Na_1.5_C_80_5_0.3`

### Выгрузка отфильтрованных материалов

```bash
python unloading_processing_data.py
```

## 💾 Пример структуры таблиц

- `Material`: информация о составе и толщине
- `Experiment`: время эксперимента и связь с материалом
- `Measure`: значения Re, Im, частоты и номер точки

## 🛠️ Используемые технологии

- Python 3.11+
- SQLAlchemy
- Pandas
- PostgreSQL
- Tkinter (для выбора папки)

## 🧑‍💻 Автор

Проект разработан для автоматизации анализа данных импедансной спектроскопии.  
Если есть вопросы — [свяжитесь со мной](mailto:youremail@example.com)
