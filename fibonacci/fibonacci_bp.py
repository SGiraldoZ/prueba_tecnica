from flask import Blueprint
from .fibonacci_service import fibonacci_from_time
from mail_service import send_fib_email

Fibonacci_bp = Blueprint("fibonacci", __name__)

@Fibonacci_bp.route("/")
def build_fibonacci_now():
    fib_from_time = fibonacci_from_time()

    map_4_return = {
        "generation_time": fib_from_time[1],
        "sequence": fib_from_time[0][::-1]
    }

    send_fib_email(map_4_return)
    
    return map_4_return