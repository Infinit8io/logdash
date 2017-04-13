import psutil
import os
import uuid
import collections
import time

import json

# The psutil documentation : http://pythonhosted.org/psutil/

def psutil_fetching():
    '''psutil experimentation fetching some metrics'''

    # CPU metrics
    machine_platform = os.name
    machine_sysname = os.uname()[0]
    machine_name = os.uname()[1]
    machine_version = os.uname()[3]
    machine_uid = os.getuid()

    machine_sexymac = ':'.join('{:02x}'.format(b) for b in uuid.getnode().to_bytes(6, 'big')) # Thanks @greut
    machine_slugmac = "{:012x}".format(uuid.getnode())

    # CPU logs
    cpu_usage_percentage = psutil.cpu_percent(interval = 1)
    cpu_number_logical = psutil.cpu_count()
    cpu_number_physical = psutil.cpu_count(logical=False)

    cpu_times = psutil.cpu_times()

    cpu_per_cpu_percentage = psutil.cpu_percent(interval=1, percpu=True)

    # Temperatures
    # temperatures = psutil.sensors_temperatures() # Looks like it doesn't work

    # Batteries
    batteries = psutil.sensors_battery()

    # Processes
    processes = [proc.as_dict(attrs=['status', 'pid', 'name', 'username', 'cpu_num']) for proc in psutil.process_iter()]
    process_counter = collections.Counter([proc["status"] for proc in processes])

    # Disks
    disk_usage = psutil.disk_usage("/") # Root disk usage

    # Networks
    connections = psutil.net_connections(kind='inet4')
    net_adresses = psutil.net_if_addrs()
    network_interfaces = {interface : net_adresses[interface][0].address for interface in net_adresses}
    network_interfaces = collections.OrderedDict(sorted(network_interfaces.items()))

    # Memory
    memory = psutil.virtual_memory()

    # Generating log
    log = {
        'machine_name':     machine_name,       # dom-hp-elitebook
        'machine_sysname':  machine_sysname,    # Linux
        'machine_version':  machine_version,    # #93-Ubuntu SMP Fri Mar...
        'machine_platform': machine_platform,   # Posix
        'machine_mac':      machine_sexymac,    # 80:86:F2:67:88:74
        'machine_slug':     machine_slugmac,    # 8086F2678874
        'metrics_took_at':  time.time(),
        'metrics': {
            'cpu':
                {
                'cpu_usage_percentage':     cpu_usage_percentage,
                'cpu_number_logical':       cpu_number_logical,
                'cpu_number_physical':      cpu_number_physical,
                'cpu_per_cpu_percentage':   cpu_per_cpu_percentage,
                'cpu_times':                cpu_times._asdict(),
                },
            'memory': psutil.virtual_memory()._asdict(),
            'process':
                {
                'process_nb':           len(processes),
                'process_sleeping_nb':  process_counter.get("sleeping", 0),
                'process_running_nb':   process_counter.get("running", 0),
                'process_stopped_nb':   process_counter.get("stopped", 0),
                'processes':            processes,
                },
            'disk': disk_usage._asdict(),
            'network': [network_interfaces,],
            'battery' : batteries._asdict(),
        },
    }

    return log

if __name__ == "__main__":
    print(json.dumps(psutil_fetching(), indent=4))
    #print(json.dumps(psutil.virtual_memory()._asdict()))
