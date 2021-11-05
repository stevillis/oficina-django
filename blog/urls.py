from django.urls import path

from blog.views import inserir_categoria, visualizar_categorias, editar_categoria, excluir_categoria, index

urlpatterns = [
    path('', index, name='index'),
    path('inserir_categoria/', inserir_categoria, name='inserir_categoria'),
    path('visualizar_categorias/', visualizar_categorias, name='visualizar_categorias'),
    path('editar_categoria/<int:id>', editar_categoria, name='editar_categoria'),
    path('excluir_categoria/<int:id>', excluir_categoria, name='excluir_categoria'),
]
