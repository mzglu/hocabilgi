import scrapy


class HocabilgiSpider(scrapy.Spider):
    name = 'hocabilgi'
    allowed_domains = ['ercanbulus.cv.nku.edu.tr']
    start_urls = ['http://ercanbulus.cv.nku.edu.tr/',
                    'http://erdincuzun.cv.nku.edu.tr/',
                    'http://eozhan.cv.nku.edu.tr/',
                    'http://asaygili.cv.nku.edu.tr/',
                    'http://vatalay.cv.nku.edu.tr/',
                    'http://pkaya.cv.nku.edu.tr/',
                    'http://ucetin.cv.nku.edu.tr/',
                    'http://btasdelen.cv.nku.edu.tr/',
                    'http://fuysal.cv.nku.edu.tr/',
                    'http://gkaykioglu.cv.nku.edu.tr/',
                    'http://bozlusen.cv.nku.edu.tr/',
                    'http://aakyildiz.cv.nku.edu.tr/',
                    'http://aozmutlu.cv.nku.edu.tr/',
                    'http://vakyuncu.cv.nku.edu.tr/',
                    'http://uakyol.cv.nku.edu.tr/',
                    'http://nonturk.cv.nku.edu.tr/',
                    'http://cunal.cv.nku.edu.tr/',
                    'http://ubilen.cv.nku.edu.tr/',
                    'http://gpekkan.cv.nku.edu.tr/'
                    


                    ]


    custom_settings={
        'FEED_URI':'veriler.json',
        'FEED_FORMAT':'json'
                }                

    def parse(self, response):

        tablo=response.xpath('.//div[@class="col-md-9"]')
        satirlar=tablo.xpath('.//div[@id="myTabContent"]')
        unvan_isim=satirlar.xpath('.//div[@class="panel-body"]/p/text()').extract_first()
        ogrenimanasayfa=satirlar.xpath ('.//div[@id="anasayfa"] // tr ')
        birim=ogrenimanasayfa.xpath (' td // text () ') [2] .extract ()
        bolum=ogrenimanasayfa.xpath (' td // text () ') [5] .extract ()
        ogrenimbilgi=satirlar.xpath ('.//div[@id="ogrenimbilgileri"] // tr ')
        uni_lisans=ogrenimbilgi.xpath (' td // text () ') [32] .extract ()
        bolum_lisans=ogrenimbilgi.xpath (' td // text () ') [38] .extract ()
        yıl_lisans=ogrenimbilgi.xpath (' td // text () ') [41] .extract ()
        ingilizce_seviye=ogrenimbilgi.xpath (' td // text () ') [46] .extract ()
        akademik_gorevsayısı=len(satirlar.xpath ('.//div[@id="akademikgorevler"] // tr '))
        idari_gorevsayısı=len(satirlar.xpath ('.//div[@id="idarigorevler"] // tr '))
        unidisideneyim_sayısı=len(satirlar.xpath ('.//div[@id="unidisideneyim"] // tr '))
        yayin_sayısı=len(satirlar.xpath ('.//div[@id="yayinlar"] // tr '))



        yield{'Unvan_İsim':unvan_isim,
                  'Birimi':birim,
                  'Bolum':bolum,
                  'Univeriste_Lİsans':uni_lisans,
                  'Bolum_Lisans':bolum_lisans,
                  'Yıl_Lisans':yıl_lisans,
                  'İngilizce_Seviye':ingilizce_seviye,
                  'Akademik_Görev_Sayısı':akademik_gorevsayısı,
                  'İdari_Görev_Sayısı':idari_gorevsayısı,
                  'Universite_Dısı_Deneyim_Sayısı':unidisideneyim_sayısı,
                  'Yayınlanan_Makale_Sayısı':yayin_sayısı}

   