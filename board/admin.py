from django.contrib import admin

# Register your models here.
from board.models import Board, Task

class TaskInline(admin.TabularInline):
	model = Task
	extra = 1

class BoardAdmin(admin.ModelAdmin):
	#when admin clicks on a board from many available boards
	fieldsets = [
		('Board Information', {'fields': ['name']}),
		('User Information', {'fields': ['user']}),
	]
	inlines = [TaskInline]	


	#when admin chooses a model out of many from homepage 
	list_display = ('name','user')
	search_fields = ['name']
	list_filter = ['name']


admin.site.register(Board, BoardAdmin)