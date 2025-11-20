import requests
import time

BASE_URL = "http://localhost:5000/api"
TEST_COUNT = 0


def count_test():
    global TEST_COUNT
    TEST_COUNT += 1


def safe_print(r):
    print("Status:", r.status_code)
    try:
        print("Response:", r.json())
    except:
        print("Response:", r.text)


print("\n---- VALIDATION TESTING START ----\n")


# -------------------------------------------------------
# VT_01 – Valid Login
# -------------------------------------------------------
def test_login_valid():
    print("\n[VT_01] Valid Login")
    count_test()
    safe_print(requests.post(f"{BASE_URL}/auth/login",
                             json={"email": "admin@example.com", "password": "admin123"}))


# -------------------------------------------------------
# VT_02 – Invalid Password
# -------------------------------------------------------
def test_login_invalid_password():
    print("\n[VT_02] Invalid Password")
    count_test()
    safe_print(requests.post(f"{BASE_URL}/auth/login",
                             json={"email": "admin@example.com", "password": "wrong"}))


# -------------------------------------------------------
# VT_03 – Invalid Email Format
# -------------------------------------------------------
def test_login_invalid_email_format():
    print("\n[VT_03] Invalid Email Format")
    count_test()
    safe_print(requests.post(f"{BASE_URL}/auth/login",
                             json={"email": "invalidEmail", "password": "123"}))


# -------------------------------------------------------
# VT_04 – Valid Registration
# -------------------------------------------------------
def test_register_valid():
    print("\n[VT_04] Valid Registration")
    count_test()
    safe_print(requests.post(f"{BASE_URL}/auth/register",
                             json={"name": "ValTest", "email": f"val{time.time()}@example.com",
                                   "password": "12345", "role": "Citizen"}))


# -------------------------------------------------------
# VT_05 – Registration Existing Email
# -------------------------------------------------------
def test_register_existing():
    print("\n[VT_05] Existing Email Registration")
    count_test()
    safe_print(requests.post(f"{BASE_URL}/auth/register",
                             json={"name": "A", "email": "admin@example.com",
                                   "password": "123", "role": "Admin"}))


# -------------------------------------------------------
# VT_06 – Complaint Valid
# -------------------------------------------------------
def test_complaint_valid():
    print("\n[VT_06] Complaint Valid")
    count_test()
    safe_print(requests.post(f"{BASE_URL}/complaints/create",
                             json={"citizenId": "100", "type": "Overflow", "location": "HSR"}))


# -------------------------------------------------------
# VT_07 – Complaint Missing Fields
# -------------------------------------------------------
def test_complaint_missing_fields():
    print("\n[VT_07] Complaint Missing Fields")
    count_test()
    safe_print(requests.post(f"{BASE_URL}/complaints/create", json={}))


# -------------------------------------------------------
# VT_08 – Fetch Complaints
# -------------------------------------------------------
def test_complaint_fetch():
    print("\n[VT_08] Fetch Complaints")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/complaints"))


# -------------------------------------------------------
# VT_09 – Notification Create
# -------------------------------------------------------
def test_notification_create():
    print("\n[VT_09] Notification Create")
    count_test()
    safe_print(requests.post(f"{BASE_URL}/notifications/create",
                             json={"title": "Test", "message": "Testing"}))


# -------------------------------------------------------
# VT_10 – Notification List
# -------------------------------------------------------
def test_notification_fetch():
    print("\n[VT_10] Fetch Notifications")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/notifications"))


# -------------------------------------------------------
# VT_11 – Report Valid
# -------------------------------------------------------
def test_report_valid():
    print("\n[VT_11] Report Valid")
    count_test()
    safe_print(requests.post(f"{BASE_URL}/reports/create",
                             json={"workerId": "W1", "status": "Done", "remarks": "All OK"}))


# -------------------------------------------------------
# VT_12 – Report Missing Fields
# -------------------------------------------------------
def test_report_missing():
    print("\n[VT_12] Report Missing Fields")
    count_test()
    safe_print(requests.post(f"{BASE_URL}/reports/create", json={"workerId": ""}))


# -------------------------------------------------------
# VT_13 – Fetch Reports
# -------------------------------------------------------
def test_report_fetch():
    print("\n[VT_13] Fetch Reports")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/reports"))


