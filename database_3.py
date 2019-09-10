class id_field:
    def __init__(self, id):
        self.id = id

    def isEqualTo(self, id):
        return id==self.id

    def isGreater(self, id):
        return id<self.id

    def isLower(self, id):
        return id>self.id

    def isIn(self, idlist):
        for id in idlist:
            if id==self.id:
                return True
        return False

    def isNotIn(self, idlist):
        for id in idlist:
            if id==self.id:
                return False
        return True

class url_field:
    def __init__(self, url):
        self.url = url

    def isEqualTo(self, url):
        return url==self.url

class date_field:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def isEqualTo(self, day, month, year):
        if day == self.day and month == self.month and year==self.year:
            return True
        return False

    def isGreater(self, day, month, year):
        if year<self.year:
            return True
        elif year==self.year:
            if month<self.month:
                return True
            elif month==self.month:
                if day<self.day:
                    return True
        return False

    def isLower(self, day, month, year):
        if year>self.year:
            return True
        elif year==self.year:
            if month>self.month:
                return True
            elif month==self.month:
                if day>self.day:
                    return True
        return False

class rating_field:
    def __init__(self, rating):
        self.rating = rating

    def isEqualTo(self, rating):
        return rating==self.rating

    def isGreater(self, rating):
        return rating<self.rating

    def isLower(self, rating):
        return rating>self.rating

date =	{
  "day": 7,
  "month": 2,
  "year": 2016
}

entry =	{
  "id": 6,
  "url": "www.test.co",
  "date": date,
  "rating": 7
}

db_table = [entry]
result = []
for row in db_table:
    idd = id_field(row['id'])
    url = url_field(row['url'])
    datee = date_field(row['date']['day'], row['date']['month'], row['date']['year'])
    rating = rating_field(row['rating'])
    print rating.rating
    if rating.isGreater(2) and rating.isLower(9) and idd.isIn([1, 3, 6, 10, 15]) and datee.isGreater(1,1,2016):
        result.append([idd.id, url.url, [datee.day, datee.month, datee.year], rating.rating])

print result
