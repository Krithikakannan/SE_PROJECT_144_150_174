import requests
import time

BASE_URL = "http://localhost:5000/api"
TEST_COUNT = 0


def count_test():
    global TEST_COUNT
    TEST_COUNT += 1


def safe_print(res):
    print("Status:", res.status_code)
    try:
        print("Response:", res.json())
    except:
        print("Response (non-JSON):", res.text)


print("\n---- SYSTEM TESTING START ----\n")


# -------------------------------------------------------------
# ST_01 – System Alive
# -------------------------------------------------------------
def test_system_alive():
    print("\n[ST_01] System Alive Check")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/"))


# -------------------------------------------------------------
# ST_02 – Register → Login → Dashboard
# -------------------------------------------------------------
def test_register_login_dashboard():
    print("\n[ST_02] Register → Login → Dashboard")
    count_test()
    email = f"sys{time.time()}@test.com"

    reg = requests.post(f"{BASE_URL}/auth/register", json={
        "name": "SysUser",
        "email": email,
        "password": "test123",
        "role": "Citizen"
    })
    safe_print(reg)

    login = requests.post(f"{BASE_URL}/auth/login",
                          json={"email": email, "password": "test123"})
    safe_print(login)


# -------------------------------------------------------------
# ST_03 – Citizen Complaint Flow
# -------------------------------------------------------------
def test_citizen_flow():
    print("\n[ST_03] Citizen: Login → Complaint → Fetch Complaints")
    count_test()

    login = requests.post(f"{BASE_URL}/auth/login",
                          json={"email": "citizen@example.com", "password": "citizen123"})
    safe_print(login)

    comp = requests.post(f"{BASE_URL}/complaints/create", json={
        "citizenId": "S001",
        "type": "Overflow",
        "location": "BTM Layout"
    })
    safe_print(comp)

    safe_print(requests.get(f"{BASE_URL}/complaints"))


# -------------------------------------------------------------
# ST_04 – Worker Flow
# -------------------------------------------------------------
def test_worker_flow():
    print("\n[ST_04] Worker: Login → Submit Report → Fetch Reports")
    count_test()

    login = requests.post(f"{BASE_URL}/auth/login",
                          json={"email": "worker@example.com", "password": "worker123"})
    safe_print(login)

    rep = requests.post(f"{BASE_URL}/reports/create", json={
        "workerId": "W101",
        "status": "Completed",
        "remarks": "Area cleared"
    })
    safe_print(rep)

    safe_print(requests.get(f"{BASE_URL}/reports"))


# -------------------------------------------------------------
# ST_05 – Admin Flow
# -------------------------------------------------------------
def test_admin_full():
    print("\n[ST_05] Admin: Login → Complaints → Reports → GPS")
    count_test()

    login = requests.post(f"{BASE_URL}/auth/login",
                          json={"email": "admin@example.com", "password": "admin123"})
    safe_print(login)

    token = None
    if login.status_code == 200:
        token = login.json()["token"]

    headers = {"Authorization": f"Bearer {token}"} if token else {}

    safe_print(requests.get(f"{BASE_URL}/complaints", headers=headers))
    safe_print(requests.get(f"{BASE_URL}/reports", headers=headers))
    safe_print(requests.get(f"{BASE_URL}/gps", headers=headers))


# -------------------------------------------------------------
# ST_06 – Notification Flow
# -------------------------------------------------------------
def test_notifications_system():
    print("\n[ST_06] Notification System: Create → Fetch")
    count_test()

    send = requests.post(f"{BASE_URL}/notifications/create", json={
        "title": "System Test",
        "message": "Testing Notifications"
    })
    safe_print(send)

    safe_print(requests.get(f"{BASE_URL}/notifications"))


# -------------------------------------------------------------
# ST_07 – Schedule Fetch Stability
# -------------------------------------------------------------
def test_schedule_stability():
    print("\n[ST_07] Schedule Fetch Stability")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/schedule"))
    safe_print(requests.get(f"{BASE_URL}/schedule"))


# -------------------------------------------------------------
# ST_08 – Parallel Users
# -------------------------------------------------------------
def test_parallel_operation():
    print("\n[ST_08] Parallel Users (Admin + Citizen + Worker)")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/complaints"))
    safe_print(requests.get(f"{BASE_URL}/reports"))
    safe_print(requests.get(f"{BASE_URL}/gps"))


# -------------------------------------------------------------
# ST_09 – Invalid Login Attempts
# -------------------------------------------------------------
def test_invalid_login():
    print("\n[ST_09] Multiple Invalid Logins")
    count_test()
    for pwd in ["1", "wrong", "abcd"]:
        safe_print(requests.post(f"{BASE_URL}/auth/login",
                                 json={"email": "admin@example.com", "password": pwd}))


# -------------------------------------------------------------
# ST_10 – Invalid Forms
# -------------------------------------------------------------
def test_invalid_forms():
    print("\n[ST_10] Invalid Forms")
    count_test()
    safe_print(requests.post(f"{BASE_URL}/complaints/create", json={}))
    safe_print(requests.post(f"{BASE_URL}/notifications/create", json={}))
    safe_print(requests.post(f"{BASE_URL}/auth/register", json={}))


# -------------------------------------------------------------
# ST_11 – Large Input Stress
# -------------------------------------------------------------
def test_large_input():
    print("\n[ST_11] Large Input Stress Test")
    count_test()
    safe_print(requests.post(f"{BASE_URL}/complaints/create", json={
        "citizenId": "900",
        "type": "X" * 500,
        "location": "Test Area"
    }))


