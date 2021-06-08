from crime_cctv.models import CrimeDTO
from common.services import CommonService
import pandas as pd
import xlwings as xw


class CrimeService(CommonService):

    dto = CrimeDTO()

    def new_model_from_csv(self, payload) -> object:
        this = self.dto
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)

    def new_model_from_xls(self, payload) -> object:
        this = self.dto
        this.context = './data/'
        this.fname = payload
        return pd.read_excel(this.context + this.fname)
