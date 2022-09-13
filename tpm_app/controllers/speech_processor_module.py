from flask import Blueprint

from tasks import console_tasks
speech_processor = Blueprint('speech_module', __name__, url_prefix="/speech_processor")


@speech_processor.route("/",methods=["GET"])
def fetch_speech_to_text():

    """

    :return:
    """
    console_tasks.delay(1,2)
    return "DEMO works fine...!!!"