# -------------------------------------------------------
# VT_14 – GPS Fetch
# -------------------------------------------------------
def test_gps_fetch():
    print("\n[VT_14] GPS Fetch")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/gps"))


# -------------------------------------------------------
# VT_15 – Admin Access With Token
# -------------------------------------------------------
def test_admin_with_token():
    print("\n[VT_15] Admin Access With Token")
    count_test()

    login = requests.post(f"{BASE_URL}/auth/login",
                          json={"email": "admin@example.com", "password": "admin123"})
    if login.status_code == 200:
        token = login.json()["token"]
        safe_print(requests.get(f"{BASE_URL}/admin/data",
                                headers={"Authorization": f"Bearer {token}"}))
    else:
        print("Login failed")


# -------------------------------------------------------
# VT_16 – Admin Access Without Token
# -------------------------------------------------------
def test_admin_without_token():
    print("\n[VT_16] Admin Access Without Token")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/admin/data"))


# -------------------------------------------------------
# VT_17 – Schedule Fetch
# -------------------------------------------------------
def test_schedule_fetch():
    print("\n[VT_17] Schedule Fetch")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/schedule"))


# -------------------------------------------------------
# VT_18 – Invalid Schedule Update
# -------------------------------------------------------
def test_schedule_invalid():
    print("\n[VT_18] Invalid Schedule Update")
    count_test()
    safe_print(requests.post(f"{BASE_URL}/schedule", json={}))


# -------------------------------------------------------
# VT_19 – System Root Check
# -------------------------------------------------------
def test_root_check():
    print("\n[VT_19] Root Check")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/"))


# -------------------------------------------------------
# VT_20 – Wrong Route
# -------------------------------------------------------
def test_invalid_route():
    print("\n[VT_20] Invalid Route")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/wrongRoute"))


# -------------------------------------------------------
# VT_21 – Empty Login
# -------------------------------------------------------
def test_empty_login():
    print("\n[VT_21] Empty Login")
    count_test()
    safe_print(requests.post(f"{BASE_URL}/auth/login",
                             json={"email": "", "password": ""}))


# -------------------------------------------------------
# VT_22 – Long Complaint Text
# -------------------------------------------------------
def test_long_complaint():
    print("\n[VT_22] Long Complaint Text")
    count_test()
    safe_print(requests.post(f"{BASE_URL}/complaints/create",
                             json={"citizenId": "300", "type": "Garbage",
                                   "location": "X" * 200}))


# -------------------------------------------------------
# VT_23 – Empty Notification
# -------------------------------------------------------
def test_empty_notification():
    print("\n[VT_23] Empty Notification")
    count_test()
    safe_print(requests.post(f"{BASE_URL}/notifications/create", json={}))


# -------------------------------------------------------
# VT_24 – Report Missing Status
# -------------------------------------------------------
def test_report_missing_status():
    print("\n[VT_24] Missing Report Status")
    count_test()
    safe_print(requests.post(f"{BASE_URL}/reports/create",
                             json={"workerId": "W200"}))


# -------------------------------------------------------
# VT_25 – Load Test (5 Complaints)
# -------------------------------------------------------
def test_load_complaints():
    print("\n[VT_25] Load Test – Multiple Complaints")
    count_test()
    for i in range(5):
        safe_print(requests.post(f"{BASE_URL}/complaints/create",
                                 json={"citizenId": f"L{i}", "type": "Overflow", "location": "Area"}))


# -------------------------------------------------------
# RUN ALL TESTS
# -------------------------------------------------------
if __name__ == "__main__":

    test_login_valid()
    test_login_invalid_password()
    test_login_invalid_email_format()
    test_register_valid()
    test_register_existing()
    test_complaint_valid()
    test_complaint_missing_fields()
    test_complaint_fetch()
    test_notification_create()
    test_notification_fetch()
    test_report_valid()
    test_report_missing()
    test_report_fetch()
    test_gps_fetch()
    test_admin_with_token()
    test_admin_without_token()
    test_schedule_fetch()
    test_schedule_invalid()
    test_root_check()
    test_invalid_route()
    test_empty_login()
    test_long_complaint()
    test_empty_notification()
    test_report_missing_status()
    test_load_complaints()

    print(f"\n---- TOTAL VALIDATION TEST CASES RUN: {TEST_COUNT} ----")
    print("\n---- VALIDATION TESTING END ----\n")
