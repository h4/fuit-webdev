# Список авторов и карточка автора

Создайте представления и шаблоны для отображения списка авторов и карточки автора.

Список авторов должен открываться по ссылке `/library/authors/`. На странице отображается список вида «Имя Фамилия». Каждый элемент списка представляет собой ссылку на страницу карточки соответствующего автора.

Карточка автора должна открываться по ссылке `/library/authors/N/`, где N — первичный ключ в таблице `library_author`. На странице отображаются значения всех полей модели `Author`, кроме  первичного ключа модели.