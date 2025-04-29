# 📚 Ko‘p tilli Onlayn Kutubxona API

> Django REST Framework asosida qurilgan zamonaviy ko‘p tilli (🇺🇿 🇷🇺 🇺🇸) kutubxona API tizimi.

## 📌 Loyiha haqida

> Bu loyiha foydalanuvchilarga kitoblar, mualliflar va kategoriyalarni ko‘p tilda ko‘rish, 
> izlash va ularga baho berish imkonini beruvchi RESTful API tizimidir. Loyihada 
> `API versiyalash`, `ko‘p tillilik`, `qidiruv`, `reyting`, `sharhlar` va `kitob mavjudligi`
> kabi funksiyalar mavjud.

---

## 🚀 Texnologiyalar

- **Django 4.x**
- **Django REST Framework**
- **django-modeltranslation**
- **PostgreSQL**
- **Docker (opsional)**
- **Swagger (drf-yasg)**

---

## 🌐 Ko‘p tillilik

`django-modeltranslation` orqali quyidagi maydonlar tarjima qilinadi:

- Kitob nomi (`title`)
- Kitob tavsifi (`description`)
- Muallif ismi va bio
- Kategoriya nomi

📌 Qo‘llab-quvvatlanadigan tillar:

- `uz` – O‘zbekcha  
- `en` – Inglizcha  
- `ru` – Ruscha  

> Til tanlash uchun HTTP sarlavhasidan foydalaning:
---
## 🧩 API Versiyalash
### API versiyasi URL path versioning orqali aniqlanadi:
### | `/api/v1/`  | faqat joriy tildagi ma'lumotlar                         
### | `/api/v1/`  | barcha tillardagi ma'lumotlar va qo‘shimcha funksiyalar 

## 📖 API Endpointlar
## 📘 V1 (Minimal

### 🔑 Autentifikatsiya
| Endpoint                   | Metod | Tavsif                                 |
|----------------------------|------|----------------------------------------|
| `/api/v1/categories`       | GET  | Kategoriyalar ro‘yxatini olish         |
| `/api/v1/categories/{id}/` | GET  | Bitta kategoriyah                      |
| `/api/v1/authors/`         | GET  | Mualliflar ro‘yxati                    |
| `/api/v1/authors/{id}/`    | GET  | Bitta muallif                          |
| `/api/v1/books/`           | GET  | Kitoblar ro‘yxati (sahifalangan)       |
| `/api/v1/books/{id}/`      | GET  | Bitta kitob                            |
| `/api/v1/books/search/`    | GET  | Qidiruv (q, author, category, year)    |


### 🌟 V2 (Qo‘shimcha imkoniyatlar bilan)
| Endpoint                           | Metod | Tavsif                                    |
|------------------------------------|------|-------------------------------------------|
| `/api/v2/books/{id}/reviews/`      | GET  | Kitob sharhlari                           |
| `/api/v2/books/{id}/reviews/`      | POST | Sharh qo‘shish                            |
| `/api/v2/books/{id}/similar/`      | GET  | O‘xshash kitoblar                         |
| `/api/v2/books/{id}/availability/` | GET  | Kitob mavjudligi (mavjud, band, zahirada) |
| `/api/v2/books/top-rated/`         | GET  | Eng yaxshi baholangan kitoblar            |

---
### 🛠️ O‘rnatish
```bash
git clone https://github.com/Bunyodjon-Mamadaliyev/Online-library.git
cd Online-library
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

