# Домашняя работа — тестирование ПО (F‑Bank)

Репозиторий содержит:
- ручные тест-кейсы и баг-репорты
- Selenium автотесты на найденные дефекты
- GitHub Actions CI для запуска автотестов (сборка **красная**, т.к. дефекты воспроизводятся)

## 1) Запуск приложения локально

Из корня проекта:

```bash
python -m http.server 8000
```

Открыть в браузере: `http://localhost:8000/`

## 2) Документация

- Ручные тесты: `docs/manual-tests.md`
- Баг-репорты: `docs/bug-reports/BUG-01.md`, `docs/bug-reports/BUG-02.md`, `docs/bug-reports/BUG-03.md`
- Чек-лист соответствия: `docs/checklist.md`

## 3) Автотесты (pytest + Selenium)

### Установка

```bash
python -m pip install -r requirements.txt
```

### Запуск

1. В одном терминале запустить приложение:

```bash
python -m http.server 8000
```

2. Во втором терминале запустить тесты:

```bash
pytest -q
```

## 4) CI

Workflow: `.github/workflows/ci.yml`

CI поднимает локальный `http.server` и запускает `pytest`. Тесты ожидаемо падают, потому что проверяют **ожидаемое корректное поведение**, а в приложении присутствуют дефекты (BUG-01..BUG-03).

