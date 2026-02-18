# Realtime-information-chatbot

<div align="center">

[![Korean](https://img.shields.io/badge/Language-Korean-red)](#-korean-version)
[![Russian](https://img.shields.io/badge/Language-Russian-orange)](#-russian-version)
[![English](https://img.shields.io/badge/Language-English-blue)](#-english-version)

</div>

---
<h2 id="-korean-version">🇰🇷 Korean Version</h2>
# 📰 Real-time News Briefing Chatbot (Local LLM)

**Hacker News**의 최신 IT 트렌드를 실시간으로 수집(Scraping)하여, 로컬 LLM(**Ollama**)을 통해 한국어로 요약 및 브리핑해 주는 챗봇입니다.

LangChain의 `RunnableWithMessageHistory`를 활용하여 사용자와의 대화 맥락을 기억하며 질의응답이 가능합니다.

## ✨ Key Features (핵심 기능)

* **Real-time Scraping:** `BeautifulSoup4`를 사용하여 Hacker News의 상위 10개 기사를 실시간으로 가져옵니다.
* **Context Aware:** 대화 내용을 메모리(`InMemoryChatMessageHistory`)에 저장하여 이전 질문의 맥락을 이해하고 답변합니다.
* **Local LLM Powered:** 외부 API 비용 없이 로컬 환경의 `Ollama (qwen2.5-coder)` 모델을 사용하여 개인정보 유출 걱정 없이 동작합니다.
* **다국어 지원 (Adaptive Language Support)** : 복잡한 영어 기술 뉴스를 사용자가 질문한 언어에 맞춰 번역 및 설명합니다.
* **Modern Python Stack:** `uv` 패키지 매니저와 `Ruff` 린터를 적용한 최신 파이썬 개발 환경을 따릅니다.

## 🛠 Tech Stack

* **Language:** Python 3.12+
* **LLM Engine:** [Ollama]()
* **Model:** `qwen2.5-coder` (코딩 및 기술 관련 질의에 최적화)
* **Framework:** [LangChain]()
* **Web Scraping:** BeautifulSoup4
* **Package Manager:** [uv]()

## 🚀 Getting Started

이 프로젝트는 `uv`를 통해 의존성을 관리합니다.

### 1. Prerequisites (사전 준비)

1. **Ollama 설치 및 모델 다운로드** Ollama가 설치되어 있어야 하며, 터미널에서 아래 명령어로 모델을 받아야 합니다.
```bash
ollama pull qwen2.5-coder

```


2. **uv 설치 (파이썬 패키지 매니저)**
```bash
# Mac/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

```



### 2. Installation (설치)

프로젝트를 클론하고 의존성을 설치합니다. `uv sync` 명령어 하나로 가상환경 생성과 라이브러리 설치가 끝납니다.

```bash
git clone https://github.com/your-username/realtime-info-chatbot.git
cd realtime-info-chatbot

# 의존성 설치 및 가상환경 세팅
uv sync

```

### 3. Usage (실행)

아래 명령어로 챗봇을 실행합니다.

```bash
uv run news-chatbot.py

```

### 4. Commands (명령어)

챗봇 실행 후 프롬프트에서 사용할 수 있는 명령어입니다.

* `/refresh`: 최신 뉴스를 다시 크롤링하여 캐시를 업데이트합니다.
* `/exit`: 챗봇을 종료합니다.
* 그 외 입력: 뉴스 내용에 대해 자유롭게 질문합니다.

---

## 📂 Project Structure

```plaintext
realtime-info-chatbot/
├── news-chatbot.py             # 챗봇의 진입점 및 핵심 로직 (LangChain Chain 구성)
├── pyproject.toml      # 프로젝트 설정 및 의존성 관리 (uv & ruff 설정)
├── uv.lock             # 의존성 버전 잠금 파일
├── README.md           # 프로젝트 문서
└── .venv/              # 가상환경 (자동 생성됨)

```

## 🧩 Architecture Logic

1. **Fetch:** `requests`와 `BeautifulSoup`이 Hacker News에 접속하여 제목과 링크를 추출합니다.
2. **Cache:** 추출된 데이터는 `self.news_cache`에 문자열로 저장되어 반복적인 요청을 방지합니다.
3. **Inject:** 사용자의 질문(`input`)과 캐싱된 뉴스(`news`)가 프롬프트 템플릿에 주입됩니다.
4. **Generate:** `OllamaLLM`이 프롬프트와 대화 기록(`history`)을 바탕으로 답변을 생성합니다.
5. **Memory:** `RunnableWithMessageHistory`가 세션 ID를 기준으로 대화 내용을 갱신합니다.

## ⚠️ Troubleshooting

* **Error fetching news:** Hacker News의 HTML 구조가 변경되었을 수 있습니다. `_fetch_news` 메서드의 `span class="titleline"` 선택자를 확인하세요.
* **Ollama connection error:** 로컬에서 Ollama 앱이 실행 중인지 확인하세요. (`ollama serve` 또는 앱 실행)
* **ModuleNotFoundError:** `uv sync`를 실행하여 가상환경에 패키지가 제대로 설치되었는지 확인하세요.

---

## 📜 License

This project is licensed under the MIT License.

---

<h2 id="-russian-version">🇷🇺 Russian Version</h2>

📰 Чат-бот для краткого обзора новостей (Local LLM)
Этот чат-бот собирает последние IT-тренды с Hacker News в реальном времени и предоставляет краткие сводки и объяснения на корейском языке, используя локальную LLM (Ollama).

Используя RunnableWithMessageHistory от LangChain, бот запоминает контекст разговора, обеспечивая непрерывный диалог в формате "вопрос-ответ".

✨ Ключевые возможности
Сбор данных в реальном времени: Использует BeautifulSoup4 для мгновенного получения топ-10 статей с Hacker News.

Учет контекста: Сохраняет историю переписки в памяти (InMemoryChatMessageHistory), чтобы понимать суть вопросов на основе предыдущего контекста.

Работа на локальной LLM: Использует локальную модель Ollama (qwen2.5-coder), что исключает расходы на внешние API и защищает конфиденциальность данных.

Адаптивная языковая поддержка: Переводит и объясняет сложные технические новости на языке, который использует пользователь.

Современный стек Python: Проект создан с использованием новейших инструментов разработки: пакетного менеджера uv и линтера Ruff.

🛠 Технологический стек
Язык: Python 3.12+

LLM движок: Ollama

Модель: qwen2.5-coder (Оптимизирована для задач программирования и технических вопросов)

Фреймворк: LangChain

Веб-скрапинг: BeautifulSoup4

Пакетный менеджер: uv

🚀 Начало работы
Для управления зависимостями в этом проекте используется uv.

1. Предварительные требования
Установка Ollama и загрузка модели
Необходимо установить Ollama. Выполните следующую команду в терминале, чтобы загрузить модель:

Bash

ollama pull qwen2.5-coder
Установка uv (Пакетный менеджер Python)

Bash

# Mac/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
2. Установка
Клонируйте репозиторий и установите зависимости. Команда uv sync автоматически создаст виртуальное окружение и установит библиотеки.

Bash

git clone https://github.com/your-username/realtime-info-chatbot.git
cd realtime-info-chatbot

# Установка зависимостей и настройка окружения
uv sync
3. Запуск
Запустите чат-бота следующей командой:

Bash

uv run news-chatbot.py
4. Команды
Команды, доступные в командной строке после запуска бота:

/refresh: Повторный сбор последних новостей и обновление кеша.

/exit: Завершение работы бота.

Любой другой ввод: Задавайте любые вопросы по содержанию новостей.

📂 Структура проекта
Plaintext

realtime-info-chatbot/
├── news-chatbot.py     # Точка входа и основная логика (Конфигурация LangChain Chain)
├── pyproject.toml      # Настройки проекта и зависимости (uv & ruff)
├── uv.lock             # Файл фиксации версий зависимостей
├── README.md           # Документация проекта
└── .venv/              # Виртуальное окружение (Создается автоматически)
🧩 Логика архитектуры
Fetch (Сбор): requests и BeautifulSoup подключаются к Hacker News для извлечения заголовков и ссылок.

Cache (Кеширование): Извлеченные данные сохраняются в self.news_cache в виде строки для предотвращения повторных запросов.

Inject (Внедрение): Вопрос пользователя (input) и закешированные новости (news) внедряются в шаблон промпта.

Generate (Генерация): OllamaLLM генерирует ответ на основе промпта и истории диалога (history).

Memory (Память): RunnableWithMessageHistory обновляет контекст разговора на основе ID сессии.

⚠️ Устранение неполадок
Error fetching news: Возможно, изменилась HTML-структура сайта Hacker News. Проверьте селектор span class="titleline" в методе _fetch_news.

Ollama connection error: Убедитесь, что приложение Ollama запущено локально (ollama serve или открыто приложение).

ModuleNotFoundError: Выполните uv sync, чтобы убедиться, что все пакеты корректно установлены в виртуальное окружение.

📜 Лицензия
Этот проект распространяется под лицензией MIT.

---

<h2 id="-english-version">🇺🇸 English Version</h2>

📰 Real-time News Briefing Chatbot (Local LLM)
Real-time News Briefing Chatbot scrapes the latest IT trends from Hacker News in real-time and provides summaries and briefings in Korean using a Local LLM (Ollama).

It leverages LangChain's RunnableWithMessageHistory to remember the context of the conversation, enabling seamless Q&A interactions.

✨ Key Features
Real-time Scraping: Utilizes BeautifulSoup4 to fetch the top 10 articles from Hacker News instantly.

Context Aware: Stores conversation history in memory (InMemoryChatMessageHistory) to understand and answer based on previous context.

Local LLM Powered: Runs on the local Ollama (qwen2.5-coder) model, ensuring operation without external API costs and protecting data privacy.

Adaptive Language Support: Translates and explains complex English technical news in the user's preferred language.

Modern Python Stack: Built with the latest Python development environment using the uv package manager and Ruff linter.

🛠 Tech Stack
Language: Python 3.12+

LLM Engine: Ollama

Model: qwen2.5-coder (Optimized for coding and technical queries)

Framework: LangChain

Web Scraping: BeautifulSoup4

Package Manager: uv

🚀 Getting Started
This project uses uv for dependency management.

1. Prerequisites
Install Ollama & Download Model
Ollama must be installed. Run the following command in your terminal to pull the model:

Bash

ollama pull qwen2.5-coder
Install uv (Python Package Manager)

Bash

# Mac/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
2. Installation
Clone the project and install dependencies. uv sync handles virtual environment creation and library installation in one step.

Bash

git clone https://github.com/your-username/realtime-info-chatbot.git
cd realtime-info-chatbot

# Install dependencies and setup virtual environment
uv sync
3. Usage
Run the chatbot with the following command:

Bash

uv run news-chatbot.py
4. Commands
Available commands in the prompt after running the chatbot:

/refresh: Re-crawls the latest news and updates the cache.

/exit: Exits the chatbot.

Any other input: Ask questions freely about the news content.

📂 Project Structure
Plaintext

realtime-info-chatbot/
├── news-chatbot.py     # Entry point and core logic (LangChain Chain configuration)
├── pyproject.toml      # Project settings and dependencies (uv & ruff config)
├── uv.lock             # Dependency lock file
├── README.md           # Project documentation
└── .venv/              # Virtual environment (Automatically generated)
🧩 Architecture Logic
Fetch: requests and BeautifulSoup access Hacker News to extract titles and links.

Cache: Extracted data is stored as a string in self.news_cache to prevent redundant requests.

Inject: User input (input) and cached news (news) are injected into the Prompt Template.

Generate: OllamaLLM generates a response based on the prompt and conversation history (history).

Memory: RunnableWithMessageHistory updates the conversation context based on the session ID.

⚠️ Troubleshooting
Error fetching news: The HTML structure of Hacker News might have changed. Check the span class="titleline" selector in the _fetch_news method.

Ollama connection error: Ensure the Ollama app is running locally (ollama serve or open the app).

ModuleNotFoundError: Run uv sync to ensure packages are correctly installed in the virtual environment.

📜 License
This project is licensed under the MIT License.