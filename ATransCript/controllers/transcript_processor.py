from flask import Blueprint, request, jsonify
from .transcript_tasks import add_two,get_large_audio_transcription
from flask import current_app


transcript_module = Blueprint("transcript_module", __name__, url_prefix="/transcript")


@transcript_module.route("/", methods=['GET'])
def trans_ping():
    """

    :return:
    """
    task_id = add_two.delay(10, 20)
    print(task_id)
    return "DEMO"


@transcript_module.route("/convert_transcript", methods=['POST'])
def convert_transcript():
    """

    :return:

    """
    audio_file = request.files['file']
    try:
        file_extention = audio_file.filename.split('.')[-1].lower()
        print(file_extention)
        if file_extention not in current_app.config['ALLOWED_EXTENTIONS']:
            return jsonify({"message": "Invalid file stream"})
        a = get_large_audio_transcription(audio_file, file_extention)
        print(a)
        return jsonify({"message": "cool"})
    except Exception as e:
        print(e)
        return jsonify({"message": "error"})
