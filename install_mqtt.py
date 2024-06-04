import subprocess
import time

def install_docker():
    print("Installing Docker...")
    time.sleep(2)
    subprocess.run(['sudo', 'apt-get', 'update'], check=True)
    subprocess.run(['sudo', 'apt-get', 'install', '-y', 'docker.io'], check=True)
    print("Done!")
    time.sleep(2)    
    print("Installing Docker-Compose...")
    time.sleep(2)
    subprocess.run(['sudo', 'apt-get', 'install', '-y', 'docker.io'], check=True)
    print("Done!")
    time.sleep(2)


def configure_mosquitto():
    print("Creating Directories")
    time.sleep(2)
    subprocess.run(['mkdir', '-p', '/mosquitto/config'], check=True)
    subprocess.run(['mkdir', '-p', '/mosquitto/data'], check=True)
    subprocess.run(['mkdir', '-p', '/mosquitto/log'], check=True)
    print("Done!")
    time.sleep(2)
    print("Starting Container...")
    time.sleep(2)
    subprocess.run(["docker", "run", "-d", "-p", "1883:1883", "-p", "9001:9001", "-v", "/mosquitto/data", "-v", "/mosquitto/log", "eclipse-mosquitto"], check=True)
    subprocess.run(["docker", "ps"])


if __name__ == "__main__":
    install_docker()
    configure_mosquitto()

