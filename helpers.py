import random


class GenerateData:

    @classmethod
    def generate_email_correct (cls):
        return 'usver'+ str(int(random.random()*10000))+'@abvgd.edu'