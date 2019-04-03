from unittest import TestCase
import message


class PaxosTest(TestCase):

    def test_message_create_sha256(self):
        query_string = {
            "message": "FOO"
        }
        msg = message.create_hash_sha256(query_string)
        print(msg)
        print(msg[0]["digest"])
        self.assertEqual(msg[0]["digest"], '9520437ce8902eb379a7d8aaa98fc4c94eeb07b6684854868fa6f72bf34b0fd3')
        print(msg[1])
        self.assertEqual(msg[1], 201)
        print("test_message_create_sha256 Done")

    def test_empty_message_create_sha256(self):
        query_string = {
        }
        msg = message.create_hash_sha256(query_string)
        print(msg)
        self.assertEqual(msg[1], 404)

    def test_get_message(self):
        query_string = {
            "message": "FOO"
        }
        msg = message.create_hash_sha256(query_string)

        query_string = {
            "hash": "9520437ce8902eb379a7d8aaa98fc4c94eeb07b6684854868fa6f72bf34b0fd3"
        }

        key = message.get_message(query_string["hash"])
        print(key)
        self.assertEqual(key[0]["message"], 'FOO')
        self.assertEqual(key[1], 200)

    def test_get_message_not_exist(self):

        query_string = {
            "hash": "9520437ce8902eb379a7d8aaa98fc4c94eeb07b6684854868fa6f72bf34b0fd3"
        }

        key = message.get_message(query_string["hash"])
        print(key)
        self.assertEqual(key[0]["err_msg"], 'Message not found')
        self.assertEqual(key[1], 404)

