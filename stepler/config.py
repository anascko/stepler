"""
------
Config
------
"""

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import functools
import json
import os
import socket
import uuid

from six.moves.urllib.parse import urlparse

import stepler.hacking  # noqa F401

from stepler.third_party.utils import generate_ids

BASE_PREFIX = os.environ.get('BASE_PREFIX', 'stepler')
STEPLER_PREFIX = '{}-{}'.format(
    BASE_PREFIX, str(uuid.uuid4())[:4])  # resources unique prefix
# TODO(schipiga): inject STEPLER_PREFIX to prevent cross imports problem.
generate_ids = functools.partial(generate_ids, _stepler_prefix=STEPLER_PREFIX)

socket.setdefaulttimeout(60)

DEBUG = bool(os.environ.get('DEBUG', False))

PROJECT_DOMAIN_NAME = os.environ.get('OS_PROJECT_DOMAIN_NAME', 'default')
USER_DOMAIN_NAME = os.environ.get('OS_USER_DOMAIN_NAME', 'default')
PROJECT_NAME = os.environ.get('OS_PROJECT_NAME', 'admin')
USERNAME = os.environ.get('OS_USERNAME', 'admin')
PASSWORD = os.environ.get('OS_PASSWORD', 'password')

# If AUTH_URL is undefined, corresponding fixture raises exception.
# AUTH_URL absence doesn't raise exception here, because for docs generation
# and unittests launching this variable doesn't need.
AUTH_URL = os.environ.get('OS_AUTH_URL')

if AUTH_URL:  # figure out keystone API version
    AUTH_URL = AUTH_URL.rstrip('/')  # remove last slash if it is present
    version = AUTH_URL.rsplit('/')[-1]  # get version tail
    versions = ('v2.0', 'v3')
    # Versionless AUTH_URL looks like http://1.2.3.4/identity
    if version not in versions:
        KEYSTONE_API_VERSION = int(
            os.environ.get('OS_IDENTITY_API_VERSION', 3))
        AUTH_URL = '{}/v{}'.format(AUTH_URL, KEYSTONE_API_VERSION)
        if KEYSTONE_API_VERSION == 2:
            AUTH_URL = '{}/v{}'.format(AUTH_URL, '2.0')

    else:
        assert version in versions, \
            "OS_AUTH_URL must have tail among values {!r}.".format(versions)

        KEYSTONE_API_VERSION = 3 if version == 'v3' else 2

UBUNTU_QCOW2_URL = 'https://cloud-images.ubuntu.com/trusty/current/trusty-server-cloudimg-amd64-disk1.img'  # noqa E501
UBUNTU_XENIAL_QCOW2_URL = 'https://cloud-images.ubuntu.com/xenial/current/xenial-server-cloudimg-amd64-disk1.img'  # noqa E501
FEDORA_QCOW2_URL = 'https://download.fedoraproject.org/pub/fedora/linux/releases/23/Cloud/x86_64/Images/Fedora-Cloud-Base-23-20151030.x86_64.qcow2'  # noqa E501
CIRROS_QCOW2_URL = 'http://download.cirros-cloud.net/0.3.4/cirros-0.3.4-x86_64-disk.img'  # noqa E501
UBUNTU_ISO_URL = 'http://archive.ubuntu.com/ubuntu/dists/trusty/main/installer-amd64/current/images/netboot/mini.iso'  # noqa E501
BAREMETAL_UBUNTU = 'http://mos-ironic.vm.mirantis.net/ipukha/dib-user-image-dkms-grub.raw'  # noqa E501
BAREMETAL_VIRTUAL_UBUNTU = UBUNTU_XENIAL_QCOW2_URL
CONNTRACK_CIRROS_IMAGE = 'https://github.com/gdyuldin/ping/raw/master/cirros-0.3.4-x86_64-disk.img'  # noqa E501
CUSTOM_PING_COMMAND_PATH = '/usr/bin/fix_id_ping'

FORCE_API = bool(os.environ.get('FORCE_API_USAGE'))

# TODO(schipiga): copied from mos-integration-tests, need refactor.
TEST_IMAGE_PATH = os.environ.get("TEST_IMAGE_PATH",
                                 os.path.expanduser('~/images'))

TEST_REPORTS_DIR = os.environ.get(
    "TEST_REPORTS_DIR",
    os.path.join(os.getcwd(),  # put results to folder where tests are launched
                 "test_reports"))

TEST_REPORTS_DIR = os.path.abspath(os.path.expanduser(TEST_REPORTS_DIR))
if not os.path.exists(TEST_REPORTS_DIR):
    os.mkdir(TEST_REPORTS_DIR)

