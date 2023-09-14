from datetime import datetime


class Reservation:

    def __init__(self,
                 id: int,
                 id_user: int,
                 id_hotel: int,
                 check_in: datetime,
                 check_out: datetime,
                 num_of_adults: int,
                 num_of_children: int) -> None:
        self._id = id
        self._id_user = id_user
        self._id_hotel = id_hotel
        self._check_in = check_in
        self._check_out = check_out
        self._num_of_adults = num_of_adults
        self._num_of_children = num_of_children

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, new_id: id):
        if new_id:
            self._id = new_id

    @property
    def id_user(self):
        return self._id_user
    
    @id_user.setter
    def id_user(self, new_id_user: id_user):
        if new_id_user:
            self._id_user = new_id_user

    @property
    def id_hotel(self):
        return self._id_hotel
    
    @id_hotel.setter
    def id_hotel(self, new_id_hotel: id_hotel):
        if new_id_hotel:
            self._id_hotel = new_id_hotel

    @property
    def check_in(self):
        return self._check_in
    
    @check_in.setter
    def check_in(self, new_check_in: check_in):
        if new_check_in:
            self._check_in = new_check_in

    @property
    def check_out(self):
        return self._check_out
    
    @check_out.setter
    def check_out(self, new_check_out: check_out):
        if new_check_out:
            self._check_out = new_check_out

    @property
    def num_of_adults(self):
        return self._num_of_adults
    
    @num_of_adults.setter
    def num_of_adults(self, new_num_of_adults: num_of_adults):
        if new_num_of_adults:
            self._num_of_adults = new_num_of_adults

    @property
    def num_of_children(self):
        return self._num_of_children
    
    @num_of_children.setter
    def num_of_children(self, new_num_of_children: num_of_children):
        if new_num_of_children:
            self._num_of_children = new_num_of_children
   