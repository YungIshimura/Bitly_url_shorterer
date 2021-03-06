## Обрезка ссылок с помощью Битли
Программа для сокращения URL (битлинка) и получения количества переходов по битлинку. Программа взаимодействует с сервисом [Bitly.com](https://bitly.com) через API-ключ.
Вот в качестве примера битлинк на [google.com](https://www.google.com/) [bit.ly/3whhj2H](https://bit.ly/3whhj2H).
### Как установить
Для начала необходимо зарегистрироваться на сервисе [Bitly](https://bitly.com) и сгенерировать токен [(гайд по генерации необходимого ключа)](https://support.bitly.com/hc/en-us/articles/230647907-How-do-I-generate-an-OAuth-access-token-for-the-Bitly-API-).
Сохранять такую информацию публично плохая идея. Потому все чувствительные данные стоит скрыть. Для этого в корне репозитория нужно создать ```.env``` файл и поместить ключ туда, прописав:
```python 
BITLY_API_KEY='Ваш API-ключ'
```

В самом коде это выглядит так:
``` python
API_KEY = os.getenv('BITLY_API_KEY')
```
В проекте используется пакет [python-dotenv](https://github.com/theskumar/python-dotenv). Он позволяет загружать переменные окружения из файла .env в корневом каталоге приложения.
Этот .env-файл можно использовать для всех переменных конфигурации.

Далее необходимо, чтобы Python3 был уже установлен затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```python
pip install -r requirements.txt
```
### Как пользоваться
В командной строке переходите к расположению файла, прописываете команду :
```python
python main.py ссылка(и) 
```  
и получаете битлинк или же количество переходов по нему (в зависимости от того, что было введено).

