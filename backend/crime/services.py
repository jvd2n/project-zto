from common.models import FileDTO
from common.services import Printer, Reader
from common.abstracts import ReaderBase


class CrimeService(ReaderBase):

    def csv(self, payload):
        printer = Printer()
        reader = Reader()
        file = FileDTO()
        file.context = payload.get('context')
        file.fname = payload.get('fname')
        printer.dframe(reader.csv(file))

    def xls(self, payload):
        printer = Printer()
        reader = Reader()
        file = FileDTO()
        file.context = payload.get('context')
        file.fname = payload.get('fname')
        printer.dframe(reader.xls(file, 1))

    def json(self):
        pass

    def new_file(self):
        pass

    # def new_model_from_csv(self, payload) -> object:
    #     this = self.dto
    #     this.context = './data/'
    #     this.fname = payload
    #     return pd.read_csv(self.context + this.fname)
    #
    # def new_model_from_xls(self, payload) -> object:
    #     this = self.dto
    #     this.context = './data/'
    #     this.fname = payload
    #     return pd.read_excel(self.context + this.fname)
