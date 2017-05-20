import os
import yaml
from pact_test.config.default_config import default_config


CONFIGURATION_FILE = '.pact.yml'


def verify():
    print('')
    print('Verify Pact tests: START')
    print('------------------------')
    print('\nDefault configuration:')
    print(default_config)
    user_settings_file = os.path.join(os.getcwd(), CONFIGURATION_FILE)
    if os.path.isfile(user_settings_file):
        with open(os.path.join(os.getcwd(), CONFIGURATION_FILE)) as f:
            user_settings = yaml.load(f)
            print('\nCustom configuration:')
            print(user_settings)
            default_config.update(user_settings)
    print('\nFinal configuration for the tests:')
    print(default_config)
    print('\nVerify Pact tests: DONE')
    print('------------------------')
    print('')
