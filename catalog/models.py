"""
File: models.py
"""

from django.db import models
from django.urls import reverse
import uuid 

class Genre(models.Model):
    """
    Repraesentiert ein Buch-Genre
    """
    name = models.CharField(max_length=200, help_text="Legt das sog. Genre fest (z.B. Sachbuch, Krimi, Science Fiction usw.)")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
        
class Book(models.Model):
    """
    Repräsentiert ein Buch (aber nicht ein einzelnes physikalisches Buch)
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    summary = models.TextField(max_length=1000, help_text='Eine kurze Beschreibung - max. 1000 Zeichen')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Zeichen mehr unter <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text='Das Genre zu dem das Buch gehört')
    language = models.CharField(max_length=64)
    yearPublished = models.IntegerField(default=0)
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    
    def __str__(self):
        """
        Zeichenkette, die eine Bezeichnung für das Objekt zurückgibt.
        """
        return self.title
    
    def get_absolute_url(self):
        """
        Gibt die Url zurück, über die Details zum Buch abgerufen werden.
        """
        return reverse('book-detail', args=[str(self.id)])

class BookInstance(models.Model):
    """
    Repräsentiert ein einzelne Kopie eines Buches (die ausgeliehen werden kann)
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Eindeutige ID für dieses Buch")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True) 
    imprint = models.CharField(max_length=200)
    dueBack = models.DateField(null=True, blank=True)
    currentPrice = models.DecimalField(max_digits=10, decimal_places=10)

    LOAN_STATUS = (
        ('m', 'Instandhaltung'),
        ('o', 'Ausgeliehen'),
        ('a', 'Verfuegbar'),
        ('r', 'Reserviert'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Buch-Verfügbarkeit')

    class Meta:
        ordering = ["dueBack"]
        

    def __str__(self):
        """
        Zeichenkette, die eine Bezeichnung für das Objekt zurückgibt.
        """
        return '{0} ({1})'.format(self.id, self.book.title)


class Author(models.Model):
    """
    Repraesentiert einen Autor.
    """
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    birthDate = models.DateField(null=True, blank=True)
    deathDate = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ["lastName","firstName"]
    
    def get_absolute_url(self):
        """
        Liefert die url, ueber die eine Instanz eines Autors angesprochen wird
        """
        return reverse('author-detail', args=[str(self.id)])
    
    def __str__(self):
        """
        Zeichenkette, die eine Bezeichnung für das Objekt zurückgibt.
        """
        return '{0}, {1}'.format(self.lastName,self.firstName)
