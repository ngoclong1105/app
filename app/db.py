
from .models import Comic,Comment

def getProducts(keyword):
    phrase = '%' + keyword + '%'
    return Comic.objects.raw('SELECT * FROM app_comic WHERE name LIKE %s OR code LIKE %s', [phrase, phrase])

def findProductById(id):
    return Comic.objects.get(pk=id)

def deleteProduct(id):
    product = findProductById(id)
    if product:
        product.delete()
def addComment(cmt,username):
    return Comment.objects.create(reply=cmt,name=username)