GOOGLE_DNS_IP = '8.8.8.8'

ANSIBLE_EXECUTION_MAX_TIMEOUT = 1200

# IMAGE / SERVER CREDENTIALS
CIRROS_USERNAME = 'cirros'
CIRROS_PASSWORD = 'cubswin:)'
UBUNTU_USERNAME = 'ubuntu'

CIRROS_ENV_PATH = 'PATH=$PATH:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'  # noqa

# CURRENT API VERSIONS
CURRENT_NOVA_VERSION = '2'
CURRENT_GLANCE_VERSION = '2'
CURRENT_CINDER_VERSION = '2'
CURRENT_IRONIC_VERSION = '1'
CURRENT_IRONIC_MICRO_VERSION = '1.9'

# SERVICES
CINDER = 'cinder'
CINDERV2 = 'cinderv2'
CINDER_BACKUP = 'cinder-backup'
CINDER_API = 'cinder-api'
CINDER_SCHEDULER = 'cinder-scheduler'
CINDER_VOLUME = 'cinder-volume'
CINDER_SERVICES = (CINDER_API, CINDER_SCHEDULER, CINDER_VOLUME)
GLANCE = 'glance'
GLANCE_API = 'glance-api'
GLANCE_GLARE = 'glance-glare'
GLANCE_REGISTRY = 'glance-registry'
GLANCE_SERVICES = (GLANCE_API, GLANCE_GLARE, GLANCE_REGISTRY)
KEYSTONE = 'keystone'
NOVA = 'nova'
NOVA20 = 'nova20'
NOVA_EC2 = 'nova-ec2'
NOVA_API = 'nova-api'
NOVA_COMPUTE = 'nova-compute'
IRONIC_API = 'ironic-api'
IRONIC_CONDUCTOR = 'ironic-conductor'
HORIZON = 'horizon'
SWIFT = 'swift'
RABBITMQ = 'rabbitmq'
MYSQL = 'mysql'
CEILOMETER = 'ceilometer'
HEAT = 'heat'
HEAT_CNF = 'heat-cfn'

# STATUSES
STATUS_ACTIVE = 'active'
STATUS_ATTACHING = 'attaching'
STATUS_AVAILABLE = 'available'
STATUS_AWAITING_TRANSFER = 'awaiting-transfer'
STATUS_BUILD = 'build'
STATUS_CREATING = 'creating'
STATUS_DELETING = 'deleting'
STATUS_DETACHING = 'detaching'
STATUS_DOWNLOADING = 'downloading'
STATUS_ERROR = 'error'
STATUS_FAILED = 'FAILED'
STATUS_HARD_REBOOT = 'hard_reboot'
STATUS_INUSE = 'in-use'
STATUS_MIGRATING = 'migrating'
STATUS_OK = 'OK'
STATUS_PAUSED = 'paused'
STATUS_PAUSING = 'pausing'
STATUS_QUEUED = 'queued'
STATUS_REBOOT = 'reboot'
STATUS_REBUILD = 'rebuild'
STATUS_REBUILD_SPAWNING = 'rebuild_spawning'
STATUS_REBUILDING = 'rebuilding'
STATUS_RESCUE = 'rescue'
STATUS_RESCUING = 'rescuing'
STATUS_RESIZE = 'resize'
STATUS_SHELVED = 'shelved'
STATUS_SHELVED_OFFLOADED = 'shelved_offloaded'
STATUS_SHUTOFF = 'shutoff'
STATUS_SOFT_DELETED = 'soft_deleted'
STATUS_SUCCESS = 'success'
STATUS_UNREACHABLE = 'UNREACHABLE'
STATUS_UPDATING = 'updating'
STATUS_UPLOADING = 'uploading'
STATUS_VERIFY_RESIZE = 'verify_resize'

# TIMEOUTS (in seconds)
# TODO(kromanenko): Investigate less intensive good polling interval value.
POLLING_TIME = 1

