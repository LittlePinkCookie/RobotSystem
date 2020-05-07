def convert_to_bool(s: str) -> bool:
    return s.lower() in ['true', '1', 't', 'y', 'yes']


def authenticate_controller(controller_sid: str, sid: str):
    if controller_sid != sid:
        raise Exception("Received SID not matching controller SID")
