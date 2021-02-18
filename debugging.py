# Write error message to a log file
import traceback
try:
    raise Exception('This is the error message')
except:
    errorFile = open('error_log.txt', 'a')  # write errors to error_log with append mode in current dir
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print("The traceback info was written error_log.txt")


# assertion
# Assertions are for detecting programmer errors that are not meat to be recovered from. User errors should raise
# exceptions