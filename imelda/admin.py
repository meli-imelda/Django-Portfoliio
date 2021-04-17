from django.contrib import admin

# Register your models here.
from .models import Home, About, Profile, Category, Skills, Portfolio


# Home
admin.site.register(Home) #adds home to the admin 


# About
class ProfileInline(admin.TabularInline):  #tells us that the profile will be inline with the about section
    model = Profile
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
     inlines = [
        ProfileInline,
    ]

# Skills
class SkillsInline(admin.TabularInline):  #this will be displayed inline with the catgory section
    model = Skills
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     inlines = [
        SkillsInline,
    ]


# Portfolio
admin.site.register(Portfolio)