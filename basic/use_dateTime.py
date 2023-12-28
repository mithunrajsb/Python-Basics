from datetime import datetime, timedelta, timezone

now = datetime.now()
print('now =', now)
print('type(now) =', type(now))

dt = datetime(2023, 12, 19, 10, 35)
print('dt =', dt)

print('datetime -> timestamp:', dt.timestamp())
t = dt.timestamp()

print('timestamp -> datetime:', datetime.fromtimestamp(t))
print('timestamp -> datetime as UTC+0:', datetime.utcfromtimestamp(t))

