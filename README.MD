# LMS

# Dodawanie feature w django:
1. Czy potrzebuje django apps?
2. Dodać do settings.py do INSTALLED_APPS.
3. Czy potrzebujemy modele? 
   - models.py
   - `python manage.py makemigrations <app_name>`
   - `python manage.py migrate <app_name>`
4. Czy potrzebujemy to w django admin? (CMS)
   - rejestrujemy modele w admin.py
5. Czy potrzebujemy formularze?
   - django forms w pliku forms.py
6. Czy potrzebujemy widok?
   - views.py
7. Czy potrzebujemy templatki?
   - w folderze templates/namespace/ tworzymy templatke
8. Lokalne urls.py
9. Dodanie do globalnych urls.py