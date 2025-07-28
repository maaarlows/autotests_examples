import os
import time
import argparse

TESTS_PATH = os.path.join('api_tests')
ALLURE_RESULTS = os.path.join('allure-results')

test_config = {
    'regress': [
        os.path.join(TESTS_PATH, 'get_person_test.py'),
        os.path.join(TESTS_PATH, 'create_person_test.py'),
        os.path.join(TESTS_PATH, 'delete_person_test.py'),
    ],
    'smoke': [
        os.path.join(TESTS_PATH, 'get_person_test.py')
    ]
}

def collect_tests(tests):
    res_str = ''
    for test_path in tests:
        res_str += f' {test_path}'
    return res_str


timestr = time.strftime('%Y%m%d-%H%M%S')

allure_results_path = f'{ALLURE_RESULTS}_{timestr}'

argument_parser = argparse.ArgumentParser(prog='run_tests')
argument_parser.add_argument(
    '--regress',
    help='regression api_tests',
    action='store_true'
)
argument_parser.add_argument(
    '--smoke',
    help='smoke api_tests',
    action='store_true'
)

arguments = argument_parser.parse_args()
if arguments.regress:
    os.system(f'python -m pytest {collect_tests(test_config['regress'])} --alluredir {allure_results_path}')
elif arguments.smoke:
    os.system(f'python -m pytest {collect_tests(test_config['smoke'])} --alluredir {allure_results_path}')

os.system(f'allure serve {allure_results_path}')