import requests
import time

BASE_URL = "http://localhost:5000/api"

TEST_COUNT = 0


def count_test():
    global TEST_COUNT
    TEST_COUNT += 1


def safe_print(response):
    print("Status:", response.status_code)
    try:
        print("Response:", response.json())
    except:
        print("Response (non-JSON):", response.text)


print("\n---- REGRESSION TESTING START ----\n")


# -------------------------------------------------------------
# 1️⃣ LOGIN REGRESSION (8 TEST CASES)
# -------------------------------------------------------------

def test_login_still_works():
    print("\n[R_LOGIN_01] Valid login still works")
    count_test()
    data = {"email": "admin@example.com", "password": "admin123"}
    res = requests.post(f"{BASE_URL}/auth/login", json=data)
    safe_print(res)
    return res.json().get("token") if res.status_code == 200 else None


def test_invalid_login():
    print("\n[R_LOGIN_02] Invalid login still fails")
    count_test()
    data = {"email": "wrong@example.com", "password": "wrong"}
    res = requests.post(f"{BASE_URL}/auth/login", json=data)
    safe_print(res)


def test_login_wrong_case():
    print("\n[R_LOGIN_03] Login email case insensitive")
    count_test()
    data = {"email": "ADMIN@example.com", "password": "admin123"}
    res = requests.post(f"{BASE_URL}/auth/login", json=data)
    safe_print(res)


def test_login_empty_body():
    print("\n[R_LOGIN_04] Empty login body")
    count_test()
    res = requests.post(f"{BASE_URL}/auth/login", json={})
    safe_print(res)


def test_login_missing_email():
    print("\n[R_LOGIN_05] Missing email")
    count_test()
    data = {"password": "12345"}
    res = requests.post(f"{BASE_URL}/auth/login", json=data)
    safe_print(res)


def test_login_missing_password():
    print("\n[R_LOGIN_06] Missing password")
    count_test()
    data = {"email": "test@example.com"}
    res = requests.post(f"{BASE_URL}/auth/login", json=data)
    safe_print(res)


def test_login_numeric_password():
    print("\n[R_LOGIN_07] Numeric password")
    count_test()
    data = {"email": "admin@example.com", "password": 123456}
    res = requests.post(f"{BASE_URL}/auth/login", json=data)
    safe_print(res)


def test_login_special_chars():
    print("\n[R_LOGIN_08] Login with special characters")
    count_test()
    data = {"email": "admin@example.com", "password": "@@@###$$$"}
    res = requests.post(f"{BASE_URL}/auth/login", json=data)
    safe_print(res)


# -------------------------------------------------------------
# 2️⃣ COMPLAINT REGRESSION (7 TEST CASES)
# -------------------------------------------------------------

def test_complaint_create():
    print("\n[R_COMP_01] Complaint creation works")
    count_test()
    data = {"citizenId": "100", "type": "Garbage", "location": "JP Nagar"}
    res = requests.post(f"{BASE_URL}/complaints/create", json=data)
    safe_print(res)


def test_complaint_empty_request():
    print("\n[R_COMP_02] Empty complaint request")
    count_test()
    res = requests.post(f"{BASE_URL}/complaints/create", json={})
    safe_print(res)


def test_complaint_missing_type():
    print("\n[R_COMP_03] Missing complaint type")
    count_test()
    data = {"citizenId": "100", "location": "MG Road"}
    res = requests.post(f"{BASE_URL}/complaints/create", json=data)
    safe_print(res)


def test_complaint_long_text():
    print("\n[R_COMP_04] Long complaint text")
    count_test()
    data = {"citizenId": "100", "type": "A"*200, "location": "BTM"}
    res = requests.post(f"{BASE_URL}/complaints/create", json=data)
    safe_print(res)


def test_complaint_fetch():
    print("\n[R_COMP_05] Fetch complaints")
    count_test()
    res = requests.get(f"{BASE_URL}/complaints")
    safe_print(res)


def test_complaint_filter_type():
    print("\n[R_COMP_06] Complaint filter by type")
    count_test()
    res = requests.get(f"{BASE_URL}/complaints?type=Garbage")
    safe_print(res)


def test_complaint_invalid_route():
    print("\n[R_COMP_07] Wrong complaint route")
    count_test()
    res = requests.get(f"{BASE_URL}/complaintssss")
    safe_print(res)


# -------------------------------------------------------------
# 3️⃣ SCHEDULE REGRESSION (3 TEST CASES)
# -------------------------------------------------------------

def test_schedule_fetch():
    print("\n[R_SCH_01] Fetch schedule")
    count_test()
    res = requests.get(f"{BASE_URL}/schedule")
    safe_print(res)


def test_schedule_invalid_day():
    print("\n[R_SCH_02] Invalid schedule day")
    count_test()
    res = requests.get(f"{BASE_URL}/schedule?day=WrongDay")
    safe_print(res)


def test_schedule_wrong_route():
    print("\n[R_SCH_03] Wrong schedule route")
    count_test()
    res = requests.get(f"{BASE_URL}/schedulessss")
    safe_print(res)


# -------------------------------------------------------------
# 4️⃣ NOTIFICATION REGRESSION (5 TEST CASES)
# -------------------------------------------------------------

def test_notification_create():
    print("\n[R_NOTIF_01] Notification create")
    count_test()
    data = {"title": "Test", "message": "Testing"}
    res = requests.post(f"{BASE_URL}/notifications/create", json=data)
    safe_print(res)


def test_notification_empty_payload():
    print("\n[R_NOTIF_02] Empty notification payload")
    count_test()
    res = requests.post(f"{BASE_URL}/notifications/create", json={})
    safe_print(res)


def test_notification_fetch():
    print("\n[R_NOTIF_03] Fetch notifications")
    count_test()
    res = requests.get(f"{BASE_URL}/notifications")
    safe_print(res)


def test_notification_long_title():
    print("\n[R_NOTIF_04] Long title notification")
    count_test()
    data = {"title": "A"*200, "message": "Test"}
    res = requests.post(f"{BASE_URL}/notifications/create", json=data)
    safe_print(res)


def test_notification_wrong_route():
    print("\n[R_NOTIF_05] Wrong notification route")
    count_test()
    res = requests.get(f"{BASE_URL}/notificationZZZ")
    safe_print(res)


# -------------------------------------------------------------
# 5️⃣ REPORT REGRESSION (5 TEST CASES)
# -------------------------------------------------------------

def test_report_submit():
    print("\n[R_REP_01] Submit report")
    count_test()
    data = {"workerId": "9001", "status": "Collected"}
    res = requests.post(f"{BASE_URL}/reports/create", json=data)
    safe_print(res)


def test_report_missing_worker():
    print("\n[R_REP_02] Missing worker ID")
    count_test()
    data = {"status": "Collected"}
    res = requests.post(f"{BASE_URL}/reports/create", json=data)
    safe_print(res)


def test_report_fetch():
    print("\n[R_REP_03] Fetch reports")
    count_test()
    res = requests.get(f"{BASE_URL}/reports")
    safe_print(res)


def test_report_filtering():
    print("\n[R_REP_04] Fetch reports with filter")
    count_test()
    res = requests.get(f"{BASE_URL}/reports?status=Collected")
    safe_print(res)


def test_report_wrong_route():
    print("\n[R_REP_05] Wrong report route")
    count_test()
    res = requests.get(f"{BASE_URL}/reportZZZ")
    safe_print(res)


# -------------------------------------------------------------
# 6️⃣ GPS REGRESSION (3 TEST CASES)
# -------------------------------------------------------------

def test_gps_fetch():
    print("\n[R_GPS_01] Fetch GPS")
    count_test()
    res = requests.get(f"{BASE_URL}/gps")
    safe_print(res)


def test_gps_specific():
    print("\n[R_GPS_02] GPS for specific truck")
    count_test()
    res = requests.get(f"{BASE_URL}/gps/truck001")
    safe_print(res)


def test_gps_wrong_route():
    print("\n[R_GPS_03] Wrong GPS route")
    count_test()
    res = requests.get(f"{BASE_URL}/gpsXXX")
    safe_print(res)


# -------------------------------------------------------------
# 7️⃣ INVALID ROUTE REGRESSION (3 TEST CASES)
# -------------------------------------------------------------

def test_invalid_route_1():
    print("\n[R_INV_01] Invalid route test 1")
    count_test()
    res = requests.get(f"{BASE_URL}/abc")
    safe_print(res)


def test_invalid_route_2():
    print("\n[R_INV_02] Invalid route test 2")
    count_test()
    res = requests.get(f"{BASE_URL}/xyz123")
    safe_print(res)


def test_invalid_route_3():
    print("\n[R_INV_03] Invalid route test 3")
    count_test()
    res = requests.get(f"{BASE_URL}/wrong/url/path")
    safe_print(res)


# -------------------------------------------------------------
# RUN ALL TEST CASES
# -------------------------------------------------------------

if __name__ == "__main__":

    # LOGIN (8 Tests)
    token = test_login_still_works()
    test_invalid_login()
    test_login_wrong_case()
    test_login_empty_body()
    test_login_missing_email()
    test_login_missing_password()
    test_login_numeric_password()
    test_login_special_chars()

    # COMPLAINT (7 Tests)
    test_complaint_create()
    test_complaint_empty_request()
    test_complaint_missing_type()
    test_complaint_long_text()
    test_complaint_fetch()
    test_complaint_filter_type()
    test_complaint_invalid_route()

    # SCHEDULE (3 Tests)
    test_schedule_fetch()
    test_schedule_invalid_day()
    test_schedule_wrong_route()

    # NOTIFICATION (5 Tests)
    test_notification_create()
    test_notification_empty_payload()
    test_notification_fetch()
    test_notification_long_title()
    test_notification_wrong_route()

    # REPORT (5 Tests)
    test_report_submit()
    test_report_missing_worker()
    test_report_fetch()
    test_report_filtering()
    test_report_wrong_route()

    # GPS (3 Tests)
    test_gps_fetch()
    test_gps_specific()
    test_gps_wrong_route()

    # INVALID ROUTES (3 Tests)
    test_invalid_route_1()
    test_invalid_route_2()
    test_invalid_route_3()

    print(f"\n---- TOTAL REGRESSION TEST CASES RUN: {TEST_COUNT} ----")
    print("\n---- REGRESSION TESTING END ----\n")
