import wx
import Gui

class Frame(Gui.MyFrame1):
    def __init__(self, parent):
        super().__init__(parent)

    def calculate( self, event ):
        p = self.m_textCtrl1.GetValue()
        l = self.m_textCtrl2.GetValue()
        t = self.m_textCtrl3.GetValue()
        try:
            vol = eval(f'({p} * {l} * {t})')
            lp =  eval(f'(2 * {p} * {l}) + (2 * {l} * {t}) + (2 * {p} * {t})')
            wx.MessageBox(f'Volume: {vol}\nLuas Permukaan: {lp}', 'Hasil Perhitungan', wx.OK | wx.ICON_INFORMATION)
            if (wx.OK):
                self.m_textCtrl1.SetValue("")
                self.m_textCtrl2.SetValue("")
                self.m_textCtrl3.SetValue("")
        except SyntaxError:
            wx.MessageBox('Inputan tidak boleh Null', 'Peringatan', wx.OK | wx.ICON_ERROR)
            if (wx.OK):
                self.m_textCtrl1.SetValue("")
                self.m_textCtrl2.SetValue("")
                self.m_textCtrl3.SetValue("")



app = wx.App()
frame = Frame(parent=None)
frame.Show()
app.MainLoop()