# Проект OnlineStoreProject
Проект интернет магазина

## Описание:
Магазин предствляет из себя каталог товаров разбитых на категории.
С функционалом добавлять, редактировать и удалять как категории,
так и товары.
Пользователи регистрируются, авторизуются. Есть возможность 
редактировать профиль.

## Установка:
1. Клонируйте репозиторий:
```commandline
git clone https://github.com/AndreySapeshko/OnlineStoreProject.git
```
2. Установите зависимости:
```commandline
pip install -r requirements.txt
```
## Тестирование:

## Использование:

## Документация:
### Приложение Catalog
Модели:
1. Класс описывающий модель Category (категория товаров)
2. Класс описывающий модель Product

Формы:
1. ProductForm - Класс описывающий форму для регистрации и редактирования Product
2. CategoryForm - Класс описывающий форму создания и редактирования Category

Представления:
1. HomeView - Класс описывающий представление страницы catalog/home.html
2. ContactsView - Класс описывающий представление страницы catalog/contacts.html
3. ProductDeleteView - Класс описывающий представление страницы catalog/product_confirm_delete.html удаление продукта
4. ProductListView - Класс описывающий представление страницы catalog/product_list.html
5. ProductUpdateView - Класс описывающий представление страницы catalog/product_form.html редактирование продукта
6. ProductCreateView - Класс описывающий представление страницы catalog/product_form.html создание продукта
7. ProductDetailView - Класс описывающий представление страницы catalog/product_detail.html
8. CategoryCreateView - Класс описывающий представление страницы catalog/category_list.html
9. CategoryDetailView - Класс описывающий представление страницы catalog/category_detail.html
10. CategoryUpdateView - Класс описывающий представление страницы catalog/category_form.html редактирование категории
11. CategoryDeleteView - Класс описывающий представление страницы catalog/category_confirm_delete.html удаление категории

Шаблоны:
1. base.html
2. navbar.html
3. category_confirm_delete.html
4. category_detail.html
5. category_form.thml
6. category_list.html
7. contacts.html
8. home.html
9. product_confirm_delete.html
10. product_detail.html
11. product_form.html
12. product_list.html

### Приложение blog
Модели:
1. Post - Класс описывающий сообщение в блоге

Представления:
1. PostCreateView - Класс описывающий представление страницы blog/post_form.html создание сообщения
2. PostListView - Класс описывающий представление страницы blog/post_list.html
3. PostDetailView - Класс описывающий представление страницы blog/post_detail.html
4. PostUpdateView - Класс описывающий представление страницы blog/post_form.html редактирование поста
5. PostDeleteView - Класс описывающий представление страницы blog/post_confirm_delete.html удаление поста

Шаблоны:
1. post_confirm_delete.html
2. post_detail.html
3. post_form.html
4. post_list.html

### Приложение users

Модели:
1. CustomUser - Класс описывающий модель пользователя

Формы:
1. BaseUserForm - Родительский класс с общим для многих форм методом добавляющем стили форме
2. CustomUserCreationForm - Класс описывающий форму регистрации нового пользователя
3. UserUpdateForm - Класс описывающий форму редактирования профиля пользователя

Представления:
1. RegisterView - Класс описывающий представление страницы users/register.html
2. UserUpdateView - Класс описывающий представление страницы users/user_form.html редактирования профиля
3. UserDetailView - Класс описывающий представление страницы users/user_detail.html


## Логирование

## Лицензия: