from datetime import datetime, timedelta
from kbds.inline import create_buttons
async def generate_time_slots(start_str, end_str, step=1):
    start_time = datetime.strptime(start_str, "%H:%M")
    end_time = datetime.strptime(end_str, "%H:%M")
    time_slots = []
    current_time = start_time

    while current_time < end_time:
        next_time = current_time + timedelta(hours=step)
        time_slots.append((current_time.strftime("%H:%M"), next_time.strftime("%H:%M")))
        current_time = next_time

    return await create_buttons(time_slots)

# time_slots = generate_time_slots('10:00', '23:00')
#

