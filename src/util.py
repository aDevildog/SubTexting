import sublime, base64

SETTNIGS_FILE = 'SubTexting.sublime-settings'

def set_pref(key, val):
	pref = sublime.load_settings(SETTNIGS_FILE)
	pref.set(key, val)
	sublime.save_settings(SETTNIGS_FILE)

def get_pref(key):
	return sublime.load_settings(SETTNIGS_FILE).get(key)

def get_host():
  return '52.11.152.202:80'

def get_auth_token():
  user_and_pass = "%s:%s" % (get_pref('username'), get_pref('key'))
  e_auth = base64.b64encode(bytes(user_and_pass, 'utf-8')).decode('utf-8')
  return "Basic %s" % e_auth

def get_contact_name(local_id):
  contacts = get_pref('contact_list')
  return contacts[str(local_id)]