# -------------------------------------------------------------
# ST_12 – Token Missing / Invalid
# -------------------------------------------------------------
def test_token_security():
    print("\n[ST_12] Missing Token → Access Blocked")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/admin/data"))

    print("\n[ST_13] Invalid Token → Access Blocked")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/admin/data",
                            headers={"Authorization": "Bearer FAKE123"}))


# -------------------------------------------------------------
# ST_14 – Multi-module Consistency
# -------------------------------------------------------------
def test_multi_module_consistency():
    print("\n[ST_14] Complaint + Report + GPS Consistency")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/complaints"))
    safe_print(requests.get(f"{BASE_URL}/reports"))
    safe_print(requests.get(f"{BASE_URL}/gps"))


# -------------------------------------------------------------
# ST_15 – Light Load (5 Complaints)
# -------------------------------------------------------------
def test_light_load():
    print("\n[ST_15] Light Complaint Load")
    count_test()

    for i in range(5):
        safe_print(requests.post(
            f"{BASE_URL}/complaints/create",
            json={"citizenId": f"L{i}", "type": "Overflow", "location": "City Center"}
        ))


# -------------------------------------------------------------
# ⭐ ADDITIONAL SYSTEM TESTS (ST_16 → ST_30)
# -------------------------------------------------------------

def test_fetch_all_notifications_twice():
    print("\n[ST_16] Fetch Notifications Twice")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/notifications"))
    safe_print(requests.get(f"{BASE_URL}/notifications"))


def test_fetch_reports_twice():
    print("\n[ST_17] Fetch Reports Twice")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/reports"))
    safe_print(requests.get(f"{BASE_URL}/reports"))


def test_multiple_complaint_submissions():
    print("\n[ST_18] Multi Complaint Submission")
    count_test()
    for i in range(3):
        safe_print(requests.post(f"{BASE_URL}/complaints/create",
                                 json={"citizenId": f"M{i}", "type": "TestCase", "location": "Street"}))


def test_invalid_route():
    print("\n[ST_19] Invalid Route Handling")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/invalidRoute/test"))


def test_schedule_double_check():
    print("\n[ST_20] Check Schedule Two Times")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/schedule"))
    safe_print(requests.get(f"{BASE_URL}/schedule"))


def test_worker_report_with_missing_fields():
    print("\n[ST_21] Worker Report Missing Fields")
    count_test()
    safe_print(requests.post(f"{BASE_URL}/reports/create",
                             json={"workerId": ""}))


def test_citizen_fetch_notifications():
    print("\n[ST_22] Citizen Fetch Notifications")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/notifications"))


def test_register_invalid_email_format():
    print("\n[ST_23] Register with Invalid Email Format")
    count_test()
    safe_print(requests.post(f"{BASE_URL}/auth/register",
                             json={"name": "X", "email": "invalidEmail", "password": "123", "role": "Citizen"}))


def test_admin_fetch_all_data():
    print("\n[ST_24] Admin Fetch All Data")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/reports"))
    safe_print(requests.get(f"{BASE_URL}/complaints"))
    safe_print(requests.get(f"{BASE_URL}/gps"))


def test_system_invalid_method():
    print("\n[ST_25] Wrong Method on Route")
    count_test()
    safe_print(requests.post(f"{BASE_URL}/schedule"))


def test_long_location_complaint():
    print("\n[ST_26] Long Location Text")
    count_test()
    safe_print(requests.post(f"{BASE_URL}/complaints/create",
                             json={"citizenId": "500", "type": "Garbage", "location": "X" * 200}))


def test_empty_login_attempt():
    print("\n[ST_27] Empty Login Attempt")
    count_test()
    safe_print(requests.post(f"{BASE_URL}/auth/login", json={"email": "", "password": ""}))


def test_system_two_parallel_actions():
    print("\n[ST_28] Two Parallel System Actions")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/complaints"))
    safe_print(requests.get(f"{BASE_URL}/notifications"))


def test_multiple_worker_reports():
    print("\n[ST_29] Multiple Worker Reports")
    count_test()
    for i in range(2):
        safe_print(requests.post(f"{BASE_URL}/reports/create",
                                 json={"workerId": f"W{i}", "status": "Done"}))


def test_invalid_json_format():
    print("\n[ST_30] Invalid JSON Format")
    count_test()
    try:
        safe_print(requests.post(f"{BASE_URL}/complaints/create", data="INVALID_JSON"))
    except Exception as e:
        print("Exception:", e)


# -------------------------------------------------------------
# RUN ALL SYSTEM TEST CASES
# -------------------------------------------------------------
if __name__ == "__main__":

    test_system_alive()
    test_register_login_dashboard()
    test_citizen_flow()
    test_worker_flow()
    test_admin_full()
    test_notifications_system()
    test_schedule_stability()
    test_parallel_operation()
    test_invalid_login()
    test_invalid_forms()
    test_large_input()
    test_token_security()
    test_multi_module_consistency()
    test_light_load()

    # NEW TESTS
    test_fetch_all_notifications_twice()
    test_fetch_reports_twice()
    test_multiple_complaint_submissions()
    test_invalid_route()
    test_schedule_double_check()
    test_worker_report_with_missing_fields()
    test_citizen_fetch_notifications()
    test_register_invalid_email_format()
    test_admin_fetch_all_data()
    test_system_invalid_method()
    test_long_location_complaint()
    test_empty_login_attempt()
    test_system_two_parallel_actions()
    test_multiple_worker_reports()
    test_invalid_json_format()

    print(f"\n---- TOTAL SYSTEM TEST CASES RUN: {TEST_COUNT} ----")
    print("\n---- SYSTEM TESTING END ----\n")
