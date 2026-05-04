# Чек-лист соответствия заданию

## Ручное тестирование
- **5 тестов**: `docs/manual-tests.md` ✅
- **Минимум 2 дефекта найдены**: найдено 3 (BUG-01..BUG-03) ✅

## Баг-репорты
- **BUG-01**: `docs/bug-reports/BUG-01.md` ✅
- **BUG-02**: `docs/bug-reports/BUG-02.md` ✅
- **BUG-03**: `docs/bug-reports/BUG-03.md` ✅

## Автоматизация
- **По автотесту на каждый дефект** ✅
  - BUG-01 → `tests/test_bug_01_zero_amount.py`
  - BUG-02 → `tests/test_bug_02_negative_amount.py`
  - BUG-03 → `tests/test_bug_03_overdraft_usd.py`
- **CI в GitHub Actions**: `.github/workflows/ci.yml` ✅
- **Итоговая сборка красная**: тесты написаны под ожидаемое корректное поведение, но текущая версия приложения содержит дефекты → `pytest` падает ✅

## Для сдачи
- Сделать репозиторий публичным на GitHub ✅
- Загрузить ссылку на репозиторий в личный кабинет ✅

