from django.contrib import admin
from polls.models import Choice, Question
#from mysite.polls.models import Author

#class ChoiceInline(admin.TabularInline):
#    model = Choice
#    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    #inlines = [ChoiceInline]
#class AuthorAdmin(admin.ModelAdmin):
#    pass
admin.site.register(Question,QuestionAdmin)
