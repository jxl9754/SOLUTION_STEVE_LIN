from unittest import TestCase
import message


class PaxosTest(TestCase):

    def test_message_create_sha256(self):
        queryString = {
            "message" : "FOO"
        }
        msg = message.create_hash_sha256(queryString)
        self.assertEqual(msg[0]["digest"],'9520437ce8902eb379a7d8aaa98fc4c94eeb07b6684854868fa6f72bf34b0fd3')
        self.assertEqual(msg[1],201)

    def test_empty_message_create_sha256(self):
        queryString = {
        }
        msg = message.create_hash_sha256(queryString)
        print(msg)
        self.assertEqual(msg[1],404)

    def test_get_message(self):
        queryString = {
            "message" : "FOO"
        }
        msg = message.create_hash_sha256(queryString)

        queryString = {
            "hash" : "9520437ce8902eb379a7d8aaa98fc4c94eeb07b6684854868fa6f72bf34b0fd3"
        }

        key = message.get_message(queryString["hash"])
        print(key)
        self.assertEqual(key[0]["message"],'FOO')
        self.assertEqual(key[1],200)

    def test_get_message_not_exist(self):

        queryString = {
            "hash" : "9520437ce8902eb379a7d8aaa98fc4c94eeb07b6684854868fa6f72bf34b0fd3"
        }

        key = message.get_message(queryString["hash"])
        print(key)
        self.assertEqual(key[0]["err_msg"],'Message not found')
        self.assertEqual(key[1],404)

