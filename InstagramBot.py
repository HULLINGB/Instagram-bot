from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random_words import RandomWords

import time
import random


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(5)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(2)

    def expand_photo(self):
        driver = self.driver
        select = driver.find_element_by_class_name("_9AhH0")
        select.click()

    def go_to_hashtag(self, hashtag):

        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)

    def like_photos(self, amount):
        driver = self.driver
        # gathering photos
        like = driver.find_element_by_class_name('v1Nh3')
        like.click()

        i = 1
        while i < amount:
            try:
                random2 = random.randint(1, 5)
                if(random2 == 1):
                    rand = random.randint(1, 500)
                    time.sleep(rand)
                    driver.find_element_by_class_name('fr66n').click()
                    driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
                    i += 1

                if (random2 == 4):
                    rand = random.randint(1, 30)
                    time.sleep(rand)
                    driver.find_element_by_class_name('fr66n').click()
                    driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
                else:
                    print("")
            except:
                print("")

    def auto_comment(self, content):
        time.sleep(3)
        driver = self.driver
        comment = driver.find_element_by_xpath("//textarea[contains(@placeholder, 'Add a comment')]")
        comment.send_keys(content)

usernames = ['USERNAME']

i = 0
j = 0
username = random.choice(usernames)
password = "PASSWORD"
ig = InstagramBot(username, password)
ig.login()

