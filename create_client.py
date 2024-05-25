import subprocess


def create_client(user):
    ip_address = f'10.24.{user.id // 255}.{user.id + 1 % 255}'
    print(user.username, ip_address)
    subprocess.run(['bash', '/etc/wireguard/create_client.sh', user.username, ip_address], capture_output=True, text=True)
