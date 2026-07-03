import requests
import json
import time
import uuid
import sys
import os

# Ensure directory exists
script_dir = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(script_dir, "pilot_onboarding_results.log")

# Configuration
BASE_URL = "https://staging.ntrust.ai"
REGISTER_ENDPOINT = f"{BASE_URL}/register"
HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "nTrust-Pilot-Onboarding-Script/1.0"
}

# Pilot User Data Generator
def generate_pilot_users(count=10):
    users = []
    for i in range(1, count + 1):
        user_id = str(uuid.uuid4())[:8]
        users.append({
            "username": f"pilot_user_{user_id}",
            "email": f"pilot_{user_id}@ntrust.ai",
            "password": f"P@ssw0rd_{user_id}!",
            "first_name": f"Pilot",
            "last_name": f"User_{i}"
        })
    return users

def register_user(user_data):
    try:
        start_time = time.time()
        response = requests.post(REGISTER_ENDPOINT, json=user_data, headers=HEADERS, timeout=10)
        duration = time.time() - start_time
        
        if response.status_code in [200, 201, 302]:
            try:
                resp_json = response.json()
                if "success" in resp_json and resp_json["success"]:
                    return {"status": "SUCCESS", "latency": f"{duration:.2f}s", "data": resp_json}
                elif "error" in resp_json:
                    return {"status": "API_ERROR", "latency": f"{duration:.2f}s", "message": resp_json["error"]}
                else:
                    return {"status": "SUCCESS", "latency": f"{duration:.2f}s", "raw": str(resp_json)}
            except json.JSONDecodeError:
                return {"status": "SUCCESS", "latency": f"{duration:.2f}s", "raw": response.text[:100]}
        else:
            return {"status": "HTTP_ERROR", "latency": f"{duration:.2f}s", "code": response.status_code, "message": response.text[:100]}
    except requests.exceptions.Timeout:
        return {"status": "TIMEOUT", "message": "Request timed out"}
    except requests.exceptions.RequestException as e:
        return {"status": "NETWORK_ERROR", "message": str(e)}

def main():
    print(f"🚀 Starting Pilot Onboarding for 10 users at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Target: {REGISTER_ENDPOINT}")
    print("-" * 50)
    
    users = generate_pilot_users(10)
    results = []
    success_count = 0
    fail_count = 0

    for i, user in enumerate(users, 1):
        print(f"Registering User {i}/10: {user['username']}...", end=" ")
        result = register_user(user)
        results.append(result)
        
        if result["status"] == "SUCCESS":
            print(f"✅ ({result['latency']})")
            success_count += 1
        else:
            print(f"❌ {result['status']}")
            fail_count += 1
        
        time.sleep(0.5)

    print("-" * 50)
    print(f"📊 SUMMARY: {success_count} Successful, {fail_count} Failed")
    
    # Log results
    with open(log_file, "w") as f:
        f.write(f"Run Time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Target: {REGISTER_ENDPOINT}\n")
        f.write(f"Total: {len(users)}, Success: {success_count}, Failed: {fail_count}\n\n")
        for i, r in enumerate(results):
            f.write(f"User {i+1}: {r['status']} - {r.get('latency', 'N/A')}\n")
            if r['status'] != 'SUCCESS':
                f.write(f"  Error: {r.get('message', 'N/A')}\n")

    if fail_count > 0:
        print("⚠️  FAILED REGISTRATIONS DETECTED. Check logs.")
    
    return success_count == 10

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)