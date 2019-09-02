import shelve


class Registration:
    def __init__(self, login_name: str, password: str):
        self.login = login_name
        self.password = password
        self.db_name = 'local.db'

    def save_new_user(self):
        with shelve.open(self.db_name) as db:
            if self.login not in db:
                if self.password != '':
                    db[self.login] = self.password
                    return f'new user {self.login} has been added'
                return f"you've entered empty password"
            print('such user already exist')


class Authorization(Registration):
    def log_in(self):
        with shelve.open(self.db_name) as db:
            if self.login in db:
                if self.password == db.get(self.login):
                    pass

    def get_comment(self):




