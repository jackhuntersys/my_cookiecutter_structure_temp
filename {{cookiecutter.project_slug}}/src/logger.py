import logging
import os
from datetime import datetime

# Vaqtni kursatadigan log_file yasash
LOG_FILE = f"{datetime.now().strftime("%d_%m_%Y, %H:%M:%S")}.log"


# log lar uchun folder ochish
logs_dir = os.path.join(os.getcwd(), 'logs')
os.makedirs(logs_dir, exist_ok=True)


# log faylni full path ni kursatish

LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logging

logging.basicConfig(
    filename=LOG_FILE_PATH, # Loglar yoziladigan fayl nomi yoki yo‘li
    filemode='a', # 'a' - mavjud log faylga qo‘shib yozadi; 'w' - eski faylni o‘chirib yangi ochadi
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s", # Log yozilish uslubi
    level=logging.INFO   # INFO darajasidan yuqoridagi loglar yoziladi (INFO, WARNING, ERROR va h.k.)
)