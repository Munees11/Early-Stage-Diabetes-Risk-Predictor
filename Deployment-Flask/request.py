import requests

url = 'http://localhost:500/predict_api'
r = requests.post(url,json={'Age':45, 'Gender':1, 'Polyuria':0, 'Polydipsia':1, 'sudden weight loss':1,
       'weakness':0, 'Polyphagia':0, 'Genital thrush':1, 'visual blurring':1,
       'Itching':1, 'Irritability':0, 'delayed healing':1, 'partial paresis':0,
       'muscle stiffness':0, 'Alopecia':1, 'Obesity':1})

print(r.json())