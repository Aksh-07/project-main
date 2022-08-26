import user_database
import user_input
import android_actions
import retail_actions
import python_wrapper
import speech_errors
from time import time
import os
import numpy as np


if __name__ == "__main__":
    start_time_ = time()
    user_obj = user_input.ProcessUserInput()
    obj = python_wrapper.PythonSpeechWrapper()

    if "user_tasks.db" not in os.listdir(r"C:\Users\kc\Downloads\project-main\project-main"):
        read_file = user_obj.read_input_db_file("py4j/data.txt")
        obj.create_local_db_tables(table_names=user_input.table_names)
        user_input.table_names.clear(), user_input.android_input_data.clear(), user_input.business_input_data.clear(), user_input.supplies_input_data.clear(), user_input.data_tag.clear()

    # obj.update_local_db("py4j/data.txt")
    # r = user_database.ProcessDataBaseRequests()
    # r.create_connection()
    # rr = r.fetch_db_data("android_words", 752)
    # print(rr)
    ui = obj.get_user_input("text")
    
    # print(ui)
    # dl = obj.delete_local_db_rows("supply_add_ons", "pizza")
    print("Total execution time : %s " %(time() - start_time_))


