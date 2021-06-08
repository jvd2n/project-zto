from real_estate.models import HousingDTO
import pandas as pd
import xlwings as xw


class HousingService(object):

    dto = HousingDTO()

    # DF 생성하기
    def new_model(self, payload):

        this = self.dto
        this.context = './data/'
        this.fname = payload
        # 'time_series_cost2.xlsx'
        # excel_dir = os.path.join(this.context, this.fname)
        """
        < No Encryption xlsx file >
        df = pd.read_excel(this.context + this.fname + '.xlsx', sheet_name='매매종합')
        """
        sheet = xw.Book(this.context + this.fname + '.xlsx').sheets['매매종합']
        row_num = sheet.range(1, 1).end('down').end('down').row
        data_range = 'A2:GE' + str(row_num)
        df = sheet[data_range].options(pd.DataFrame, index=False, header=True).value
        return df
