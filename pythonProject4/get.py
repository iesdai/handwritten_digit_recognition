import json
import requests
from PIL import Image
import io

# извлекаем данные об всех предсказаниях
r = requests.get('http://127.0.0.1:8000/predict/')
# преобразовываем данные в формат JSON
s = json.loads(r.text)
for i in range(len(s)):
    # для каждого из них извлекаем данные со страницы фотографии
    asa = requests.get('http://127.0.0.1:8000{}'.format(s[i]['img']))
    b_str = asa.content
    # открываем фотографию из байтовой строки
    image = Image.open(io.BytesIO(b_str))
    # сохряняем в папку
    image.save('/Users/dasha/PycharmProjects/pythonProject4/images/image{}.png'.format(i+1))