# Cinder
VOLUME_AVAILABLE_TIMEOUT = 5 * 60
VOLUME_DELETE_TIMEOUT = 3 * 60
VOLUME_IN_USE_TIMEOUT = 60
VOLUME_ATTACH_TIMEOUT = 60
VOLUME_SHOW_TIMEOUT = 60
SNAPSHOT_AVAILABLE_TIMEOUT = 5 * 60
SNAPSHOT_SHOW_TIMEOUT = 60
SNAPSHOT_CREATE_TIMEOUT = 3 * 60
SNAPSHOT_DELETE_TIMEOUT = 3 * 60
VOLUME_RETYPE_TIMEOUT = 60
CINDER_VOLUME_MAX_SIZE_QUOTA_VALUE = 20
CINDER_VOLUMES_QUOTA_BIG_VALUE = 100
CINDER_SNAPSHOTS_QUOTA_BIG_VALUE = 200
CINDER_BACKUPS_QUOTA_BIG_VALUE = 200
POLICY_NEVER = 'never'
VOLUME_HOST_ATTR = 'os-vol-host-attr:host'
VOLUME_HOST_POSTFIX = '@LVM-backend#LVM-backend'
BACKUP_AVAILABLE_TIMEOUT = 5 * 60
BACKUP_SHOW_TIMEOUT = 60
BACKUP_DELETE_TIMEOUT = 3 * 60
TRANSFER_CREATE_TIMEOUT = 3 * 60
TRANSFER_SHOW_TIMEOUT = 60
VOLUMES_CREATE_CHUNK = 5

# Glance
IMAGE_AVAILABLE_TIMEOUT = 5 * 60
IMAGE_QUEUED_TIMEOUT = 30
BAREMETAL_DISK_INFO = [{"name": "sda",
                        "extra": [],
                        "free_space": 11000,
                        "type": "disk",
                        "id": "sda",
                        "size": 11000,
                        "volumes": [{"mount": "/",
                                     "type": "partition",
                                     "file_system": "ext4",
                                     "size": 10000}]}]
BAREMETAL_VIRTUAL_DISK_INFO = [{"name": "vda",
                                "extra": [],
                                "free_space": 9000,
                                "type": "disk",
                                "id": "vda",
                                "size": 9000,
                                "volumes": [{"mount": "/",
                                             "type": "partition",
                                             "file_system": "ext4",
                                             "size": 8000}]}]

IMAGE_VISIBILITY_PUBLIC = 'public'
IMAGE_VISIBILITY_SHARED = 'shared'
GLANCE_API_CONFIG_PATH = os.environ.get('GLANCE_API_CONFIG_PATH',
                                        '/etc/glance/glance-api.conf')
GLANCE_SWIFT_CONFIG_PATH = os.environ.get('GLANCE_SWIFT_CONFIG_PATH',
                                          '/etc/glance/glance-swift.conf')
GLANCE_USER = 'glance'


# Nova
CREDENTIALS_PREFIX = 'stepler_credentials_'
EPHEMERAL_MNT_FS_PATH = '/mnt'
DISK_TIMESTAMP_FILE = 'timestamp.txt'
DISK_TIMESTAMP_FILE_FULL_PATH = (EPHEMERAL_MNT_FS_PATH + '/' +
                                 DISK_TIMESTAMP_FILE)
NOVA_API_LOG_FILE = '/var/log/nova/nova-api.log'
NOVA_CONFIG_PATH = '/etc/nova/nova.conf'
EPHEMERAL_ROOT_FS_PATH = '/'
DEFAULT_QCOW_IMAGE_SIZE = '20G'

FLAVOR_MICRO = 'm1.micro'
FLAVOR_TINY = 'm1.tiny'
FLAVOR_SMALL = 'm1.small'
BAREMETAL_RAM = 8192
BAREMETAL_VCPUS = 4
BAREMETAL_DISK = 150

BAREMETAL_VIRTUAL_RAM = 1024
BAREMETAL_VIRTUAL_VCPUS = 1
BAREMETAL_VIRTUAL_DISK = 10

ROLE_MEMBER = '_member_'
ROLE_ADMIN = 'admin'

PING_CALL_TIMEOUT = 5 * 60
PING_BETWEEN_SERVERS_TIMEOUT = 10 * 60
USERDATA_EXECUTING_TIMEOUT = 20 * 60
ROUTER_NAMESPACE_TIMEOUT = 15
SSH_CLIENT_TIMEOUT = 60
SSH_CONNECT_TIMEOUT = 8 * 60
LIVE_MIGRATE_TIMEOUT = 10 * 60
VERIFY_RESIZE_TIMEOUT = 3 * 60
EVACUATE_TIMEOUT = 3 * 60
SOFT_DELETED_TIMEOUT = 30
SERVER_DELETE_TIMEOUT = 3 * 60
SERVER_ACTIVE_TIMEOUT = 14 * 60
SERVER_UPDATE_TIMEOUT = 2 * 60
SERVER_SHELVE_TIMEOUT = 5 * 60
SERVER_SHUTOFF_TIMEOUT = 3 * 60
SERVER_ERROR_TIMEOUT = 60
UBUNTU_BOOT_COMPLETE_TIMEOUT = 10 * 60

REBOOT_SOFT = 'SOFT'
REBOOT_HARD = 'HARD'

