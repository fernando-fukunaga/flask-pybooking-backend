class Hotel:

    def __init__(self,
                 id: int,
                 name: str,
                 location: str,
                 daily_rate: float,
                 rating: float,
                 additional_info: str) -> None:
        self._id = id
        self._name = name
        self._location = location
        self._daily_rate = daily_rate
        self._rating = rating
        self._additional_info = additional_info

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, new_id: id):
        if new_id:
            self._id = new_id

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name: str):
        if new_name:
            self._name = new_name

    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, new_location: str):
        if new_location:
            self._location = new_location

    @property
    def daily_rate(self):
        return self._daily_rate
    
    @daily_rate.setter
    def daily_rate(self, new_daily_rate: float):
        if new_daily_rate:
            self._daily_rate = new_daily_rate

    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, new_rating: float):
        if new_rating:
            self._rating = new_rating

    @property
    def additional_info(self):
        return self._additional_info
    
    @additional_info.setter
    def additional_info(self, new_additional_info: str):
        if new_additional_info:
            self._additional_info = new_additional_info
