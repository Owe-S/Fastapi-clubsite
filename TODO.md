# To-Dos

## 1. News
- [ ] Define Pydantic schemas in `schemas.py`  
  • NewsArticleBase, NewsArticleIn, NewsArticleOut  
  • NewsPluginsIn/Out, NewsBulletinIn/Out, NewsKeywordIn/Out  
- [ ] Scaffold `routers/news.py` with CRUD endpoints and sub-routes  
- [ ] Wire `news_router` into `main.py` with JWT deps  
- [ ] Write unit tests under `tests/news_test.py`

## 2. Activities
- [ ] Extend schemas: ActivitiesBase/In/Out, ActivitiesDateTime, ActivitiesList, Participants, Pricing  
- [ ] Scaffold `routers/activities.py` (you have most stubs; fill in missing parts)  
- [ ] Wire router in `main.py` (already included)  
- [ ] Add tests in `tests/activities_test.py`

## 3. Images
- [ ] Define `ImageBase/In/Out` schemas and specialized image-table schemas  
- [ ] Scaffold `routers/images.py` with CRUD for Images & each specialized table  
- [ ] Include in `main.py` with JWT deps  
- [ ] Tests in `tests/images_test.py`

## 4. Articles
> (no standalone table; use News module)

## 5. Pages
- [ ] Schemas: PageBase/In/Out, PageMenu, PagePlugin  
- [ ] Scaffold `routers/pages.py` with CRUD + sub-routes  
- [ ] Include in `main.py`  
- [ ] Tests in `tests/pages_test.py`

## 6. Blog
- [ ] Schemas: BlogBase/In/Out, BlogComment, BlogImage, Blogger  
- [ ] Scaffold `routers/blog.py`  
- [ ] Wire in `main.py`  
- [ ] Tests in `tests/blog_test.py`

## 7. Calendar
- [ ] Schema: CalendarEntryIn/Out  
- [ ] Scaffold `routers/calendar.py`  
- [ ] Include in `main.py`  
- [ ] Tests in `tests/calendar_test.py`

## 8. Forms
- [ ] Schemas: FormType, FormField, FormReceived  
- [ ] Scaffold `routers/forms.py`  
- [ ] Include in `main.py`  
- [ ] Tests in `tests/forms_test.py`

## 9. Orders & Cart
- [ ] Schemas: CartItem, OrderDetail, Order  
- [ ] Scaffold `routers/cart.py` and `routers/orders.py`  
- [ ] Include both in `main.py`  
- [ ] Tests in `tests/cart_test.py` and `tests/orders_test.py`

---

Once these stubs are in place, populate each handler, wire validators, commit and review via unit tests before moving to the next module.// filepath: c:\FastAPI-Clubsite\TODO.md

# To-Dos

## 1. News
- [ ] Define Pydantic schemas in `schemas.py`  
  • NewsArticleBase, NewsArticleIn, NewsArticleOut  
  • NewsPluginsIn/Out, NewsBulletinIn/Out, NewsKeywordIn/Out  
- [ ] Scaffold `routers/news.py` with CRUD endpoints and sub-routes  
- [ ] Wire `news_router` into `main.py` with JWT deps  
- [ ] Write unit tests under `tests/news_test.py`

## 2. Activities
- [ ] Extend schemas: ActivitiesBase/In/Out, ActivitiesDateTime, ActivitiesList, Participants, Pricing  
- [ ] Scaffold `routers/activities.py` (you have most stubs; fill in missing parts)  
- [ ] Wire router in `main.py` (already included)  
- [ ] Add tests in `tests/activities_test.py`

## 3. Images
- [ ] Define `ImageBase/In/Out` schemas and specialized image-table schemas  
- [ ] Scaffold `routers/images.py` with CRUD for Images & each specialized table  
- [ ] Include in `main.py` with JWT deps  
- [ ] Tests in `tests/images_test.py`

## 4. Articles
> (no standalone table; use News module)

## 5. Pages
- [ ] Schemas: PageBase/In/Out, PageMenu, PagePlugin  
- [ ] Scaffold `routers/pages.py` with CRUD + sub-routes  
- [ ] Include in `main.py`  
- [ ] Tests in `tests/pages_test.py`

## 6. Blog
- [ ] Schemas: BlogBase/In/Out, BlogComment, BlogImage, Blogger  
- [ ] Scaffold `routers/blog.py`  
- [ ] Wire in `main.py`  
- [ ] Tests in `tests/blog_test.py`

## 7. Calendar
- [ ] Schema: CalendarEntryIn/Out  
- [ ] Scaffold `routers/calendar.py`  
- [ ] Include in `main.py`  
- [ ] Tests in `tests/calendar_test.py`

## 8. Forms
- [ ] Schemas: FormType, FormField, FormReceived  
- [ ] Scaffold `routers/forms.py`  
- [ ] Include in `main.py`  
- [ ] Tests in `tests/forms_test.py`

## 9. Orders & Cart
- [ ] Schemas: CartItem, OrderDetail, Order  
- [ ] Scaffold `routers/cart.py` and `routers/orders.py`  
- [ ] Include both in `main.py`  
- [ ] Tests in `tests/cart_test.py` and `tests/orders_test.py`

---

Once these stubs are in place, populate each handler, wire validators, commit and review via unit tests before moving to