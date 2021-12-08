import unittest
from app import app


class TestLogin(unittest.TestCase):
    """定义测试案例"""
    def setUp(self):
        """在执行具体的测试方法前，先被调用"""

        self.app = app
        # 激活测试标志
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_pass_correctx(self):
        tester = app.test_client(self)
        response = tester.post('/register', data=dict(password='testtest'))
        self.assertEqual(response.status_code, 200)

    def test_pass_correct(self):
        tester = app.test_client(self)
        response = tester.post('/register', data=dict(password='testte'))
        self.assertFalse(b'Field must be at least 6 characters long.' in response.data)

d
if __name__ == '__main__':
    unittest.main()
