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
        print("Response:", res.text)


print("\n---- INTEGRATION TESTING START ----\n")


# -------------------------------------------------------------
# IT_01 → Login → Token → Admin Route
# -------------------------------------------------------------
def test_login_to_admin_route():
    print("\n[IT_01] Login → Token → Admin Route")
    count_test()

    login = requests.post(f"{BASE_URL}/auth/login",
                          json={"email": "admin@example.com", "password": "admin123"})
    safe_print(login)

    if login.status_code != 200:
        return
    token = login.json()["token"]

    res = requests.get(f"{BASE_URL}/admin/data",
                       headers={"Authorization": f"Bearer {token}"})
    safe_print(res)


# -------------------------------------------------------------
# IT_02 Register → Login
# -------------------------------------------------------------
def test_register_then_login():
    print("\n[IT_02] Register → Login")
    count_test()

    email = f"user{time.time()}@example.com"
    reg = requests.post(f"{BASE_URL}/auth/register", json={
        "name": "User",
        "email": email,
        "password": "test123",
        "role": "Citizen"
    })
    safe_print(reg)

    login = requests.post(f"{BASE_URL}/auth/login",
                          json={"email": email, "password": "test123"})
    safe_print(login)


# -------------------------------------------------------------
# IT_03 Login → Create Complaint → Fetch Complaints
# -------------------------------------------------------------
def test_complaint_flow():
    print("\n[IT_03] Login → Create Complaint → Fetch Complaint")
    count_test()

    comp = requests.post(f"{BASE_URL}/complaints/create", json={
        "citizenId": "300",
        "type": "Overflow",
        "location": "HSR"
    })
    safe_print(comp)

    fetch = requests.get(f"{BASE_URL}/complaints")
    safe_print(fetch)


# -------------------------------------------------------------
# IT_04 Complaint → Notification
# -------------------------------------------------------------
def test_complaint_notification():
    print("\n[IT_04] Complaint → Notification")
    count_test()

    create = requests.post(f"{BASE_URL}/complaints/create", json={
        "citizenId": "301",
        "type": "Garbage",
        "location": "Koramangala"
    })
    safe_print(create)

    notif = requests.get(f"{BASE_URL}/notifications")
    safe_print(notif)


# -------------------------------------------------------------
# IT_05 Worker Report → Admin Fetch
# -------------------------------------------------------------
def test_report_to_admin():
    print("\n[IT_05] Worker Report → Admin Fetch")
    count_test()

    rep = requests.post(f"{BASE_URL}/reports/create", json={
        "workerId": "W100",
        "status": "Collected"
    })
    safe_print(rep)

    fetch = requests.get(f"{BASE_URL}/reports")
    safe_print(fetch)


# -------------------------------------------------------------
# IT_06 GPS Fetch
# -------------------------------------------------------------
def test_gps_flow():
    print("\n[IT_06] GPS Fetch")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/gps"))


# -------------------------------------------------------------
# IT_07 Admin Sends Notification → Fetch
# -------------------------------------------------------------
def test_notification_flow():
    print("\n[IT_07] Admin Sends Notification → Citizen Fetches")
    count_test()

    send = requests.post(f"{BASE_URL}/notifications/create",
                         json={"title": "Test", "message": "Integration"})
    safe_print(send)

    fetch = requests.get(f"{BASE_URL}/notifications")
    safe_print(fetch)


# -------------------------------------------------------------
# IT_08 Login → Role Dashboard
# -------------------------------------------------------------
def test_role_dashboard():
    print("\n[IT_08] Login → Role Dashboard")
    count_test()

    safe_print(requests.post(f"{BASE_URL}/auth/login",
                             json={"email": "citizen@example.com", "password": "citizen123"}))

    safe_print(requests.post(f"{BASE_URL}/auth/login",
                             json={"email": "admin@example.com", "password": "admin123"}))


# -------------------------------------------------------------
# IT_09 Schedule Fetch
# -------------------------------------------------------------
def test_schedule_flow():
    print("\n[IT_09] Schedule Fetch")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/schedule"))


# -------------------------------------------------------------
# IT_10 Dashboard Complaint Count
# -------------------------------------------------------------
def test_dashboard_complaint_count():
    print("\n[IT_10] Dashboard Complaint Count")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/complaints"))


# -------------------------------------------------------------
# IT_11 Report Create → Fetch
# -------------------------------------------------------------
def test_report_status_update():
    print("\n[IT_11] Report Create → Fetch")
    count_test()

    safe_print(requests.post(f"{BASE_URL}/reports/create",
                             json={"workerId": "W200", "status": "Pending"}))

    safe_print(requests.get(f"{BASE_URL}/reports"))


# -------------------------------------------------------------
# IT_12 Invalid Token → Protected Route
# -------------------------------------------------------------
def test_invalid_token_access():
    print("\n[IT_12] Invalid Token → Protected Route")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/admin/data",
                            headers={"Authorization": "Bearer WRONGTOKEN"}))



# -------------------------------------------------------------
# ⭐ NEW TEST CASES (IT_13–IT_36)
# -------------------------------------------------------------

def test_admin_fetch_after_complaint():
    print("\n[IT_13] Complaint → Admin Fetch")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/admin/complaints"))


def test_dashboard_updates():
    print("\n[IT_14] Dashboard Updated After New Complaint")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/complaints"))


def test_admin_notification_list():
    print("\n[IT_15] Notification → Admin List")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/notifications"))


def test_new_user_complaint_flow():
    print("\n[IT_16] Register → Login → Complaint")
    count_test()

    email = f"flow{time.time()}@example.com"
    safe_print(requests.post(f"{BASE_URL}/auth/register",
                             json={"name": "Flow", "email": email, "password": "abc123", "role": "Citizen"}))
    safe_print(requests.post(f"{BASE_URL}/auth/login",
                             json={"email": email, "password": "abc123"}))
    safe_print(requests.post(f"{BASE_URL}/complaints/create",
                             json={"citizenId": "998", "type": "Roadside", "location": "Silk Board"}))


