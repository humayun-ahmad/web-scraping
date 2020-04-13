

# =============================================================================
# from yandex import Translater
# tr = Translater()
# 
# tr.set_key("api key here")
# tr.set_text("Hello World") 
# tr.set_from_lang('en')
# tr.set_to_lang('ru')
# 
# result = tr.translate()
# 
# print(result)
# =============================================================================
import array as ar
from yandex_translate import YandexTranslate
from csv import reader

api_key = [api_key1,api_key2]

# translate = YandexTranslate('api_key')

# =============================================================================
# print('Languages:', translate.langs)
# print('Translate directions:', translate.directions)
# print('Detect language:', translate.detect('Hello,world!'))
# print('Translate:', translate.translate('Привет, мир!', 'ru-en'))  # or just 'en'
# =============================================================================


file = open("output.csv", 'w')
with open('input.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    i = 0
          
    for row in csv_reader:
        
        translate = YandexTranslate(api_key[i])
        
        try:
            result = translate.translate(row, 'en-es') #english to spanish
            tx = result['text']
            result = translate.translate(tx, 'es-de') # spanish to German
            tx = result['text']
            result = translate.translate(tx, 'de-en') # German to english
            file.write(str(result['text']) + "\n")
            if i==0:
                i = 1
            else:
                i = 0
        
        except:
            print("ERR_DAILY_CHAR_LIMIT_EXCEEDED")
file.close()



# =============================================================================
# file = open("output.csv", 'w')
# with open('input.csv', 'r') as read_obj:
#     csv_reader = reader(read_obj)
#     
#     for row in csv_reader:
#         result = translate.translate(row, 'en-es') #english to spanish
#         tx = result['text']
#         result = translate.translate(tx, 'es-de') # spanish to German
#         tx = result['text']
#         result = translate.translate(tx, 'de-en') # German to english
#         file.write(str(result['text']) + "\n")
# 
# file.close()
# 
# =============================================================================
