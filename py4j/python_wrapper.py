from distutils.text_file import TextFile
from multiprocessing import current_process
from py4j.java_gateway import JavaGateway,GatewayParameters, CallbackServerParameters
import user_input as py_obj
from datetime import datetime
from speech_errors import SpeechResult as enums
from speech_errors import SpeechProcessError, SpeechInvalidArgumentError
import logging
import android_actions
# from decorators import status_check

questions = ["can", "should", "would", "what", "when", "where", "how", "who", "whose", "why", "which", "isn't", "don't",
             "aren't", "won't", "must"]
locations = ["united states of america", "usa", "uk", "united kingdom"]
tenses = ["is", "are", "will", "shall", "did", "have", "had", "has", "were"]
adverb = ["good", "open", "closed", "shutdown", "giving", "asking", "accepting", "delivering", "address"]
actions = ["show", "order", "get", "add", "cancel", "decline", "dismiss", "stop", "close", "play", "pause", "up",
           "down", "change", "save", "repeat", "shuffle", "seek", "enable", "open", "ask", "accept", "delivering",
           "back", "forward", "connect"]
android_word = ["photo", "video", "memories", "memory", "history", "past", "weather", "music", "setting", "calendar",
                 "weather", "volume", "display", "wallpaper", "screen", "saver", "profile", "picture", "notification",
                 "promotion", "date", "time", "year", "month", "temperature", "network", "wifi", "bluetooth",
                 "seconds", "minutes", "hours", "favorites", "album", "silent", "mode", "brightness", "preference",
                 "security", "camera", "cam", "camera1", "cam1", "camera2", "cam2", "camera3", "cam3", "camera4",
                 "cam4", "security", "card", "credit", "debit", "pin", "cvv", "address", "apartment", "home",
                 "emergency"]

retailers = ["costco", "kfc", "bjs", "target"]
ret_actions = ["order", "get", "add", "cancel", "stop", "take", "over"]
incomplete_actions = ["order", "get", "add", "cancel", "take", "over"]
restaurants = [""]
brands = ["nike"]
accessories = [""]
apparels = [""]
furniture = [""]
electronics = [""]
electrical = [""]
office_supplies = []
toys = []
school = []
college = []
pharma = []
cosmetics = []
snacks = []
fruits = []
diary = []
groceries = []
vegetables = []
automotive = []
women_clothing = []
men_clothing = []
optical_frames = []
sports = []

if current_process().name!="MainProcess":
    gateway = JavaGateway(gateway_parameters=GatewayParameters(auto_convert=True),callback_server_parameters=CallbackServerParameters())
    speech_process = gateway.jvm.py4j.AppClass()


class PythonSpeechWrapper:
    def __init__(self):
        """creates an object of ProcessUserInput() class from user_input module
        """
        self.user_obj = py_obj.ProcessUserInput()

    def __del__(self):
        pass

  

    def extra_user_input(self, item, i_q):
        a = android_actions.AndroidActions.additional_user_input(item)
        i_q.put(a)

        
    def get_user_input(self, data_type: str):
        """calls and compare the results from self.user_obj.run() with data_type and input_dta as argument

        Args:
            data_type (str): `audio`, `video` or `text`
            input_data (str): user input

        Raises:
            SpeechProcessError: _description_

        Returns:
            int: 1 if self.user_obj.run() fails
                 0 if self.user_obj.run() is success
        """
        try:
            start_time = datetime.now()
            if self.user_obj.run(data_type) == 0:
                logging.error("Failed to start speech process")
                return 1
            logging.debug("Total execution time : %s " % (datetime.now() - start_time))
            return 0
        except Exception as e:
            logging.error(f"{e}")
            raise SpeechProcessError(e)

    
    def update_local_db(self, db_file: TextFile):
        """calls update_local_data_base() function from user_input module

        Args:
            db_file (TextFile): .txt file to read data from

        Raises:
            SpeechInvalidArgumentError: _description_

        Returns:
            str : result from update_local_data_base() function from user_input module
        """
        try:
            logging.info("Success")
            return self.user_obj.update_local_data_base(db_file)
        except Exception as e:
            logging.error(f"{e}")
            raise SpeechInvalidArgumentError(e)

    
    def create_local_db_tables(self, table_names: list):
        """calls create_local_data_base() from user_input module to create local database with given table names

        Args:
            table_names (list): list of tables to be created in database

        Returns:
            str: result from function create_local_data_base() from user_input module
        """
        logging.info("Success")
        return self.user_obj.create_local_data_base(table_names)

    
    def delete_local_db_rows(self, table_name: str, input_data: str):
        """calls delete_local_db_data() from user_input module to delete row with given input_data from given table_name

        Args:
            table_name (str): name of table to delete row from
            input_data (str): data to match and find the row

        Returns:
            str: result from function delete_local_db_data() from user_input module
        """
        logging.info("Success")
        return self.user_obj.delete_local_db_data(table_name, input_data)


    class Java:
        implements = ['py4j.app_1']


class PythonJavaBridge(object):
    def __init__(self):
        pass

    def __del__(self):
        pass


    

    def Close_gateway(self):
        gateway.shutdown_callback_server()


    @staticmethod
    def request_user_input_from_java(que1):
        """send incomplete_input to java side functions

        Args:
            incomplete_input (list): list from validate_user_input() function from retail_actions module

        Raises:
            SpeechProcessError: _description_

        Returns:
            str: SUCCESS if java side functions return something
                 FAILURE if java side functions return nothing
        """
        try:
            # obj = PythonSpeechWrapper()
            result = speech_process.fill_data_for_speech_request()
            if result is None:
                logging.error("Failed to get requested input")
                que1.put( enums.FAILURE.name)
            logging.info("Success")
            que1.put(result)
        except Exception as e:
            logging.error(f"{e}")
            raise SpeechProcessError(e)
    
    @staticmethod
    def takeinput_from_java(que5):
     try:
        str=speech_process.enterinput()
        if str is None:
                logging.error("Failed to get requested input")
                que5.put( enums.FAILURE.name)
        logging.info("Success")
        que5.put(str)
     except Exception as e:
        logging.error(f"{e}")
        raise SpeechProcessError(e)

    @staticmethod
    def update_new_words_to_analysis(new_user_words: list,que2):
        """send the new word to java functions for update and analysis

        Args:
            new_user_words (list): list of words and its related description from user

        Raises:
            SpeechProcessError: _description_

        Returns:
            str: SUCCESS if java side functions return something
                 FAILURE if java side functions return nothing
        """
        try:
            obj = PythonSpeechWrapper()
            result = speech_process.update_new_words_cloud(new_user_words, obj)
            if result == 0:
                logging.error("Failed to get requested input")
                que2.put(enums.FAILURE.name)
            else:
                logging.info("Success")
                que2.put(enums.SUCCESS.name)
        except Exception as e:
            logging.error(f"{e}")
            raise SpeechProcessError(e)

    @staticmethod
    def process_user_intention_actions(words: list):
        """send words to java side functions

        Args:
            words (list): list containing all information about the word user entered

        Raises:
            SpeechProcessError: _description_
        """
        try:
            speech_process.process_user_actions(words)
            logging.info("Success")
        except Exception as e:
            logging.error(f"{e}")
            raise SpeechProcessError(e)

    class Java:
        implements = ['py4j.app_1']

# if __name__ == "__main__":
#     start_time_ = datetime.now()
#     obj = PythonSpeechWrapper()
#     obj.get_user_input("text", "what is this for")
#     print("Total execution time : %s " % (datetime.now() - start_time_))