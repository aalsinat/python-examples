from rx_extensions.reqs import rx_get_json


# noinspection PyMethodMayBeStatic
class GithubService:
    def rx_user_details(self, username):
        return rx_get_json('https://api.github.com/users/{0}'.format(username))

    def rx_starred_repositories(self, username):
        return rx_get_json('https://api.github.com/users/{0}/starred'.format(
            username))

    def rx_contributors(self, repository_path):
        return rx_get_json(
            'https://api.github.com/repos/{0}/contributors'.format(
                repository_path))
