import datetime
from classLibrary.User import User
from classLibrary.Coffe import Coffe
from classLibrary.Additional import Additional
class Pay:
    _date: datetime.date
    _eMoney: bool
    _client: User
    _sum = 0.0
    _coffes: list[Coffe]
    _additionals: list[Additional]
    def __init__(self, eMoney, client, coffes=None, additionals=None):
        if additionals is None:
            additionals = []
        if coffes is None:
            coffes = []
        self._eMoney = eMoney
        self._client = client
        self._coffes = coffes
        self._date = datetime.datetime.now().date()
        self._additionals = additionals
        if len(coffes) !=0:
            for coffe in coffes:
                self._sum += coffe.getPrice()
        if len(additionals) !=0:
            for additional in additionals:
                self._sum += additional.getPrice()


