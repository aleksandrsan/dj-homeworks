
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


from .models import Article, Tag, Scope



class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        #Флаг наличия основного раздела
        isMainScope = False
        for form in self.forms:
            if form.cleaned_data.get('is_main') == True:
                if isMainScope == True:
                    raise ValidationError('Основным может быть только один раздел')
                else:
                    isMainScope = True


        if isMainScope == False:
            raise ValidationError('Укажите основной раздел')

        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass