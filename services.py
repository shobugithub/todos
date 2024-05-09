from utils import ResponseData, hash_password
from db import cur, conn
from models import User
from session import Session
from db import commit
from db import cur
import utils

session = Session()


@commit
def login(username: str, password: str) -> utils.ResponseData:
    user: User | None = session.check_session()
    if user:
        return utils.ResponseData('This User already logged in😎.', False)

    get_user_by_username = '''select * from users where username = %s;'''
    cur.execute(get_user_by_username, (username,))
    user_data = cur.fetchone()
    if not user_data:
        return utils.ResponseData('Bad credentials', False)
    user = User.from_tuple(user_data)
    if user.login_try_count >= 3:
        return utils.ResponseData('User has been blocked😒',False)

    if not utils.match_password(password, user.password):
        update_user_try_count = '''update users set login_try_count = login_try_count + 1 where username = %s;'''
        cur.execute(update_user_try_count, (username,))
        return utils.ResponseData('Bad credentials', False)

    session.add_session(user)
    return utils.ResponseData('User Successfully logged in', True)


def register(username: str, password: str) -> ResponseData:
    # Check if username already exists
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    existing_user = cur.fetchone()
    if existing_user:
        return ResponseData("Username already exists", False)

    # Hash the password
    hashed_password = hash_password(password)

    # Insert the new user into the database
    try:
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        return ResponseData("User registered successfully", True)
    except Exception as e:
        # Handle database insertion errors
        return ResponseData(f"Error registering user: {str(e)}", False)
