import requests
import json
import datetime

TEAM_REQ_INFO = {
    11: {
        "login": "logInForm.html",
        "login_params": (
            ("", ""),
            ("", "")
            )
        ,
        "register": "registrationForm.html",
        "register_params": (
            ("", ""),
            ),
        "order": "",
        "order_params": (
            (),
            )
        },
    12: {
        "login": "login",
        "login_params": (
            ("", ""),
            ("", "")
            )
        ,
        "register": "registration",
        "register_params": (
            ("", ""),
            ),
        "order": "",
        "order_params": (
            (),
            )
        },
    21: {
        "login": "/common-services/login",
        "login_params": (
            ("email", "b"),
            ("password", "d")
            )
        ,
        "register": "/common-services/register",
        "register_params": (
            ("", ""),
            ),
        "order": "",
        "order_params": (
            (),
            )
        },
    22: {
        "login": "login.html?",
        "login_params": (
            ("", ""),
            ("", "")
            )
        ,
        "register": "register.html?",
        "register_params": (
            ("", ""),
            ),
        "order": "",
        "order_params": (
            (),
            )
        },
    23: {
        "login": "login.html",
        "login_params": (
            ("", ""),
            ("", "")
            )
        ,
        "register": "",
        "register_params": (
            ("", ""),
            ),
        "order": "",
        "order_params": (
            (),
            )
        },
    }

ELEVEN, TWELVE, TWENTY_ONE, TWENTY_TWO, TWENTY_THREE = range(5)
TEAMS = (
    11,
    12,
    21,
    22,
    23
    )
TEAM_NO = TEAMS[TWENTY_ONE]

LOGIN, REGISTER, ORDER = range(3)
REQ_TYPES = (
    "login",
    "register",
    "order"
    )
REQ_TYPE = REQ_TYPES[LOGIN]

now = datetime.datetime.now().replace(microsecond=0).isoformat()
print(now)

print("--Preloading Data--")
team = f"Team {TEAM_NO}"
print(team)

req_info = TEAM_REQ_INFO.get(TEAM_NO)
for k, v in req_info.items():
    print(f"{k} ::: {v}")

url = f"https://demand.{team.replace(' ', '').lower()}.sweispring21.tk" \
      f"{req_info.get(REQ_TYPE)}"
print(url)

payload_package = req_info.get(f"{REQ_TYPE}_params")
payload = {}
for attr in payload_package:
    k, v = attr
    payload[k] = v
    print(f"{k} ::: {v}")

payload = json.dumps(payload)

print(f"\n--Starting the request for {team}--")
req = requests.post(url, data=payload)
print("--Recording Request--")
file_name = f"{team}_{REQ_TYPE}.txt".replace(' ', '_').lower()
with open(file_name, "w") as f:
    f.write(f"Starting time ::: {now}")
    f.write('\n')
    for i, it in enumerate(req.__dict__.items()):
        k, v = it
        f.write(f"{k} ::: {v}")
        if i != len(req.__dict__.items()) - 1:
            f.write('\n')

print("--Investigating Request--")
with open(file_name, "r") as f:
    for line in f.readlines():
            print(line.strip('\n'))