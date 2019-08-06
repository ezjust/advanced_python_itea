class File:
    def __init__(self, file_name, what_to_do):
        self._file_name = file_name
        self._what_to_do = what_to_do

    def __enter__(self):
        f = open(self._file_name, f'{self._what_to_do}')
        return f

    def __exit__(self, *args):
        if ValueError in args:
            raise Exception('Inserted wrong value')
        if FileNotFoundError in args:
            raise Exception(f'No file {self._file_name} found')
        if args[0] is None:
            print('No args found, script finished without errors')


with File('test.txt', 'r') as f:
    print(f)
