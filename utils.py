# import asyncio
# import functools
# from functools import wraps
# import sched, time




def isvalidAlert(message):
        
        

        if len(message.command) < 3:
                return False

        alertPrice = message.command[-1] 

        try:
                float(alertPrice)
        except :
                return False
        return True



# s = sched.scheduler(time.time, time.sleep)

# def setInterval(sec):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*argv, **kw):
#             setInterval(sec)(func)
#             print("started thread")
#             func(*argv, **kw)
#         s.enter(sec, 1, wrapper, ())
#         return wrapper
#     s.run()
#     return decorator



