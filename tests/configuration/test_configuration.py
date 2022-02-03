import sys
sys.path.append("src")

class TestConfiguration:

    def setup_method(self,method):
        print('method={}'.format(method.__name__))

    def teardown_method(self, method):
        print('method={}'.format(method.__name__))
        
    def test_hello_world(self):
        from configuration import host, port, debug

        assert host == "0.0.0.0"
        assert port == 80
        assert debug == True

