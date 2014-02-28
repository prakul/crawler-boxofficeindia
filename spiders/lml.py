from scrapy.spider import BaseSpider 
from scrapy.http import Request,FormRequest,Response
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.spiders.crawl import CrawlSpider,Rule
from scrapy.contrib.spiders.init import InitSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.loader.processor import Join, MapCompose,TakeFirst

from boxOffice.items import *

class LivingSocialSpider(CrawlSpider):
    name="boxOffice"
    allowed_domains = [
    "boxofficeindia.com"
    ]
    login_page =  "http://www.boxofficeindia.com/Years/years_detail/2012"
    start_urls = [
   
    "http://www.boxofficeindia.com/Years/years_detail/2012"
    #login_page
    ]
    
    rules = (
    
    #Rule(SgmlLinkExtractor(allow=('/Boxoffice',)),follow=True),
    #Rule(SgmlLinkExtractor(allow=('/Years/years_detail/2014',))),
    Rule(SgmlLinkExtractor(allow=('movie_detail')),callback='myparse',follow=True),

    )
      
                   
    mov_fields = {'title':'.//div[@class="title4"]/a/text()',
    'rel_date':'//div[@id="detailed"]//span/ul/li[1]//td[2]/b/text()',
    'genre':'//div[@id="detailed"]//span/ul/li[2]//td[2]/a/b/text()',
    'run_time':'//div[@id="detailed"]//span/ul/li[3]//td[2]/b/text()',
    'budget':'//div[@id="detailed"]//span/ul/li[4]//td[2]/b/text()',
    'screens':'//div[@id="detailed"]//span/ul/li[5]//td[2]/b/text()',
    'footfalls':'//div[@id="detailed"]//span/ul/li[6]//td[2]/b/text()',
    'dis_share':'//div[@id="detailed"]//span/ul/li[7]//td[2]/b/text()',
    'total_gross':'//div[@id="detailed"]//span/ul/li[8]//td[2]/b/text()',
    'total_nett_gross':'//div[@id="detailed"]//span/ul/li[9]//td[2]/b/text()',
    #'link':'.//div[@class="details"]//td/b/text()'
     'link':'.//div[@id="detailed"]//span/ul/li[9]//td[2]/b/text()'
	}
	
    def start_requests(self):
        return self.init_request()
	    
    def init_request(self):
        print 'init_request'
        return [Request(url=self.login_page,callback=self.login)]
	
    def login(self,response):
        print 'login'
        return FormRequest.from_response(response,formnumber =1,
	    formdata={'loginUname':'nitin.agarwal@hindustantimes.com','loginUpass':'lasersoft123'},
	    callback = self.check_login_response)
	    
    def check_login_response(self,response):
        print "login response"
        if "Logout" in response.body:
            print "bitchP0Lease"
            for url in self.start_urls:
                yield self.make_requests_from_url(url)
            #return Request("http://www.boxofficeindia.com/Years/years_detail/2014",callback=self.Red)
            
        else:
            self.file = open('dump2.html','wb')
            self.file.write(response.body)
            
            print "bitchPLease"
            return
	

        
   # def parse(self,response):
    #    sel = HtmlXPathSelector(response)
     #   l = sel.select('//div[@class="images"]/a')
      #  for i in l:
       #     j = i.select('.//a')
            
        #        for iter in j:
         #           self.myparse(Request(iter.select(
                
            
            
    def myparse(self,response):
        print "myParse"
        selector = HtmlXPathSelector(response)
       # l = selector.select(self.deals_list_xpath)
        l = selector.select('//div[@id="detailed"]')
        ll = l.select('.//div[@class="title4"]/a/text()').extract()
        open(ll[0].strip()+'.html','wb').write(response.body)
        print ll[0].strip()
        for deal in l:
            
            #loader = XPathItemLoader(LivingSocialDeal(),selector=deal)
            loader = XPathItemLoader(MoviesClass() , selector=deal)
            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_output_processor = Join()
            loader.default_output_processor = TakeFirst()
            
            for field,xpath in self.mov_fields.iteritems():
                loader.add_xpath(field,xpath)
                x = deal.select(field).extract()            
            yield loader.load_item()
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            