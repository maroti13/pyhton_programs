def db_conn(username,password):
    res="Success" if username == "maroti" and password == "maroti123" else "fail"
    print(res)

db_conn("maroti","maroti123")