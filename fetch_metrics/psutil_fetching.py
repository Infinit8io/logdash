import psutil
import os
import uuid
from datetime import datetime

# The psutil documentation : http://pythonhosted.org/psutil/

def psutil_fetching():
    '''psutil experimentation fetching some metrics'''

    # CPU metrics
    machine_platform = os.name
    machine_sysname = os.uname()[0]
    machine_name = os.uname()[1]
    machine_version = os.uname()[3]
    machine_uid = os.getuid()

    machine_sexymac = ':'.join(("%012X" % uuid.getnode())[i:i+2] for i in range(0, 12, 2))
    machine_slugmac = ''.join(("%012X" % uuid.getnode())[i:i+2] for i in range(0, 12, 2))

    # CPU logs
    cpu_usage_percentage = psutil.cpu_percent(interval = 1)
    cpu_number_logical = psutil.cpu_count()
    cpu_number_physical = psutil.cpu_count(logical=False)

    cpu_times = psutil.cpu_times()

    cpu_time_user = cpu_times[0]
    cpu_time_nice = cpu_times[1]
    cpu_time_system = cpu_times[2]
    cpu_time_idle = cpu_times[3]
    cpu_time_iowait =  cpu_times[4]

    cpu_per_cpu_percentage = psutil.cpu_percent(interval=1, percpu=True)

    # Temperatures
    # temperatures = psutil.sensors_temperatures() # Looks like it doesn't work

    # Batteries
    batteries = psutil.sensors_battery()

    # Processes
    processes = [proc.as_dict(attrs=['status', 'pid', 'name', 'username', 'cpu_num']) for proc in psutil.process_iter()]

    # Disks
    disk_usage = psutil.disk_usage("/") # Root disk usage

    # Networks
    connections = psutil.net_connections(kind='inet4')

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
        'metrics': {
            'cpu':[
                {
                'took_at':                  datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'cpu_usage_percentage':     cpu_usage_percentage,
                'cpu_number_logical':       cpu_number_logical,
                'cpu_number_physical':      cpu_number_physical,
                'cpu_per_cpu_percentage':   cpu_per_cpu_percentage,
                'cpu_times': [
                    {
                    'user':     cpu_time_user,
                    'nice':     cpu_time_nice,
                    'system':   cpu_time_system,
                    'idle':     cpu_time_idle,
                    'iowait':   cpu_time_iowait,
                    }
                ]
                }
            ],
            'memory': [
                {
                'memory_total':     memory[0],
                'memory_available': memory[1],
                'memory_percent':   memory[2],
                'memory_used':      memory[3],
                'memory_free':      memory[4],
                'memory_active':    memory[5],
                'memory_inactive':  memory[6],
                }
            ],
            'process': [
                {
                'process_nb':           len(processes),
                'process_sleeping_nb':  len([p for p in processes if p["status"] == "sleeping"]),
                'process_running_nb':   len([p for p in processes if p["status"] == "running"]),
                'process_stopped_nb':   len([p for p in processes if p["status"] == "stopped"]),
                'processes':            processes,
                }
            ],
            'disks': [
                {
                'disk_total':   disk_usage[0],
                'disk_used':    disk_usage[1],
                'disk_free':    disk_usage[2],
                'disk_percent': disk_usage[3],
                }
            ],
            'batteries' : [
                {
                    'battery_percentage': batteries[0],
                    'battery_time_left':  batteries[1],
                    'battery_plugged':    batteries[2],
                }
            ],
        },
    }

    return log
