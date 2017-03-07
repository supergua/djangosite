import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question


class QuestionMethodTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        在将来发布的问卷应该返回False
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        日期超过1天的将返回False。这里创建了一个30天前发布的实例。
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        最近一天内的将返回True。这里创建了一个1小时内发布的实例。
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
