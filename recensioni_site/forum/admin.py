from django.contrib import admin
from .models import Sezione,SezioneImage

class SezioneModelAdmin(admin.ModelAdmin):
    model = Sezione
    list_display = ["nome_sezione", "descrizione"]

class SezioneImageAdmin(admin.StackedInline):
    model = SezioneImage
    
@admin.register(Sezione)
class PropertyAdmin(admin.ModelAdmin):
    inlines = [ SezioneImageAdmin ]

    class Meta:
        model = Sezione


@admin.register(SezioneImage)
class SezioneImageAdmin(admin.ModelAdmin):
    pass


