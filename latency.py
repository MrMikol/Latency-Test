import subprocess
import re

def ping_host(host):
    command = ["ping", "-n", "4", host]

    try:
        #Runs the ping command
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        output = result.stdout

        #Extract latency values
        latencies = re.findall(r"Minimum = (\d+)ms, Maximum = (\d+)ms, Average = (\d+)ms", output)

        if latencies:
            min_latency, max_latency, avg_latency = map(int, latencies[0])
            print(f"✅ Ping results for {host}:")
            print(f"  Min Latency: {min_latency} ms")
            print(f"  Max Latency: {max_latency} ms")
            print(f"  Avg Latency: {avg_latency} ms")

            if max_latency > 100 :
                print("🐌 Latency")
            else:
                print("🐅 Latency")
        else:
            print(f"❌ Failed to get latency information from {host}")
    except subprocess.CalledProcessError:
        print(F"❌ Failed to ping {host}. Host is unreachable.")

print("🌎 LATENCY TESTER 🌏")
target_host = input("Enter the hostname or IP to ping: ")
ping_host(target_host)