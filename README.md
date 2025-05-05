# stress_app

stress-app/                  # Корневая папка проекта
├── backend/                 # Бэкенд на FastAPI
│   ├── app/                # Основной код бэкенда
│   │   ├── __init__.py
│   │   ├── main.py         # Точка входа (роуты)
│   │   ├── models.py       # SQLAlchemy-модели БД
│   │   ├── schemas.py      # Pydantic-схемы для валидации
│   │   ├── auth.py         # Аутентификация (JWT)
│   │   └── ml/             # Интеграция нейросети
│   │       ├── model.py    # Загрузка и инференс модели
│   │       └── tokenizer/  # Токенизатор (если нужно)
│   ├── tests/              # Тесты API
│   ├── static/             # Статические файлы (если нужно)
│   ├── requirements.txt    # Зависимости Python
│   └── Dockerfile          # Контейнеризация бэкенда
│
├── frontend/               # Фронтенд на React
│   ├── public/             # Статические файлы (index.html)
│   ├── src/
│   │   ├── components/     # React-компоненты
│   │   │   ├── Auth/
│   │   │   ├── Dashboard/
│   │   │   └── Diagnosis/
│   │   ├── pages/          # Страницы
│   │   ├── App.js          # Главный компонент
│   │   └── index.js        # Точка входа
│   ├── package.json        # Зависимости JavaScript
│   └── Dockerfile          # Контейнеризация фронтенда
│
├── ml/                     # ML-модель и её обучение
│   ├── train_model.ipynb   # Ноутбук с обучением (Kaggle)
│   ├── stress_model.pt     # Сохранённая модель (PyTorch)
│   └── requirements.txt    # Зависимости для обучения
│
├── database/               # Скрипты для работы с БД
│   ├── init_db.py          # Инициализация БД (таблицы)
│   └── migrations/         # Alembic-миграции (если нужно)
│
├── docs/                   # Документация
│   ├── ER-diagram.drawio   # Диаграмма БД
│   ├── API-spec.yaml       # OpenAPI-спецификация
│   └── README-dev.md       # Инструкции для разработчиков
│
├── docker-compose.yml      # Оркестрация контейнеров
└── README.md               # Общее описание проекта