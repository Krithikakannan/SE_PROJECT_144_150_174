import requests

BASE_URL = "http://localhost:5000/api"

# Counter for test cases
TEST_COUNT = 0

# Utility — Safe printing for JSON or text
def safe_print(response):
    print("Status:", response.status_code)
    try:
        print("Response:", response.json())
    except:
        print("Response (non-JSON):", response.text)

# Count helper
def count_test():
    global TEST_COUNT
    TEST_COUNT += 1


print("\n---- UNIT TESTING START ----\n")


# --------------------------------------------------------------
# 1️⃣ LOGIN TEST CASES
# --------------------------------------------------------------

def test_login_valid():
    print("\n[TC_LOGIN_01] Valid Login")
    count_test()
    data = {"email": "admin@example.com", "password": "admin123"}
    res = requests.post(f"{BASE_URL}/auth/login", json=data)
    safe_print(res)

def test_login_invalid_password():
    print("\n[TC_LOGIN_02] Invalid Password")
    count_test()
    data = {"email": "admin@example.com", "password": "wrong"}
    res = requests.post(f"{BASE_URL}/auth/login", json=data)
    safe_print(res)

def test_login_user_not_found():
    print("\n[TC_LOGIN_03] User Not Found")
    count_test()
    data = {"email": "notexist@example.com", "password": "12345"}
    res = requests.post(f"{BASE_URL}/auth/login", json=data)
    safe_print(res)

def test_login_empty_email():
    print("\n[TC_LOGIN_04] Empty Email")
    count_test()
    data = {"email": "", "password": "admin123"}
    res = requests.post(f"{BASE_URL}/auth/login", json=data)
    safe_print(res)

def test_login_empty_password():
    print("\n[TC_LOGIN_05] Empty Password")
    count_test()
    data = {"email": "admin@example.com", "password": ""}
    res = requests.post(f"{BASE_URL}/auth/login", json=data)
    safe_print(res)

def test_login_invalid_email_format():
    print("\n[TC_LOGIN_06] Invalid Email Format")
    count_test()
    data = {"email": "not-an-email", "password": "pass123"}
    res = requests.post(f"{BASE_URL}/auth/login", json=data)
    safe_print(res)

# EXTRA LOGIN TEST CASES
def test_login_sql_injection():
    print("\n[TC_LOGIN_07] SQL Injection Attempt")
    count_test()
    data = {"email": "' OR 1=1 --", "password": "anything"}
    res = requests.post(f"{BASE_URL}/auth/login", json=data)
    safe_print(res)

def test_login_special_characters():
    print("\n[TC_LOGIN_08] Special Characters in Email")
    count_test()
    data = {"email": "#$%^^&&@", "password": "123456"}
    res = requests.post(f"{BASE_URL}/auth/login", json=data)
    safe_print(res)



# --------------------------------------------------------------
# 2️⃣ COMPLAINT CREATION
# --------------------------------------------------------------

def test_complaint_missing_fields():
    print("\n[TC_COMP_01] Complaint Missing Fields")
    count_test()
    data = {"location": ""}
    res = requests.post(f"{BASE_URL}/complaints/create", json=data)
    safe_print(res)

def test_complaint_valid():
    print("\n[TC_COMP_02] Valid Complaint")
    count_test()
    data = {
        "citizenId": "12345",
        "type": "Garbage Overflow",
        "location": "MG Road",
        "photo": ""
    }
    res = requests.post(f"{BASE_URL}/complaints/create", json=data)
    safe_print(res)

def test_complaint_fetch():
    print("\n[TC_COMP_03] Fetch Complaints")
    count_test()
    res = requests.get(f"{BASE_URL}/complaints")
    safe_print(res)

def test_complaint_missing_type():
    print("\n[TC_COMP_04] Missing Complaint Type")
    count_test()
    data = {"citizenId": "100", "location": "BTM Layout"}
    res = requests.post(f"{BASE_URL}/complaints/create", json=data)
    safe_print(res)

def test_complaint_long_text():
    print("\n[TC_COMP_05] Very Long Complaint Text")
    count_test()
    data = {
        "citizenId": "100",
        "type": "A" * 500,
        "location": "MG Road",
        "photo": ""
    }
    res = requests.post(f"{BASE_URL}/complaints/create", json=data)
    safe_print(res)

def test_complaint_invalid_citizenId():
    print("\n[TC_COMP_06] Invalid Citizen ID")
    count_test()
    data = {
        "citizenId": 123,
        "type": "Garbage",
        "location": "MG Road"
    }
    res = requests.post(f"{BASE_URL}/complaints/create", json=data)
    safe_print(res)

