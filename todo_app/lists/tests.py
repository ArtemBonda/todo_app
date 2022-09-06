from django.test import TestCase

class SmokeTest(TestCase):
    '''Тест на токсичность'''

    def test_bad_maths(self):
        '''тест: Неправильные математические расчеты'''
        self.assertEqual(1 + 1, 3,msg='Fail test')
