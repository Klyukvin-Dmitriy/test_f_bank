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
- Чек-лист соответствия: `docs/checklist.md`

### Баг-репорты (GitHub Issues)

Официальная фиксация дефектов — во вкладке [Issues](https://github.com/Klyukvin-Dmitriy/test_f_bank/issues):

| Дефект | Issue | Ручной тест | Автотест |
|--------|-------|-------------|----------|
| BUG-01 — перевод 0 ₽ | [#1](https://github.com/Klyukvin-Dmitriy/test_f_bank/issues/1) | TC-03 | `tests/test_bug_01_zero_amount.py` |
| BUG-02 — отрицательная сумма | [#2](https://github.com/Klyukvin-Dmitriy/test_f_bank/issues/2) | TC-04 | `tests/test_bug_02_negative_amount.py` |
| BUG-03 — USD сверх баланса | [#3](https://github.com/Klyukvin-Dmitriy/test_f_bank/issues/3) | TC-05 | `tests/test_bug_03_overdraft_usd.py` |

Копии баг-репортов в репозитории: `docs/bug-reports/BUG-01.md`, `BUG-02.md`, `BUG-03.md`.

Если Issues ещё не созданы, выполните один раз (нужен `gh auth login`):

```powershell
.\scripts\create_github_issues.ps1
```

## 3) Автотесты (pytest + Selenium)

### Установка

```bash
python -m pip install -r requirements.txt
```

Примечание: драйвер браузера подбирается автоматически через Selenium Manager (встроен в Selenium 4), поэтому отдельно ставить ChromeDriver не нужно.

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

