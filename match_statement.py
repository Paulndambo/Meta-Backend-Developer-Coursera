http_status = 503

match http_status:
    case 200 | 201:
        print("Success")
    case 400:
        print("Bad request")
    case 404:
        print("Not Found!!")
    case 500:
        print("Internal Server Error!!")
    case _:
        print("Unknown")