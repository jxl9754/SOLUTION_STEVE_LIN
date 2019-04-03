"""
This is the message module and implement create hash message and read message
"""

# 3rd party modules
from flask import make_response, abort
import hashlib

# Data to serve with this test
hash_message = {
}


def get_message(hash_msg):
    """
    This function responds to a request for /messages/{hash}
    :param hash_msg:   hash of message to find
    :return:        message and 200 return code or 404 on hash not found
    """
    # Does the hash exist in hash_message - status 404
    if hash_msg in hash_message:
        message_key = hash_message.get(hash_msg)
        return {"message": message_key}, 200
    # otherwise, not found abort exception
    else:
        # return {"err_msg": "Hash Message not found - " + hash_msg}, 404
        abort(404, {"err_msg": "Hash Message not found - " + hash_msg})


def create_hash_sha256(msg):
    """
    This function creates hash256 structure
    based on the passed in msg data
    :param msg:  message string to create hash in message structure
    :return:        201 on success, 404 on msg key not exists
    """
    message_key = msg.get("message", None)

    # Does the input message exist?
    if message_key is not None:
        hash_object=hashlib.sha256(message_key.encode('utf-8'))
        hash_message[hash_object.hexdigest()] = message_key
        return {"digest": hash_object.hexdigest()}, 201
    # Otherwise, that's an abort error - status 404
    else:
        # return {"err_msg": "No input Message"}, 404
        abort(404, {"err_msg": "No input Message"})
