from datetime import datetime
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

def website_blocker():
    badsites_list = ['www.facebook.com', 'facebook.com', 'twitter.com', 'www.twitter.com', 'instagram.com', 'www.instagram.com']
    start_hour = '8'
    end_hour = '16'
    start = int(start_hour) * 60
    end = int(end_hour) * 60
    current_time = datetime.now().hour*60
    if current_time >= start and current_time <= end:
        print("Sites are blocked")
        with open(hosts_path, 'r+') as hostsfile:
            hosts_content = hostsfile.read()
            for site in badsites_list:
                if site not in hosts_content:
                    hostsfile.write(redirect + " " + site + "\n")
    else:
        print("Unblocking sites")
        with open(hosts_path, 'r+') as hostsfile:
            lines = hostsfile.readlines()
            hostsfile.seek(0)
            for line in lines:
                if not any(site in line for site in badsites_list):
                    hostsfile.write(line)
            hostsfile.truncate()

if __name__ == "__main__":
    website_blocker()