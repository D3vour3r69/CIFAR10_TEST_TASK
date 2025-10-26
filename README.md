# CIFAR-10 Классификатор изображений на API

FastAPI приложение, с классификатором изображений на CIFAR-10 дата сете. Для 10 классов изображений с точностью 94%.

##  Основная информация по модели

- **Точность на тесте**: 94.0%
- **Готовая архитектура модели**: ResNet-18
- **Датасет**: CIFAR-10 (60,000 изображений)

### Classification Report

Метрики для текущей модели: 

              precision    recall  f1-score   support

           0       0.95      0.94      0.95      1000
           1       0.96      0.97      0.97      1000
           2       0.92      0.92      0.92      1000
           3       0.88      0.87      0.87      1000
           4       0.94      0.96      0.95      1000
           5       0.91      0.90      0.90      1000
           6       0.96      0.96      0.96      1000
           7       0.96      0.95      0.96      1000
           8       0.96      0.96      0.96      1000
           9       0.95      0.96      0.96      1000

    accuracy                           0.94     10000
    macro avg      0.94      0.94      0.94     10000
    weighted avg   0.94      0.94      0.94     10000

Test accuracy: 0.9396

### Confusion Matrix
![Confusion Matrix](/confusion_matrix.png)

### Графики обучения
![Graph](/grapf.png)
Возможно присутствует небольшое переобучение. Старался минимизировать это, аугментациями и scheduler'ом
##  Как запустить проект

### Требования
- Git with [Git LFS](https://git-lfs.com). В соврменном гите встроен по умолчанию.
- Python 3.9+(Локально) or Docker
- [Poetry](https://python-poetry.org)

### Используем докер
#### 1 Способ(Через контейниризацию):
```bash
# 1. Клонируйте репозиторий
git clone https://github.com/D3vour3r69/CIFAR10_TEST_TASK
# Зайдите в папку с репозиторием
cd CIFAR10_TEST_TASK
# 2. Собираем и запускаем докер образ
docker build -t cifar10-api .
docker run -p 8000:8000 cifar10-api
```

##  Использование API
### Health Check(Проверка состояния программы)
```bash
curl http://localhost:8000/health
Response: {"status":"healthy"}
```
### Получить классы в датасете
```bash
curl http://localhost:8000/classes
```
### Классифицировать изображение
```bash
curl -X POST -F "file=@название_вашего_файла.jpg" http://localhost:8000/predict
```
## Более простое использование API
Зайти по адресу localhost:8000/docs
- **Зайти по адрессу localhost:8000/docs**
- **Выбрать вкладку predict**
- **Нажать try it out**
- **Загрузить картинку, можно просто перетащить на окно**
- **Получить предсказание модели**

# Если хотите использовать локально
```bash
git clone https://github.com/D3vour3r69/CIFAR10_TEST_TASK
cd CIFAR10_TEST_TASK
git lfs install && git lfs pull
poetry install
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```


