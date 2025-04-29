from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
def product_list(request, category_slug = None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available = True)
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        products = products.filter(category = category)
    return render(request, 'start_django/list.html',
                  {'category':category,
                          'categories':categories,
                          'products': products
                   })
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id = id, slug = slug, available = True)
    cart_product_form = CartAddProductForm()
    return render(request, 'start_django/detail.html',
                  {'product': product,
                   'cart_product_form':cart_product_form
    })




'''
scheme - схема запросов
body - тело запроса ввиде строки байтов
method - метод запросов GET POST
encoding - кодировка
content_type -тип содержимого запроса (значение заголовка CONTENT_TYPE)
GET - объект ввид словаря, который содержит параметры запроса GET
ROST - объект ввиде словаря, который содержит параметры запроса POST
COOKIES -отправленные клиентом куки
FILES - отправленные клиентом файлы
META - хранит все заголовки http в виде словаря


'''



''' host = request.META['HTTP_HOST']
        user_agent = request.META['HTTP_USER_AGENT']
        path = request.path
        return HttpResponse(f'#<p>HOST: {host} </p>
                                #<p>user_agent: {user_agent} </p>
                                #<p>path: {path} </p>
                                ')
'''
    #return HttpResponse('Заголовок', headers={'SecretCode': '183469'})
    #return HttpResponse('Ошибка', status = 404, reason = 'Incorrect data')