hashtags = ['amazing', 'beautiful', 'adventure', 'photography', 'nofilter',
                'newyork', 'artsy', 'alumni', 'lion', 'best', 'fun', 'happy',
                'art', 'funny', 'me', 'followme', 'follow', 'cinematography', 'cinema',
                'love', 'instagood', 'instagood', 'followme', 'fashion', 'sun', 'scruffy',
                'street', 'canon', 'beauty', 'studio', 'pretty', 'vintage', 'fierce',
                'photooftheday', 'lifeisgood', 'swag', 'instadaily', 'follow4follow',
                'instafood', 'foodporn', 'food', 'organic', 'best', 'vegetarian', 'vegan',
                'homemade', 'travel', 'vacation', 'tourist', 'android', 'applevsandroid', 'makinglifeeasier',
                'innovation', 'instagood', 'loveislove', 'lookgoodfeelgood', 'nopainnogain', 'noexcuses', 'stockingstuffers',
                'entrepreneur', 'goodeats', 'trainhard', 'instagiveaway', 'sweepstakes', 'cute', 'sky',
                'workout', 'drawing', 'home', 'goodmorning', 'nofilter',
                'baby', 'design', 'lol', 'gym', 'instapic', 'flowers', 'blue',
                'arts', 'artistic', 'following', 'loveher', 'artwork', 'loveyou', 'loveyourself',
                'coffee', 'coffeegram', 'coffeeholic', 'coffeeaddict', 'coffeelover', 'sprouts', 'wholefoods',
                'dogs', 'dogslife', 'dogslover', 'musicians', 'musician', 'artofvisuals', 'artistsoninstagram',
                'choirs', 'wonderful', 'lovelife', 'activewear', 'smiley',
                'artsy', 'pathetic', 'lover', 'queen', 'loser', 'painful', 'popculture',
                'techindustry', 'engineering', 'instagram', 'unfollow', 'venturecapital', 'military', 'shootings',
                'violence', 'guns', 'keepmoving', 'underwear', 'underwear', 'panties', 'happiness',
                'hawaii', 'mountains', 'skateboarding', 'venicebeach', 'diplo',
                'edc', 'cashisking', 'entrepreneur', 'gym', 'bench', 'abs', 'health',
                'christmas', 'thanksgiving', 'pathetic', 'industrial', 'welding', 'applevsandroid', 'innovation',
                'kimkardasian', 'goodboy', 'dogs', 'animallover', 'crocodiles', 'therock',
                'theavengers',
                'noclue', 'unfair', 'suicide', 'heroine', 'weed', 'bobmarley', 'planes',
                'clueless', 'malibubeach', 'malibu', 'music', 'ironman',
                'thor', 'thehulk', 'comicon', 'nerds', 'destiny', 'halo', 'xbox',
                'microsoft', 'google', 'apple', 'amazon', 'oracle', 'loveyou', 'canyousee',
                'lightning', 'camping', 'climbing', 'agenda', 'racism', 'fuckracism', 'denver',
                'clouds', 'sky', 'denversunset', 'sunset', 'california', 'madmen', 'politics',
                'newyork', 'georgia', 'louisiana', 'southcarolina', 'northcarolina',
                'charity', 'sex', 'vibrators', 'television', 'cbs', 'happy', 'adamsandler',
                'jamiefoxx', 'kimkardasian', 'postmalone', 'lilpeep', 'fights', 'protests', 'police',
                'fuckthepolic', 'culture', 'gallery', 'wishyouwerehere', 'oldtimes', 'gratefuldead', 'gratefuldeadfamily',
                'gdf', 'canon', 'beauty', 'studio', 'pretty', 'vintage', 'fierce',
                'photooftheday', 'lifeisgood', 'swag', 'instadaily', 'follow4follow',
                'instafood', 'foodporn', 'food', 'organic', 'best', 'vegetarian', 'vegan',
                'homemade', 'travel', 'vacation', 'tourist', 'android', 'applevsandroid', 'makinglifeeasier',
                'innovation', 'instagood', 'loveislove', 'lookgoodfeelgood', 'nopainnogain', 'noexcuses',
                'stockingstuffers',
                'entrepreneur', 'goodeats', 'trainhard', 'instagiveaway', 'sweepstakes', 'cute', 'sky',
                'workout', 'drawing', 'home', 'goodmorning', 'nofilter',
                'baby', 'design', 'lol', 'gym', 'instapic', 'flowers', 'blue',
                'arts', 'artistic', 'following', 'loveher', 'artwork', 'loveyou', 'loveyourself',
                'coffee', 'coffeegram', 'coffeeholic', 'coffeeaddict', 'coffeelover', 'sprouts', 'wholefoods',
                'dogs', 'dogslife', 'dogslover', 'musicians', 'musician', 'artofvisuals', 'artistsoninstagram',
                'choirs', 'wonderful', 'lovelife', 'activewear', 'smiley',
                'artsy', 'pathetic', 'lover', 'queen', 'loser', 'painful', 'popculture',
                'techindustry', 'engineering', 'instagram', 'unfollow', 'venturecapital', 'military', 'shootings',
                'violence', 'guns', 'keepmoving', 'underwear', 'underwear', 'panties', 'happiness',
                'hawaii', 'mountains', 'skateboarding', 'venicebeach', 'diplo',
                'edc', 'cashisking', 'entrepreneur', 'gym', 'bench', 'abs', 'health',
                'christmas', 'thanksgiving', 'pathetic', 'industrial', 'welding', 'applevsandroid', 'innovation',
                'kimkardasian', 'goodboy', 'dogs', 'animallover', 'crocodiles', 'therock',
                'theavengers',
                'noclue', 'unfair', 'suicide', 'heroine', 'weed', 'bobmarley', 'planes',
                'clueless', 'malibubeach', 'malibu', 'music', 'ironman',
                'thor', 'thehulk', 'comicon', 'nerds', 'destiny', 'halo', 'xbox',
                'microsoft', 'google', 'apple', 'amazon', 'oracle', 'loveyou', 'canyousee',
                'lightning', 'camping', 'climbing', 'agenda', 'racism', 'fuckracism', 'denver',
                'clouds', 'sky', 'denversunset', 'sunset', 'california', 'madmen', 'politics',
                'noclue', 'unfair', 'suicide', 'heroine', 'weed', 'bobmarley', 'planes',
                'covid', 'blue', 'biden', 'democrats', 'vote',
                'grocerystore', 'target', 'pizzahut', 'wearamask', 'teachme', 'wisdom', 'iloveyou',
                'accoutability', 'sustainability', 'solar', 'tesla', 'teslamodel3', 'spacex', 'nasa',
                'astronomy', 'telescope', 'fishing', 'peoplewatching', 'pity', 'pety', 'pranks',
                'college', 'frat', 'slut', 'dimensions', 'coding', 'mountainmen', 'smalltown',
                'lightning', 'camping', 'climbing',
                'markzuckerberg', 'timburton', 'mileycyrus', 'dancing',
                'skating', 'tennis', 'basketball', 'soccee', 'sports', 'champions', 'underwear',
                'nordstrom', 'nightlife', 'ed', 'medicine', 'hospital', 'nurses', 'doctors',
                'bipolar', 'forbidden', 'fairgame', 'cheater', 'cheatingboyfriend',
                'restaraunts', 'steak', 'ovenfreshpizza', 'citylife', 'palmsprings', 'sacramento', 'healthone',
                'wellsfargo', 'killing', 'lovenotwar', 'phish', 'ilovelife', 'mars', 'blueorigin',
                'promotion', 'venue', 'concert', 'prettylights', 'redrocks', 'sickness', 'lovingeachother',
                'soulmate', 'real', 'jogging', 'starbucks', 'starbucks', 'wellsfargo', 'politics',
                'petite', 'sexy', 'tennis', 'basketball', 'soccee', 'sports', 'champions', 'underwear',
                'nordstrom', 'nightlife', 'ed', 'medicine', 'hospital', 'nurses', 'doctors',
                'animated', 'hour', 'far', 'cheater', 'hanging',
                'tree', 'blizzard', 'bizarre', 'citylife', 'palmsprings', 'sacramento', 'healthone',
                'generator', 'marvel', 'captainamerica', 'why', 'ok', 'whatever', 'stupidperson',
                'hangingbyathread', 'venue', 'concert', 'blot', 'redrocks', 'sickness', 'lovingeachother',
                'brainstorming', 'science', 'goodposture', 'chicagostylepizza', 'whatnow', 'lonely', 'rediculous', 'drunk'
                'petite', 'bed', 'cushions', 'puppy', 'myboy', 'isolation', 'thelaundrylist', 'somuchpotential',
                'addiction', 'sobriety', 'golfing', 'realization', 'poverty', 'well', 'undo',
                'why', 'mango', 'joe', 'city', 'ventures', 'offroading', 'dirtbiking', 'gear',
                'paintball', 'nightlife', 'ed', 'medicine', 'hospital', 'nurses', 'doctors',
                'animated', 'hour', 'far', 'cheater', 'hanging',
                'tree', 'blizzard', 'bizarre', 'citylife', 'palmsprings', 'sacramento', 'healthone',
                'generator', 'marvel', 'captainamerica', 'why', 'ok', 'whatever', 'stupidperson',
                'hangingbyathread', 'venue', 'concert', 'blot', 'redrocks', 'sickness', 'lovingeachother',
                'brainstorming', 'science', 'goodposture', 'chicagostylepizza', 'whatnow', 'lonely', 'rediculous', 'drunk'
                'space', 'nebula', 'science', 'geeks', 'gamers', 'glasses', 'videogames', 'bigscreen', 'fire',
                'hash', 'stoners', '420', 'european', 'hiking', 'starwars', 'hollywood',
                'streetfight', 'scenic', 'longwayhome', 'lifeishard', 'kingsoopers', 'reading', 'python', 'pop',
                'michaeljackson', 'shots', 'beer', 'bar', 'cheesecakefactory', 'celebrity', 'thepeople',
                'outdoors', 'camping', 'vacation', 'travel', 'yolo',
                'palmtrees', 'beach', 'easylife', 'rich', 'parishilton', 'brittanyspears', 'nsync',
                'backstreetboys', 'idontknowyou', 'cops', 'caraccident', 'shopping', 'designer', 'mall',
                'icecream', 'chinesefood', 'wonderfulnews', 'babyboy', 'red', 'collections', 'cars',
                'exotics', 'watches', 'rolex', 'petition', 'liberal', 'unbreakable', 'curious', 'loving'
                'mother',
                    ]

while(j < 1):
    while(i < 1):
        try:

            time.sleep(5)
            rand = random.randint(1, 3)
            r = RandomWords()
            tag = r.random_word()

            ig.go_to_hashtag(tag)
            ig.like_photos(rand)

        except:
            break