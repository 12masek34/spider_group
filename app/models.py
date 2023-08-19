from django.db.models import (
    CASCADE,
    CharField,
    ForeignKey,
    ManyToManyField,
    Model,
    PositiveIntegerField,
)


class BaseModel(Model):
    """Базовый класс для всех моделей у которых есть поле name."""

    name = CharField("Название", max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.__class__.__name__}(name={self.name})"


class District(BaseModel):

    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Районы"


class Category(BaseModel):

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"



class Product(BaseModel):
    category = ForeignKey(Category, on_delete=CASCADE, verbose_name="Категория")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class ProductPrice(Model):
    product = ForeignKey(Product, on_delete=CASCADE, verbose_name="Продукт")
    price = PositiveIntegerField("Цена")

    class Meta:
        verbose_name = "Цена товара"
        verbose_name_plural = "Цена товаров"

    def __str__(self):
        return f"{self.__class__.__name__}(product={self.product.name}, price={self.price})"


class NetworkEnterprise(BaseModel):

    class Meta:
        verbose_name = "Сеть предприятий"
        verbose_name_plural = verbose_name


class Enterprise(BaseModel):
    network = ForeignKey(
        NetworkEnterprise,
        on_delete=CASCADE,
        related_name="enterprises",
        verbose_name="Сеть предприятий"
    )
    district = ManyToManyField(
        District,
        related_name="enterprises",
        verbose_name='Районы'
    )
    product = ManyToManyField(
        Product,
        related_name="enterprises",
        verbose_name="Продукты"
    )

    class Meta:
        verbose_name = "Предприятие"
        verbose_name_plural = "Предприятия"
