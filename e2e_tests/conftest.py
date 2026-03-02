import pytest

@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {
        "args": [
            "--disable-dev-shm-usage",
            "--disable-gpu",
            "--no-sandbox",
            "--disable-setuid-sandbox",
        ]
    }
