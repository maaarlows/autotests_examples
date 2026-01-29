import os
import time
import argparse

E2E_TESTS = os.path.join('e2e_tests'),
ALLURE_RESULTS = os.path.join('allure-results')

test_config = {
    'e2e': [
        os.path.join(E2E_TESTS, 'subscription_stripe_tests.py')
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
    '--e2e',
    help='e2e tests',
    action='store_true'
)

arguments = argument_parser.parse_args()
if arguments.e2e:
    os.system(f'python -m pytest {collect_tests(test_config['e2e'])} --alluredir {allure_results_path}')
#elif arguments.smoke:
    #os.system(f'python -m pytest {collect_tests(test_config['smoke'])} --alluredir {allure_results_path}')

os.system(f'allure serve {allure_results_path}')