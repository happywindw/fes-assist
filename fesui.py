# -*- coding: utf-8 -*-
from fbui.rootframe import RootFrame
from fesbusi import FesBusi


class FesRootFrame(RootFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.fb = FesBusi()

        self.trans_choice_dict = {
            0: (),
            1: ('5', 'GHPOS', '工商银行大厅POS'),
            2: ('6', 'GHIMAC', '工商银行一体机IMAC'),
            3: ('8', 'GHAPP', '工商银行APP'),
            4: ('5', 'ZHPOS', '招商银行大厅POS'),
            5: ('8', 'CCBAPP', '建设银行APP')
        }

        self.top_static_text.SetLabel('未选择交易类型！')
        self.top_static_text.SetForegroundColour((255, 0, 0))
        self.top_button.Disable()
        print('program start.')
        pass

    def on_choose_tran_type(self, event):
        choice_num = self.trans_choice.GetCurrentSelection()
        if choice_num == 0:
            self.top_static_text.SetLabel('未选择交易类型！')
            self.top_static_text.SetForegroundColour((255, 0, 0))
            self.top_button.Disable()
            return

        self.top_button.Enable()
        tran_date = self.trans_date_picker.GetValue().Format('%Y-%m-%d')
        choice_type = self.trans_choice_dict.get(choice_num)[2]
        self.top_static_text.SetLabel(choice_type + '  ' + tran_date)
        self.top_static_text.SetForegroundColour((0, 0, 255))

    def on_top_button(self, event):
        tran_date = self.trans_date_picker.GetValue().Format('%Y%m%d')
        choose_type = self.trans_choice_dict.get(self.trans_choice.GetCurrentSelection())
        res = self.fb.check_account(tran_date, choose_type[0], choose_type[1])


