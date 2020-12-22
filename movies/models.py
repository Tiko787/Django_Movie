from django.db import models
from datetime import date


class Category(models.Model):
    """категории"""
    name = models.CharField("категория", max_length=150)
    description = models.TextField("описание")
    url = models.SlugField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Actor(models.Model):
    """Актеры и режиссеры"""
    name = models.CharField("имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("описание")
    image = models.ImageField("изображение", upload_to="actors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актеры и режиссеры"
        verbose_name_plural = "Актеры и режиссеры"


class Genre(models.Model):
    """жанры"""
    name = models.CharField("имя", max_length=100)
    description = models.TextField("описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "жанр"
        verbose_name_plural = "жанры"


class Movie(models.Model):
    """фильм"""
    title = models.CharField("Називание", max_length=100)
    tagline = models.CharField("Слоган", max_length=100, default='')
    description = models.TextField("описание")
    poster = models.ImageField("постер", upload_to="movies/")
    year = models.PositiveSmallIntegerField("дата выхода", default=2019)
    country = models.CharField("Страна", max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name="режиссер", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="Актеры", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="жанры")
    world_premiere = models.DateField(default=date.today)
    budget = models.PositiveIntegerField("бюджет", default=0, help_text="указывать сумму в долларах")
    fees_in_usa = models.PositiveIntegerField("сбор в сша", default=0, help_text="указывать сумму в долларах")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("черновик", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "фильм"
        verbose_name_plural = "фильмы"


class MovieShots(models.Model):
    """кадри из фильма"""
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("описание")
    image = models.ImageField("изображение", upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name="фильм", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "кадри из фильма"
        verbose_name_plural = "кадри из фильма"


class RatingStar(models.Model):
    """звезда рейтинга"""
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "звезда рейтинга"
        verbose_name_plural = "звезда рейтинга"


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="фильм")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "рейтинг"
        verbose_name_plural = "рейтинги"


class Reviews(models.Model):
    """Отзивы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Собшение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Отзив"
        verbose_name_plural = "Отзивы"
