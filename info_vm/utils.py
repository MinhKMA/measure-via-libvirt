import configparser
from info_vm import setting


def ini_file_loader():
    """ Load configuration from ini file"""

    parser = configparser.SafeConfigParser()
    parser.read(setting.CONF_PATH)
    config_dict = {}

    for section in parser.sections():
        print(section)
        for key, value in parser.items(section, True):
            config_dict['%s-%s' % (section, key)] = value
    return config_dict