KEYSTONE_AVAILABILITY_TIMEOUT = 10 * 60
NOVA_AVAILABILITY_TIMEOUT = 10 * 60
NEUTRON_AVAILABILITY_TIMEOUT = 5 * 60
CINDER_AVAILABILITY_TIMEOUT = 30
SERVICE_REBALANCE_TIMEOUT = 2 * 60

TIME_AFTER_KEYSTONE_RESTART = 5

SSH_COMMAND_TIMEOUT = 30

USERDATA_DONE_MARKER = 'userdata-done %s' % uuid.uuid4()

INSTALL_LM_WORKLOAD_USERDATA = """#!/bin/bash -v
apt-get install -yq stress cpulimit sysstat iperf
echo {}""".format(USERDATA_DONE_MARKER)

INSTALL_QEMU_UTILS_USERDATA = """#!/bin/bash -v
apt-get install -y qemu-utils
echo {}""".format(USERDATA_DONE_MARKER)

IPERF_TCP_PORT = 5001
IPERF_UDP_PORT = 5002
RABBIT_PORT = 5673

START_IPERF_USERDATA = """#!/bin/bash -v
apt-get install -yq iperf
iperf -s -p {tcp_port} <&- > /tmp/iperf.log 2>&1 &
iperf -u -s -p {udp_port} <&- > /tmp/iperf_udp.log 2>&1 &
echo {marker}""".format(
    tcp_port=IPERF_TCP_PORT,
    udp_port=IPERF_UDP_PORT,
    marker=USERDATA_DONE_MARKER)

SMALL_RECLAIM_INTERVAL = str(30)
BIG_RECLAIM_INTERVAL = str(24 * 60 * 60)
SMALL_RECLAIM_TIMEOUT = 3 * int(SMALL_RECLAIM_INTERVAL)
NOVA_INSTANCES_PATH = "/var/lib/nova/instances/"

FIXED_IP = 'fixed'
FLOATING_IP = 'floating'

SERVER_ATTR_FLAVOR = 'flavor'
SERVER_ATTR_HOST = 'OS-EXT-SRV-ATTR:host'
SERVER_ATTR_HYPERVISOR_HOSTNAME = 'OS-EXT-SRV-ATTR:hypervisor_hostname'
SERVER_ATTR_INSTANCE_NAME = 'OS-EXT-SRV-ATTR:instance_name'
SERVER_ATTR_LOCKED = 'locked'
SERVER_ATTR_DESCRIPTION = 'description'
SERVER_ATTR_FAULT = 'fault'


IO_SPEC_LIMIT = 10240000
IO_SPEC_LIMIT_METADATA = {'quota:disk_read_bytes_sec': str(IO_SPEC_LIMIT),
                          'quota:disk_write_bytes_sec': str(IO_SPEC_LIMIT)}
EVACUATE_SERVERS_COUNT = 2
USER_FILES_FOR_TEST_REBUILD = {"/home/ubuntu/file1.txt": 'Test file 1',
                               "/home/ubuntu/file2.txt": 'Test file 2',
                               "/home/ubuntu/file3.txt": 'Test file 3',
                               "/home/ubuntu/file4.txt": 'Test file 4',
                               "/home/ubuntu/file5.txt": 'Test file 5'}
DESCRIPTION_FOR_TEST_REBUILD = "Description added during rebuild"

SERVERS_CREATE_CHUNK = 5
LIVE_MIGRATE_MAX_SERVERS_COUNT = 10

DPDK_ENABLED = bool(os.environ.get('DPDK_ENABLED', False))

# Default flavor
if DPDK_ENABLED:
    DEFAULT_FLAVOR_RAM = int(os.environ.get('DEFAULT_FLAVOR_RAM', 2048))
    DEFAULT_FLAVOR_CPU = int(os.environ.get('DEFAULT_FLAVOR_CPU', 1))
    DEFAULT_FLAVOR_DISK = int(os.environ.get('DEFAULT_FLAVOR_DISK', 10))
    DEFAULT_FLAVOR_METADATA = json.loads(os.environ.get(
        'DEFAULT_FLAVOR_METADATA', '{"hw:mem_page_size": "large"}'))
else:
    DEFAULT_FLAVOR_RAM = int(os.environ.get('DEFAULT_FLAVOR_RAM', 512))
    DEFAULT_FLAVOR_CPU = int(os.environ.get('DEFAULT_FLAVOR_CPU', 1))
    DEFAULT_FLAVOR_DISK = int(os.environ.get('DEFAULT_FLAVOR_DISK', 5))
    DEFAULT_FLAVOR_METADATA = json.loads(os.environ.get(
        'DEFAULT_FLAVOR_METADATA', '{}'))

