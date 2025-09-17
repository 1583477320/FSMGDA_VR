import sys
import server
import logging
import config

logging.basicConfig(
    format='[%(levelname)s][%(asctime)s]: %(message)s', level=getattr(logging, 'INFO'), datefmt='%H:%M:%S')

def main():
    if len(sys.argv):
        # config_path = sys.argv[1]
        config_path = r'C:\Users\15834\PycharmProjects\FMGDA\FedCMOO\base_config.json'
        a = config.Config(config_path)
        s = server.Server(a)
        s.boot()
        t = s.train()
    else:
        print("No config json file provided!")

# def main():
#     exp_configs = [config.base_config_set('base_config.json', experiment = "MultiMNIST", algorithm= 'fedadam'),
#                 # config.base_config_set('base_config.json', experiment = "MultiMNIST", algorithm = 'fedcmoo'),
#               config.base_config_set('base_config.json', experiment = "MultiMNIST", algorithm= 'fsmgda')
#               # config.base_config_set('base_config.json', experiment = "MultiMNIST", algorithm= 'fedcmoo_pref'),
#               ]
#     print(exp_configs[0])


if __name__ == "__main__":
    main()