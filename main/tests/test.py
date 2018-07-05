# test_basic.py
import unittest
from flask import current_app
from main import create_all, db


class BasicTestCase(unittest.TestCase):
    """
    setUP()和tearDown()方法分别在各测试前后运行，
    并且名字以test_开头的函数都作为测试执行。

    """

    def setUp(self):
        """每个单元测试运行之前被调用"""
        self.app = create_all('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """每个单元测试执行结束后会调用"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        """测试确保程序实例存在"""
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        """测试确保程序在测试配置中运行"""
        self.assertTrue(current_app.config['TESTING'])
