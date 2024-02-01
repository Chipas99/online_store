from app.catalog.models import Category

# Создание новых категорий
Category.objects.create(name='Category 1')
Category.objects.create(name='Category 2')
Category.objects.create(name='Category 3')

# Получение списка всех категорий
all_categories = Category.objects.all()
print(all_categories)

# Применение произвольных фильтров
filtered_categories = Category.objects.filter(name__icontains='2')
print(filtered_categories)
