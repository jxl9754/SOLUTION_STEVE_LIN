import unittest
import message


class PaxosTest(unittest.TestCase):

    def test_message_create_sha256(self):
        """Test message function create_hash_sha256 with message FOO"""
        query_string = {
            "message": "FOO"
        }
        msg = message.create_hash_sha256(query_string)
        self.assertEqual(msg[0]["digest"], '9520437ce8902eb379a7d8aaa98fc4c94eeb07b6684854868fa6f72bf34b0fd3')
        self.assertEqual(msg[1], 201)
        print("\ntest_message_create_sha256 Done")

    def test_empty_message_create_sha256(self):
        """Test message function create_hash_sha256 with empty message"""
        query_string = {
        }
        try:
            msg = message.create_hash_sha256(query_string)
        except:
            print("Abort Exception")
            pass

        # self.assertEqual(msg[1], 404)
        print("\ntest_empty_message_create_sha256 Done")

    def test_get_message(self):
        """Test message function get_message with existed hash message"""
        query_string = {
            "message": "FOO"
        }
        message.create_hash_sha256(query_string)

        query_string = {
            "hash": "9520437ce8902eb379a7d8aaa98fc4c94eeb07b6684854868fa6f72bf34b0fd3"
        }

        key = message.get_message(query_string["hash"])

        self.assertEqual(key[0]["message"], 'FOO')
        self.assertEqual(key[1], 200)
        print("\ntest_get_message Done")

    def test_get_message_not_exist(self):
        """Test message function get_message without existed hash message"""
        query_string = {
            "hash": "9520437ce8902eb379a7d8aaa98fc4c94eeb07b6684854868fa6f72bf34b0fd3"
        }
        try:
            key = message.get_message(query_string["hash"])

            # self.assertEqual(key[0]['err_msg'], 'Hash Message not found')
            # self.assertEqual(key[1], 404)
            print("\ntest_get_message_not_exist Done")
        except:
            print("Abort Exception")
            pass


if __name__ == '__main__':
        unittest.main()

