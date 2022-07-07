import pywhatkit

def send_zap_messages():
    group_ids = (
        # 'FXjhxREUgEsEO4IjeBRFNQ', # WZ
        '0x3Zhol7zjGCX0BzihWigd', # 450
        # 'Funcmi20rOaHnwHQtVQaMH', # BORA_NETO
        # 'Crxde27gt9356gwWzmLtgI', # AMIRAL
    )
    file = open('message.txt', 'r')
    message = file.read()
    
    for group_id in group_ids:
        pywhatkit.sendwhatmsg_to_group_instantly(
            group_id=group_id,
            message=message,
            tab_close=True,
            close_time=1
        )
