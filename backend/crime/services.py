from abc import abstractmethod
from common.services import CommonService
from crime.models import CrimeDTO
import pandas as pd
import xlwings as xw


class CrimeService(CommonService):

    dto = CrimeDTO()

    def new_model_from_csv(self, payload) -> object:
        this = self.dto
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(self.context + this.fname)

    def new_model_from_xls(self, payload) -> object:
        this = self.dto
        this.context = './data/'
        this.fname = payload
        return pd.read_excel(self.context + this.fname)
