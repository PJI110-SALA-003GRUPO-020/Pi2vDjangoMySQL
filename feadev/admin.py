from django.contrib import admin
admin.site.site_header = 'Administração do site'
from .models import Contato, Membro, Categoria, Subcategoria, Gestão
from django.utils.html import format_html



admin.site.register(Contato)
actions = ['mark_as_read', 'mark_as_unread']
admin.site.add_action('mark_as_read', 'Marcar como lido')
admin.site.add_action('mark_as_unread', 'Marcar como não lido')




class MembroAdmin(admin.ModelAdmin):
    actions = ['ativar_membros', 'desativar_membros']
    list_filter = ['categoria', 'sub_categoria', 'ativo', 'inativo','ano']
    list_display = ['nome', 'categoria', 'sub_categoria', 'status', 'imagem_thumbnail']
    search_fields = ['nome']

    def ativar_membros(self, request, queryset):
        queryset.update(ativo=True)
        request.session['ativo'] = True

    def desativar_membros(self, request, queryset):
        queryset.update(ativo=False)
        request.session['inativo'] = False

    def imagem_thumbnail(self, obj):
        return format_html('<img src="{}" width="40" height="40" />', obj.imagem.url)

    imagem_thumbnail.short_description = 'Imagem'

    

    def status(self, obj):
        if obj.ativo:
            return 'Ativo'
        elif obj.inativo:
            return 'Inativo'
        else:
            return 'N/A'

    status.short_description = 'Status'

admin.site.register(Membro, MembroAdmin)




class GestãoAdmin(admin.ModelAdmin):
    list_filter = ['nome', 'categoria']
    list_display = ['nome', 'categoria', 'linkedin', 'github', 'imagem_thumbnail']
    search_fields = ['nome']
    def imagem_thumbnail(self, obj):
        return format_html('<img src="{}" width="40" height="40" />', obj.imagem.url)

    imagem_thumbnail.short_description = 'Imagem'

admin.site.register(Gestão, GestãoAdmin)





admin.site.register(Categoria)
admin.site.register(Subcategoria)