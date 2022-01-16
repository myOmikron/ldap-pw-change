import ldap as l

from ldap_pw_change import settings


def get_dn(username):
    conn = l.initialize(settings.LDAP_URI)
    conn.bind_s(settings.LDAP_BIND, settings.LDAP_BIND_PW)
    try:
        ret = conn.search_s(
            settings.LDAP_USER_SEARCH_BASE,
            l.SCOPE_SUBTREE,
            settings.LDAP_USER_SEARCH_FILTER.format(username)
        )
        if len(ret) == 0:
            raise l.NO_SUCH_OBJECT
    except l.NO_SUCH_OBJECT:
        print(f"There's no user with username: {username}")
        return None
    conn.unbind_s()
    if len(ret) > 1:
        print(f"There are more than one result for username: {username}")
        return None
    return ret[0][0]


def authenticate(dn, password) -> bool:
    conn = l.initialize(settings.LDAP_URI)
    try:
        conn.bind_s(dn, password)
    except l.INVALID_CREDENTIALS:
        print(f"Invalid credentials for dn: {dn}")
        return False
    conn.unbind_s()
    return True


def change_pw(username, old_password, new_password):
    conn = l.initialize(settings.LDAP_URI)
    dn = get_dn(username)
    if not dn:
        return False
    if authenticate(dn, old_password):
        conn.bind_s(dn, old_password)
        conn.passwd_s(dn, old_password, new_password)
        return True
    else:
        return False
