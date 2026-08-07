file_path = "Logs.txt"
state = False

def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.readlines()

            return content
    except FileNotFoundError:
        print(f"ERROR: File not found in path {file_path}")

log_content = read_file(file_path)

def process_logs(log_content):
    user_data = {}

    for line in log_content:

        log_piece = line.split()
        user = log_piece[3]
        

        if "FAILED" in log_piece:
            if user not in user_data:
                user_data[user] = {"current_streak": 1, "longest_streak": 0}

            else:
                user_data[user]["current_streak"] += 1
                user_data[user]["longest_streak"] = user_data[user]["current_streak"]
    

        if "SUCCESS" in log_piece:
            user_data[user]["current_streak"] = 0
        
    return user_data

data = process_logs(log_content)

def decision_maker(data):
    high_threshold = 5
    med_threshold = 3
    
    status = None

    print("======== Brute Force Detector ========")

    for item in data:
        user = item

        if data[user]["longest_streak"] >= high_threshold:
            status = "Suspicious"
            reason = "High failure count"

        elif data[user]["longest_streak"] >= med_threshold:
            status = "Low Suspicion"
            reason = "Low failure count"

        else:
            status = "Normal"
            reason = "No flags raised"

        print(f"Username: {user}\nStatus: {status}\nReason: {reason}")
        print("======================================")


decision_maker(data)