DEFAULT_FLAVOR_PARAMS = dict(
    ram=DEFAULT_FLAVOR_RAM,
    vcpus=DEFAULT_FLAVOR_CPU,
    disk=DEFAULT_FLAVOR_DISK,
    metadata=DEFAULT_FLAVOR_METADATA)

# Glance
GLANCE_AVAILABILITY_TIMEOUT = 15
GLANCE_CONFIG_PATH = '/etc/glance/glance-api.conf'
GLANCE_IMAGES_PATH = '/var/lib/glance'
GLANCE_USER_STORAGE_QUOTA = 604979776

INGRESS = 'ingress'
EGRESS = 'egress'

SECURITY_GROUP_SSH_RULES = [
    {
        # ssh
        'direction': INGRESS,
        'protocol': 'tcp',
        'port_range_min': 22,
        'port_range_max': 22,
        'remote_ip_prefix': '0.0.0.0/0',
    }
]

SECURITY_GROUP_PING_RULES = [
    {
        # ping IPv4
        'direction': INGRESS,
        'protocol': 'icmp',
        'port_range_min': None,
        'port_range_max': None,
        'remote_ip_prefix': '0.0.0.0/0',
    }
]

SECURITY_GROUP_EGRESS_PING_RULE = {
    'direction': EGRESS,
    'protocol': 'icmp',
    'port_range_min': None,
    'port_range_max': None,
    'remote_ip_prefix': '0.0.0.0/0'
}


SECURITY_GROUP_SSH_PING_RULES = (SECURITY_GROUP_SSH_RULES +
                                 SECURITY_GROUP_PING_RULES)

# Heat
HEAT_VERSION = 1
HEAT_IN_PROGRESS_STATUS = 'in_progress'
HEAT_COMPLETE_STATUS = 'complete'
STACK_STATUS_CREATE_COMPLETE = 'create_complete'
STACK_STATUS_UPDATE_COMPLETE = 'update_complete'
STACK_STATUS_SUSPEND_COMPLETE = 'suspend_complete'
STACK_STATUS_RESUME_COMPLETE = 'resume_complete'
STACK_STATUS_CHECK_COMPLETE = 'check_complete'
STACK_STATUS_DELETE_COMPLETE = 'delete_complete'
STACK_CREATION_TIMEOUT = 10 * 60
STACK_DELETING_TIMEOUT = 3 * 60
STACK_UPDATING_TIMEOUT = 5 * 60
STACK_PREVIEW_TIMEOUT = 60
STACK_SHOW_TIMEOUT = 60
STACK_SUSPEND_TIMEOUT = 60
STACK_RESUME_TIMEOUT = 60
STACK_CHECK_TIMEOUT = 3 * 60
STACK_CLI_TIMEOUT = 60
RESOURCE_NAME = 'stepler_cirros_image'
HEAT_SIMPLE_TEMPLATE_URL = 'https://raw.githubusercontent.com/openstack/heat-templates/master/hot/resource_group/resource_group.yaml'  # noqa

# Ironic
BAREMETAL_NETWORK = 'baremetal'
BAREMETAL_NETWORK_DEVSTACK = 'ironic-provision'
BAREMETAL_NODE = bool(os.environ.get('BAREMETAL_NODE', False))

# Ceilometer
CEILOMETER_CONFIG_PATH = '/etc/ceilometer/ceilometer.conf'

# CLI clients
SERVER_LIST_TIMEOUT = 60
MIGRATION_START_TIMEOUT = 15
LIVE_EVACUATE_CLI_TIMEOUT = 60
LIVE_EVACUATE_TIMEOUT = 5 * 60
IMAGE_CREATION_TIMEOUT = 60
IMAGE_DOWNLOAD_TIMEOUT = 60

# For DevStack cmd should looks like `source devstack/openrc admin admin`
OPENRC_ACTIVATE_CMD = os.environ.get('OPENRC_ACTIVATE_CMD', 'source /root/openrc')  # noqa E501

CLEANUP_UNEXPECTED_BEFORE_TEST = bool(
    os.environ.get('CLEANUP_UNEXPECTED_BEFORE_TEST', False))

CLEANUP_UNEXPECTED_AFTER_TEST = bool(
    os.environ.get('CLEANUP_UNEXPECTED_AFTER_TEST', False))

CLEANUP_UNEXPECTED_AFTER_ALL = bool(
    os.environ.get('CLEANUP_UNEXPECTED_AFTER_ALL', False))

UNEXPECTED_VOLUMES_LIMIT = int(
    os.environ.get('UNEXPECTED_VOLUMES_LIMIT', 0))


