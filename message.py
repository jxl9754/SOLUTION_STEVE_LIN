"""
This is the message module and supports all the ReST actions for the
message collection
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
    :return:        message key
    """
    # Does the hash exist in hsah_message?
    if hash_msg in hash_message:
        message_key = hash_message.get(hash_msg)

    # otherwise, nope, not found
    else:
        abort(404, "Hash Message {msg} not found".format(msg=hash_msg))

    return {"message": message_key}, 200


def create_hash_sha256(msg):
    """
    This function creates hash256 structure
    based on the passed in msg data
    :param msg:  message string to create hash in message structure
    :return:        201 on success, 404 on msg key not exists
    """
    message_key = msg.get("message", None)

    # Does the person exist already?
    if message_key is not None:
        hash_object=hashlib.sha256(message_key.encode('utf-8'))
        hash_message[hash_object.hexdigest()] = message_key
        return {"digest": hash_object.hexdigest()}, 201

    # Otherwise, they exist, that's an error
    else:
        abort(404, "No input Message")