# EXTRA COMPLAINT TESTS
def test_complaint_empty_all_fields():
    print("\n[TC_COMP_07] All Fields Empty")
    count_test()
    res = requests.post(f"{BASE_URL}/complaints/create", json={})
    safe_print(res)

def test_complaint_numeric_location():
    print("\n[TC_COMP_08] Numeric Location")
    count_test()
    data = {"citizenId": "100", "type": "Overflow", "location": 12345}
    res = requests.post(f"{BASE_URL}/complaints/create", json=data)
    safe_print(res)



# --------------------------------------------------------------
# 3️⃣ USER REGISTRATION TEST CASES
# --------------------------------------------------------------

def test_register_valid():
    print("\n[TC_REG_01] Valid Registration")
    count_test()
    data = {
        "name": "Test User",
        "email": "testunit@example.com",
        "password": "test123",
        "role": "Citizen"
    }
    res = requests.post(f"{BASE_URL}/auth/register", json=data)
    safe_print(res)

def test_register_existing_email():
    print("\n[TC_REG_02] Existing Email")
    count_test()
    data = {
        "name": "Duplicate",
        "email": "admin@example.com",
        "password": "password",
        "role": "Admin"
    }
    res = requests.post(f"{BASE_URL}/auth/register", json=data)
    safe_print(res)

def test_register_missing_password():
    print("\n[TC_REG_03] Missing Password")
    count_test()
    data = {"name": "User", "email": "unit1@example.com", "role": "Citizen"}
    res = requests.post(f"{BASE_URL}/auth/register", json=data)
    safe_print(res)

def test_register_invalid_role():
    print("\n[TC_REG_04] Invalid Role")
    count_test()
    data = {
        "name": "User",
        "email": "unit2@example.com",
        "password": "pass123",
        "role": "Alien"
    }
    res = requests.post(f"{BASE_URL}/auth/register", json=data)
    safe_print(res)

# EXTRA REGISTER TESTS
def test_register_short_password():
    print("\n[TC_REG_05] Short Password")
    count_test()
    data = {
        "name": "Test",
        "email": "spass@example.com",
        "password": "12",
        "role": "Citizen"
    }
    res = requests.post(f"{BASE_URL}/auth/register", json=data)
    safe_print(res)

def test_register_empty_email():
    print("\n[TC_REG_06] Empty Email")
    count_test()
    data = {"name": "Test", "email": "", "password": "12345", "role": "Citizen"}
    res = requests.post(f"{BASE_URL}/auth/register", json=data)
    safe_print(res)



# --------------------------------------------------------------
# 4️⃣ SCHEDULE TEST CASES
# --------------------------------------------------------------

def test_schedule_fetch():
    print("\n[TC_SCH_01] Fetch Schedules")
    count_test()
    res = requests.get(f"{BASE_URL}/schedule")
    safe_print(res)

# EXTRA SCHEDULE TEST
def test_schedule_invalid_route():
    print("\n[TC_SCH_02] Wrong Schedule Route")
    count_test()
    res = requests.get(f"{BASE_URL}/schedule/wrong")
    safe_print(res)



# --------------------------------------------------------------
# 5️⃣ NOTIFICATION TEST CASES
# --------------------------------------------------------------

def test_notification_fetch():
    print("\n[TC_NOTIF_01] Fetch Notifications")
    count_test()
    res = requests.get(f"{BASE_URL}/notifications")
    safe_print(res)

def test_notification_missing_message():
    print("\n[TC_NOTIF_02] Missing Notification Message")
    count_test()
    data = {"title": "Alert"}
    res = requests.post(f"{BASE_URL}/notifications/create", json=data)
    safe_print(res)

def test_notification_long_title():
    print("\n[TC_NOTIF_03] Long Notification Title")
    count_test()
    data = {"title": "A" * 200, "message": "Test message"}
    res = requests.post(f"{BASE_URL}/notifications/create", json=data)
    safe_print(res)

# EXTRA NOTIFICATION TESTS
def test_notification_empty_title():
    print("\n[TC_NOTIF_04] Empty Title")
    count_test()
    data = {"title": "", "message": "Test"}
    res = requests.post(f"{BASE_URL}/notifications/create", json=data)
    safe_print(res)

