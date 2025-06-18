import sys
from logger import logging



def error_message_detail(error, error_detail:sys):
    """
    Error haqida batafsil ma'lumot beradi.
    
    :param error: Xatolik obyekti
    :param error_detail: Xatolik tafsilotlari
    :return: Xatolik haqida batafsil ma'lumot
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Xatolik: {str(error)}\nFayl: {file_name}\nSatr: {line_number}"
    return error_message


class CustomException(Exception):
    """
    Maxsus xatolik klassi.
    
    :param error: Xatolik obyekti
    :param error_detail: Xatolik tafsilotlari
    """
    def __init__(self, error, error_detail:sys):
        super().__init__(error)
        self.error_message = error_message_detail(error, error_detail)

    def __str__(self):
        return self.error_message