# Neutron
NEUTRON_L3_SERVICE = 'neutron-l3-agent'
NEUTRON_DHCP_SERVICE = 'neutron-dhcp-agent'
NEUTRON_OVS_SERVICE = 'neutron-openvswitch-agent'
NEUTRON_METADATA_SERVICE = 'neutron-metadata-agent'
NEUTRON_SERVER_SERVICE = 'neutron-server'
NEUTRON = 'neutron'

DNSMASQ_SERVICE = 'dnsmasq'

NEUTRON_AGENT_DIE_TIMEOUT = 60
NEUTRON_AGENT_ALIVE_TIMEOUT = 5 * 60
NEUTRON_OVS_RESTART_MAX_PING_LOSS = 50
NEUTRON_OVS_RESTART_MAX_ARPING_LOSS = 50
NEUTRON_OVS_RESTART_MAX_IPERF_LOSS = 50
NEUTRON_L3_HA_RESTART_MAX_PING_LOSS = 100

SERVICE_TERMINATE_TIMEOUT = 60
SERVICE_START_TIMEOUT = 60
AGENT_RESCHEDULING_TIMEOUT = 3 * 60
FLOATING_IP_DETACH_TIMEOUT = 30
FLOATING_IP_BIND_TIMEOUT = 5 * 60

NEUTRON_UPDATE_SEC_GROUP_RULES_TIMEOUT = 30

TAP_INTERFACE_UP_TIMEOUT = 3 * 60
CONNECT_RESTORE_TIMEOUT = 3 * 60

AGENT_LOGS = {
    # logs on controllers, computes and gtw nodes
    NEUTRON_L3_SERVICE: ['/var/log/neutron/l3-agent.log',  # controller
                         '/var/log/neutron/neutron-l3-agent.log',  # compute
                         '/var/log/neutron/neutron-l3-agent.log'],  # gtw
    NEUTRON_DHCP_SERVICE: ['/var/log/neutron/dhcp-agent.log',  # controller
                           None,  # file is absent on compute
                           '/var/log/neutron/neutron-dhcp-agent.log'],  # gtw
    NEUTRON_OVS_SERVICE: ['/var/log/neutron/openvswitch-agent.log',
                          '/var/log/neutron/neutron-openvswitch-agent.log',
                          '/var/log/neutron/neutron-openvswitch-agent.log'],
    NEUTRON_METADATA_SERVICE: ['/var/log/neutron/metadata-agent.log',
                               '/var/log/neutron/neutron-metadata-agent.log',
                               '/var/log/neutron/neutron-metadata-agent.log'],
    NEUTRON_SERVER_SERVICE: ['/var/log/neutron/neutron-server.log',
                             None,
                             None],
}

NEUTRON_ML2_CONFIG_PATH = '/etc/neutron/plugins/ml2/ml2_conf.ini'
NEUTRON_CONFIG_PATH = '/etc/neutron/neutron.conf'
NEUTRON_L3_CONFIG_PATH = '/etc/neutron/l3_agent.ini'
STR_L3_AGENT_NOTIFICATION = 'Got routers updated notification'
STR_ERROR_GATEWAY_PORT = 'Could not retrieve gateway port for subnet'

ERROR_GATEWAY_PORT_CHECK_TIME = 30

STR_ERROR = 'ERROR'
STR_TRACE = 'TRACE'
STR_SIGHUP = 'SIGHUP'
STR_NEUTRON_API_V2_ERROR = 'neutron.api.v2.resource'

NETWORK_TYPE_VLAN = 'vlan'
NETWORK_TYPE_VXLAN = 'vxlan'

HA_STATE_ACTIVE_ATTRS = {'ha_state': 'active'}

ROUTER_AVAILABLE_TIMEOUT = 60

LOCAL_CIDR = u'192.168.3.0/24'
LOCAL_IPS = ['192.168.3.{}'.format(i) for i in range(1, 254)]

PORT_DEVICE_OWNER_ROUTER_GATEWAY = 'network:router_gateway'
PORT_DEVICE_OWNER_SERVER = 'compute:nova'
PORT_DEVICE_OWNER_DHCP = 'network:dhcp'
PORT_DEVICE_ID_RESERVED_DHCP = 'reserved_dhcp_port'

PORT_BINDING_HOST_ID = 'binding:host_id'

HA_L3_AGENT_APPEARING_TIMEOUT = 60

# Horizon
BROWSER_WINDOW_SIZE = map(
    int, (os.environ.get('BROWSER_WINDOW_SIZE', ('1920,1080'))).split(','))