def test_notification_empty_message():
    print("\n[TC_NOTIF_05] Empty Message")
    count_test()
    data = {"title": "Notice", "message": ""}
    res = requests.post(f"{BASE_URL}/notifications/create", json=data)
    safe_print(res)



# --------------------------------------------------------------
# 6️⃣ GPS TEST CASES
# --------------------------------------------------------------

def test_gps_fetch():
    print("\n[TC_GPS_01] Fetch GPS Data")
    count_test()
    res = requests.get(f"{BASE_URL}/gps")
    safe_print(res)

def test_gps_invalid_request():
    print("\n[TC_GPS_02] Invalid GPS Request")
    count_test()
    res = requests.get(f"{BASE_URL}/gps/randomTruck")
    safe_print(res)

# EXTRA GPS TEST
def test_gps_missing_truckId():
    print("\n[TC_GPS_03] Missing Truck ID")
    count_test()
    res = requests.get(f"{BASE_URL}/gps/")
    safe_print(res)



# --------------------------------------------------------------
# 7️⃣ COLLECTION REPORT TEST CASES
# --------------------------------------------------------------

def test_report_invalid():
    print("\n[TC_REP_01] Invalid Report Missing Fields")
    count_test()
    data = {"workerId": ""}
    res = requests.post(f"{BASE_URL}/reports/create", json=data)
    safe_print(res)

def test_report_fetch():
    print("\n[TC_REP_02] Fetch Reports")
    count_test()
    res = requests.get(f"{BASE_URL}/reports")
    safe_print(res)

def test_report_missing_workerId():
    print("\n[TC_REP_03] Missing Worker ID")
    count_test()
    data = {"status": "Completed"}
    res = requests.post(f"{BASE_URL}/reports/create", json=data)
    safe_print(res)

def test_report_invalid_status():
    print("\n[TC_REP_04] Invalid Status")
    count_test()
    data = {"workerId": "500", "status": "UnknownStatus"}
    res = requests.post(f"{BASE_URL}/reports/create", json=data)
    safe_print(res)

# EXTRA REPORT TEST
def test_report_empty_payload():
    print("\n[TC_REP_05] Empty JSON Body")
    count_test()
    res = requests.post(f"{BASE_URL}/reports/create", json={})
    safe_print(res)



# --------------------------------------------------------------
# 8️⃣ TOKEN TEST CASES
# --------------------------------------------------------------

def test_access_without_token():
    print("\n[TC_TOKEN_01] Protected Route Without Token")
    count_test()
    res = requests.get(f"{BASE_URL}/admin/data")
    safe_print(res)



# --------------------------------------------------------------
# 9️⃣ INVALID ROUTE TEST CASE
# --------------------------------------------------------------

def test_invalid_route():
    print("\n[TC_INV_01] Invalid Route")
    count_test()
    res = requests.get(f"{BASE_URL}/wrong/route")
    safe_print(res)



# --------------------------------------------------------------
# RUN ALL TEST CASES
# --------------------------------------------------------------

if __name__ == "__main__":

    # LOGIN
    test_login_valid()
    test_login_invalid_password()
    test_login_user_not_found()
    test_login_empty_email()
    test_login_empty_password()
    test_login_invalid_email_format()
    test_login_sql_injection()
    test_login_special_characters()

    # COMPLAINTS
    test_complaint_missing_fields()
    test_complaint_valid()
    test_complaint_fetch()
    test_complaint_missing_type()
    test_complaint_long_text()
    test_complaint_invalid_citizenId()
    test_complaint_empty_all_fields()
    test_complaint_numeric_location()

    # REGISTRATION
    test_register_valid()
    test_register_existing_email()
    test_register_missing_password()
    test_register_invalid_role()
    test_register_short_password()
    test_register_empty_email()

    # SCHEDULE
    test_schedule_fetch()
    test_schedule_invalid_route()

    # NOTIFICATIONS
    test_notification_fetch()
    test_notification_missing_message()
    test_notification_long_title()
    test_notification_empty_title()
    test_notification_empty_message()

    # GPS
    test_gps_fetch()
    test_gps_invalid_request()
    test_gps_missing_truckId()

    # REPORTS
    test_report_invalid()
    test_report_fetch()
    test_report_missing_workerId()
    test_report_invalid_status()
    test_report_empty_payload()

    # TOKEN
    test_access_without_token()

    # INVALID ROUTE
    test_invalid_route()

    print(f"\n---- TOTAL UNIT TEST CASES RUN: {TEST_COUNT} ----")
    print("\n---- UNIT TESTING END ----\n")
