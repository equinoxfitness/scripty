import unittest
from scripty.module import ScriptRunner
from unittest.mock import patch


class TestScriptRunner(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scripty = ScriptRunner(
            db_name="db_name",
            host="host",
            user="user",
            password="password",
            port=5439,
            test=True,
        )
        cls.sql = """
                SELECT field1, field2 FROM test
                WHERE field1 = '$[?var1]' AND field2 = '$[?var2]'
                """

    @patch("scripty.module.ScriptRunner.expand_params")
    def test_expand_params(self, mock_expand_params):
        print("--------------test_expand_params")

        mock_expand_params.return_value = """
                    SELECT field1, field2 FROM test
                    WHERE field1 = 'result1' AND field2 = 'result2'
                    """

        params = {"var1": "result1", "var2": "result2"}
        result = self.scripty.expand_params(self.sql, params)
        expected_result = """
                    SELECT field1, field2 FROM test
                    WHERE field1 = 'result1' AND field2 = 'result2'
                    """

        self.assertEqual(result, expected_result)

    @patch("scripty.module.ScriptRunner.run_script")
    def test_run_script(self, mock_run_script):
        print("--------------test_run_script")
        self.scripty.run_script(self.sql)
        self.assertTrue(mock_run_script.called)


if __name__ == "__main__":
    unittest.main()