UI_TIMEOUT = 30
ACTION_TIMEOUT = 60
EVENT_TIMEOUT = 180

BIG_FILE_SIZE = 1024 * 1024 * 1024 * 100  # 100 Gb
LONG_ACTION_TIMEOUT = 60 * 60  # 1 hour (timeout for 'Working')
LONG_EVENT_TIMEOUT = 60 * 60 * 3  # 3 hours (timeout for 'Saving')

OS_DASHBOARD_URL = os.environ.get('OS_DASHBOARD_URL')  # should be defined!
VIRTUAL_DISPLAY = os.environ.get('VIRTUAL_DISPLAY')

ADMIN_NAME, ADMIN_PASSWD, ADMIN_PROJECT = list(generate_ids('admin', count=3))
USER_NAME, USER_PASSWD, USER_PROJECT = list(generate_ids('user', count=3))

FLOATING_NETWORK_NAME = os.environ.get('OS_FLOATING_NETWORK',
                                       'admin_floating_net')
INTERNAL_NETWORK_NAME = next(generate_ids('internal_net'))
INTERNAL_SUBNET_NAME = next(generate_ids('internal_subnet'))
ROUTER_NAME = next(generate_ids('router'))

EXTERNAL_ROUTER = 'router:external'

XVFB_LOCK = '/tmp/xvfb.lock'

HORIZON_TEST_FLAVOR = FLAVOR_MICRO
HORIZON_TEST_IMAGE = 'TestVM'

# Volume creating constants
IMAGE_SOURCE = 'Image'
VOLUME_SOURCE = 'Volume'

NODES_AVAILABILITY_TIMEOUT = 5 * 60
NODE_REBOOT_TIMEOUT = 10 * 60
TCPDUMP_LATENCY = 2

# Horizon
HORIZON_CONFIG_PATH = os.environ.get(
    'HORIZON_CONFIG_PATH', '/etc/openstack-dashboard/local_settings.py')

# Openstack workload
OS_LOAD_SCRIPTS_DIR = os.path.join(os.path.dirname(__file__),
                                   'workload_scripts')
OS_LOAD_GENERATOR = 'os_load_generator.py'
DELAY_AFTER_OS_WORKLOAD_START = 15

# RabbitMQ
RABBITMQ_CONFIG = '/etc/rabbitmq/rabbitmq.config'
RABBITMQ_CHECK_CLUSTER_CMD = 'rabbitmqctl cluster_status'
TIME_AFTER_RABBITMQ_STOP = 3 * 60

# keepalived
START_KEEPALIVED_CMD = '/etc/init.d/keepalived start'
STOP_KEEPALIVED_CMD = '/etc/init.d/keepalived stop'
KILL9_KEEPALIVED_CMD = 'pkill -9 keepalived'
TIME_AFTER_KEEPALIVED_START = 5
TIME_AFTER_KEEPALIVED_STOP = 5

# Cloud-specific variables

TCP_CLOUD = 'tcpcloud'

# Check if current node is fuel primary controller
FUEL_PRIMARY_CONTROLLER_CMD = "hiera roles | grep primary-controller"
FUEL_NON_PRIMARY_CONTROLLERS_CMD = ("hiera roles | grep controller | "
                                    "grep -v primary-controller")

# Command to shutdown br-ex
SHUTDOWN_BR_EX_CMD = "ip link set br-ex down"

# In TCP clouds, controller holding VIP is found via OS_AUTH_URL
# http://10.109.4.6:5000/v3 -> 10.109.4.6
if AUTH_URL:
    VIP = urlparse(AUTH_URL).hostname
    TCP_VIP_CONTROLLER_CMD = "ip a | grep -w {}".format(VIP)

TCP_KVM_NODE_CMD = "salt-call pillar.get salt:control:enabled | grep True"
TCP_MON_NODE_CMD = "salt-call pillar.get influxdb:server:enabled | grep True"
TCP_GET_INFLUXDB_DATA_CMD = "salt-call pillar.get --out=yaml influxdb:server"

INFLUX_CMD = ("/usr/bin/influx -database {database} -username {username} "
              "-password {password} -host {host} -port {port}")

TCP_CHECK_METRICS_CMD = (INFLUX_CMD +
                         " -execute 'select * from mysql_check where "
                         "time > now() - {time_sec}s'")
TCP_CHECK_ALARMS_CMD1 = (INFLUX_CMD +
                         " -execute 'select * from status where value>0 and "
                         "hostname!='cfg' and time > now() - {time_sec}s'")
TCP_CHECK_ALARMS_CMD2 = (INFLUX_CMD +
                         " -execute 'select * from cluster_status where "
                         "value>0 and time > now() - {time_sec}s'")