def test_report_dashboard_sync():
    print("\n[IT_17] Report → Dashboard Sync")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/reports"))


def test_user_notification_view():
    print("\n[IT_18] Citizen View Notifications")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/notifications"))


def test_multiple_complaints():
    print("\n[IT_19] Creating Multiple Complaints")
    count_test()
    for i in range(3):
        safe_print(requests.post(f"{BASE_URL}/complaints/create",
                                 json={"citizenId": f"C{i}", "type": "Test", "location": f"Loc {i}"}))


def test_invalid_routes():
    print("\n[IT_20] Invalid Routes Stability")
    count_test()
    for r in ["wrong/1", "abc/xyz", "404"]:
        safe_print(requests.get(f"{BASE_URL}/{r}"))


def test_gps_invalid_query():
    print("\n[IT_21] GPS Wrong URL")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/gps/wrong"))


def test_notification_missing_fields():
    print("\n[IT_22] Missing Notification Fields")
    count_test()
    safe_print(requests.post(f"{BASE_URL}/notifications/create",
                             json={"title": ""}))


def test_login_wrong_password():
    print("\n[IT_23] Wrong Password Login")
    count_test()
    safe_print(requests.post(f"{BASE_URL}/auth/login",
                             json={"email": "admin@example.com", "password": "wrong"}))


def test_create_empty_complaint():
    print("\n[IT_24] Empty Complaint Fields")
    count_test()
    safe_print(requests.post(f"{BASE_URL}/complaints/create",
                             json={"location": ""}))


def test_worker_empty_report():
    print("\n[IT_25] Empty Worker Report")
    count_test()
    safe_print(requests.post(f"{BASE_URL}/reports/create",
                             json={"workerId": ""}))


def test_register_invalid_role():
    print("\n[IT_26] Invalid Role Registration")
    count_test()
    safe_print(requests.post(f"{BASE_URL}/auth/register",
                             json={"name": "X", "email": f"inv{time.time()}@ex.com", "password": "123", "role": "Alien"}))


def test_dashboard_after_report():
    print("\n[IT_27] Dashboard After New Report")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/reports"))


def test_token_expiry_simulation():
    print("\n[IT_28] Token Expired Simulation")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/admin/data",
                            headers={"Authorization": "Bearer expiredToken"}))


def test_repeated_notifications():
    print("\n[IT_29] Repeated Notifications Test")
    count_test()
    for i in range(2):
        safe_print(requests.post(f"{BASE_URL}/notifications/create",
                                 json={"title": f"Notif {i}", "message": "Test"}))


def test_schedule_stability():
    print("\n[IT_30] Check Schedule Stability")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/schedule"))


def test_wrong_method_on_route():
    print("\n[IT_31] Wrong Method (POST on GET Route)")
    count_test()
    safe_print(requests.post(f"{BASE_URL}/complaints"))


def test_long_complaint_type():
    print("\n[IT_32] Very Long Complaint Type")
    count_test()
    safe_print(requests.post(f"{BASE_URL}/complaints/create",
                             json={"citizenId": "A", "type": "X"*200, "location": "B"}))


def test_empty_login():
    print("\n[IT_33] Login With Empty Fields")
    count_test()
    safe_print(requests.post(f"{BASE_URL}/auth/login",
                             json={"email": "", "password": ""}))


def test_multiple_login_attempts():
    print("\n[IT_34] Multiple Login Attempts")
    count_test()
    for pwd in ["x", "y", "admin123"]:
        safe_print(requests.post(f"{BASE_URL}/auth/login",
                                 json={"email": "admin@example.com", "password": pwd}))


def test_fetch_reports_twice():
    print("\n[IT_35] Double Fetch Reports")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/reports"))
    safe_print(requests.get(f"{BASE_URL}/reports"))


def test_fetch_notifications_twice():
    print("\n[IT_36] Double Fetch Notifications")
    count_test()
    safe_print(requests.get(f"{BASE_URL}/notifications"))
    safe_print(requests.get(f"{BASE_URL}/notifications"))


# -------------------------------------------------------------
# RUN ALL TESTS
# -------------------------------------------------------------
if __name__ == "__main__":

    test_login_to_admin_route()
    test_register_then_login()
    test_complaint_flow()
    test_complaint_notification()
    test_report_to_admin()
    test_gps_flow()
    test_notification_flow()
    test_role_dashboard()
    test_schedule_flow()
    test_dashboard_complaint_count()
    test_report_status_update()
    test_invalid_token_access()

    # NEW 24 TEST CASES ↓
    test_admin_fetch_after_complaint()
    test_dashboard_updates()
    test_admin_notification_list()
    test_new_user_complaint_flow()
    test_report_dashboard_sync()
    test_user_notification_view()
    test_multiple_complaints()
    test_invalid_routes()
    test_gps_invalid_query()
    test_notification_missing_fields()
    test_login_wrong_password()
    test_create_empty_complaint()
    test_worker_empty_report()
    test_register_invalid_role()
    test_dashboard_after_report()
    test_token_expiry_simulation()
    test_repeated_notifications()
    test_schedule_stability()
    test_wrong_method_on_route()
    test_long_complaint_type()
    test_empty_login()
    test_multiple_login_attempts()
    test_fetch_reports_twice()
    test_fetch_notifications_twice()

    print(f"\n---- TOTAL INTEGRATION TEST CASES RUN: {TEST_COUNT} ----")
    print("\n---- INTEGRATION TESTING END ----\n")
