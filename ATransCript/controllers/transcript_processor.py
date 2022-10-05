from flask import Blueprint, request, jsonify
from .transcript_tasks import add_two, get_large_audio_transcription
from flask import current_app
from factory import celery
from celery.result import AsyncResult
import io
import uuid
import os


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
        if file_extention not in current_app.config['ALLOWED_EXTENTIONS']:
            return jsonify({"message": "Invalid file stream"})
        file_name = f"{ str(uuid.uuid4()).replace('-', '_')}_{audio_file.filename}"
        full_path = os.path.join(current_app.config['UPLOAD_FOLDER'], file_name)
        audio_file.save(full_path)

        task = get_large_audio_transcription.delay(full_path)
        print(task)
        return jsonify({"message": "conversion initiated", "task_id": task.id})
    except Exception as e:
        print(e)
        return jsonify({"message": "error"})


@transcript_module.route("fetch_status/<task_id>", methods=['GET'])
def status_request(task_id):
    """

    :param task_id:
    :return:
    """
    try:
        task = celery.AsyncResult(task_id)
        print(task.state)
        if task.state == 'PENDING':
            # job did not start yet
            response = {
                'state': task.state,
                'current': 0,
                'total': 1,
                'status': 'Pending...'
            }
        elif task.state != 'FAILURE':
            response = {
                'state': task.state,
                'current': task.info.get('current', 0),
                'total': task.info.get('total', 1),
                'status': task.info.get('status', '')
            }
            if 'result' in task.info:
                response['result'] = task.info['result']
        else:
            # something went wrong in the background job
            response = {
                'state': task.state,
                'current': 1,
                'total': 1,
                'status': str(task.info),  # this is the exception raised
            }
        return jsonify(response)
    except Exception as e:
        print(e)
        return "ccc"
