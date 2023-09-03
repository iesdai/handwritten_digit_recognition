import requests

# указываем путь к фотографии, для которой нужно предсказание
files = {'img': open(r'/Users/dasha/Desktop/six.png', 'rb')}
# отправляем запрос, чтобы получить предсказание
r = requests.post('http://127.0.0.1:8000/predict/', files=files)
# выводим статус запроса
print(r)
