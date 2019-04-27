import logging


def main():
    logging.basicConfig(level=logging.DEBUG, filemode="w", filename="output.log")

    logging.debug("This is a debug-level log message")
    logging.info("This is an info-level log message")
    logging.warning("This is a warning-level message")
    logging.error("This is an error-level message")
    logging.critical("This is a critical-level message")
    logging.info("Here's a {} variable and an int: {}".format("string", 10))

    # ---

    ext_data = {'user': 'joem@example.com'}

    def another_function():
        logging.debug("This is a debug-level log message", extra=ext_data)

    fmt_str = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d User:%(user)s %(message)s"
    date_str = "%m/%d/%Y %I:%M:%S %p"

    logging.basicConfig(level=logging.DEBUG, filemode="w", filename="output.log", format=fmt_str, datefmt=date_str)

    logging.info("This is an info-level log message", extra=ext_data)
    logging.warning("This is a warning-level message", extra=ext_data)

    another_function()


if __name__ == '__main__':
    main()
