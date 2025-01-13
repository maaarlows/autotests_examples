import os
import time

TESTS_PATH = os.path.join('tests', 'get_person_tests.py')
ALLURE_RESULTS = os.path.join('allure-results')

timestr = time.strftime('%Y%m%d-%H%M%S')

allure_results_path = f'{ALLURE_RESULTS}_{timestr}'

os.system(f'python -m pytest {TESTS_PATH} --alluredir {allure_results_path}')
os.system(f'allure serve {allure_results_path}')