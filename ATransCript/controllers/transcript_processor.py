from flask import Blueprint
from .transcript_tasks import add_two


transcript_module = Blueprint("transcript_module", __name__, url_prefix="/transcript")


@transcript_module.route("/", methods=['GET'])
def trans_ping():
    """

    :return:
    """
    add_two.delay(10 ,20)
    return "DEMO"