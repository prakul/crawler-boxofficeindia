# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class LivingSocialDeal(Item):
    title = Field()
    description = Field()
    link = Field()
    location = Field()
    price = Field()
    
class MoviesClass(Item):
    title = Field()
    rel_date= Field()
    genre= Field()
    run_time= Field()
    budget= Field()
    screens= Field()
    footfalls= Field()
    dis_share= Field()
    total_gross= Field()
    total_nett_gross= Field()
    link =   Field()