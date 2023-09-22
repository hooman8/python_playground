class GitHubApiError(Exception):
    def __init(self, status_code):
        if status_code == 403:
            message = "rate limit reached."
        else:
            message = f"Status code was: {status_code}"

        super.__init__(message)


raise GitHubApiError(403)
