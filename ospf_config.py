from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import ConnectError, RpcError, ConfigLoadError, CommitError



devices = [
    {
        # RouterC
        "mgnt_ip": "insert management address",
        'if_config': {
            'ge-0/0/1': "72.114.96.10/30", # I designed this network topology, can make your own
            'ge-0/0/2': "72.114.97.1/24",
            'ge-0/0/3': "72.114.96.13/30",
            'lo0': "72.114.96.18/32"
            },
        'ospf_config': {
            
            "0.0.0.20": ['ge-0/0/1','ge-0/0/2', 'ge-0/0/3','lo0']
            }
    },
    
    {
        # RouterD
        "mgnt_ip": "insert management IP address",
        'if_config': {
            'ge-0/0/1': "72.114.100.11/24",
            'ge-0/0/2': "72.114.96.9/30",
            'ge-0/0/3': "72.114.96.6/30",
            'lo0': "72.114.96.19/32"
            },
        'ospf_config': {
            
            "0.0.0.20": ['ge-0/0/1','ge-0/0/2', 'lo0'],
            "0.0.0.0": ['ge-0/0/3']
            }
    }
]


for dev in devices:
    device = Device(host = dev['mgnt_ip'], user = 'user', password = 'password')
    device.open()
    device.bind(conf = Config)
    var_dict = {'device_config': dev}
    device.conf.load(template_path = 'template.conf', template_vars = var_dict, merge = True)
    device.conf.commit()
    
    
    
