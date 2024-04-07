class TestCase:
    def __enter__(self):
        print('Entrando')
    
    def __exit__(self, exec_type, exc_value, exc_tb):
        print('Saindo')

with TestCase() as hello:
    print('Meio')