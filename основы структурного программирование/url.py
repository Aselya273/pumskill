def get_absolute_url (url, *args, **kwargs):
    """
     Формирование URL адреса из переданного домена и параметра.
    :param url :  обязательный аргумент
    :param *args : позиционный аргумент
    :param **kwargs: именнованный аргумент 
    
    """ 
    for i in args:
        url+= f'/{i}'
       
    url += '?'
    
    for k, v in kwargs.items():
        
        url += f'{k}={v}&'
    
    url = url[:-1] 
        
    
    return url
        
        
print(get_absolute_url('www.yandex.ru', 'posts', 'news', id='24', author='admin'))
print(get_absolute_url('www.google.com', 'images', id='24', category='auto', color='red', size='small'))

# www.yandex.ru/posts/news?id=24&author=admin
# www.google.com/images?id=24&category=auto&color=red&size=small