TCP_EXPECTED_ALARM = 'nova_compute'

# Stacklight services
ELASTIC_SEARCH_SERVICE = 'elasticsearch'
GRAFANA_SERVICE = 'grafana-server'
INFLUXDB_SERVICE = 'influxdb'
KIBANA_SERVICE = 'kibana'
NAGIOS_SERVICE = 'nagios3'
STACKLIGHT_SERVICES = (ELASTIC_SEARCH_SERVICE, GRAFANA_SERVICE,
                       INFLUXDB_SERVICE, KIBANA_SERVICE, NAGIOS_SERVICE)

NODE_POWEROFF_TIMEOUT = 60
NODE_SHUTDOWN_TIMEOUT = 3 * 60
NOVA_SERVICES_UP_TIMEOUT = 5 * 60
NOVA_TIME_AFTER_SERVICES_UP = 30
NETWORK_OUTAGE_TIME = 5 * 60
TIME_BETWEEN_CLUSTER_RESTART = 5 * 60
TIME_BEFORE_NETWORK_DOWN = 5
TIME_NETWORK_DOWN = 4 * 60
NODES_ON_KVM_START_TIMEOUT = 5 * 60
TIME_AFTER_SHUTDOWN_KVM_NODE = 30
TIME_AFTER_START_MON_NODE = 60
TIME_BETWEEN_STOP_START_SERVICE = 120
TIME_BEFORE_ALARM_CHECK = 60

# Commands to create and remove file
CREATE_FILE_CMD = 'fallocate -l {size}K {file_path}'
REMOVE_FILE_CMD = 'rm -f {file_path}'

# Galera cluster
MYSQL_CONFIG_FILE = '/etc/mysql/my.cnf'
MYSQL_KILL_CMD = "pkill -9 mysqld && sleep 5"
TIME_AFTER_MYSQL_START = 5
GALERA_CLUSTER_STATUS_CHECK_CMD = "show status like 'wsrep%';"
GALERA_CLUSTER_START_CMD = "/usr/bin/mysqld_safe --wsrep-new-cluster &"
GALERA_CLUSTER_STATUS_PARAMS = {'wsrep_local_state_comment': 'Synced',
                                'wsrep_evs_state': 'OPERATIONAL',
                                'wsrep_cluster_status': 'Primary'}
GALERA_CLUSTER_SIZE_PARAM = "wsrep_cluster_size"
GALERA_CLUSTER_MEMBERS_PARAM = "wsrep_incoming_addresses"
GALERA_CLUSTER_UP_TIMEOUT = 3 * 60
GALERA_CLUSTER_DOWN_TIMEOUT = 2 * 60

TEST_DATABASE = 'stepler_test'
TEST_TABLE = 'test'

MYSQL_CREATE_TABLE_CMD = (
    "drop database if exists {0}; ".format(TEST_DATABASE) +
    "create database {0}; use {0}; ".format(TEST_DATABASE) +
    "create table {0}(count int); ".format(TEST_TABLE) +
    "insert into {0} values (11);".format(TEST_TABLE))
MYSQL_CHECK_TABLE_CMD = "use {0}; select * from {1};".format(
    TEST_DATABASE, TEST_TABLE)
MYSQL_DELETE_DATABASE_CMD = "drop database {0};".format(TEST_DATABASE)
MYSQL_EXPECTED_RESULT = 'count\n11'

MYSQL_PORT = 3306

S3_PORT = '8080'


RADOSGW_SOCK_FILE = '/var/run/ceph/ceph-client.radosgw.gateway.asok'

# NFV
CPU_PINNING_CMD_1 = ("grep isolcpus /proc/cmdline > /dev/null && "
                     "lscpu | grep 'NUMA node(s)'")
CPU_PINNING_CMD_2 = "grep isolcpus /proc/cmdline && lscpu | grep 'NUMA node'"
CPU_PINNING_CMD_3 = "grep MemTotal /sys/devices/system/node/node*/meminfo"
CANNOT_FIT_NUMA_TOPOLOGY = ('Requested instance NUMA topology cannot fit '
                            'the given host NUMA topology')

page_1gb = 1048576
page_2mb = 2048
HP_GET_DATA_CMD_1 = ("cat /sys/kernel/mm/hugepages/hugepages-{size}kB/"
                     "{type}_hugepages || echo 0")
HP_GET_DATA_CMD_2 = ("cat /sys/devices/system/node/node{numa_id}/hugepages/"
                     "hugepages-{size}kB/{type}_hugepages || echo 0")
TIME_AFTER_NOVA_COMPUTE_UP = 10
