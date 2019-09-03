 # **What is logging?**
When a program runs ,there are many events can occure.We need to track and record this event so that we can easily debug the program.All reconds are written in log in the form of messages.Acutally this process is called logging.There is a standard library in python called logging to handle this process

# Why not print() ?
For a small project we generally use print() function to debug our program.But it’s so difficult to debug a large program using **print()** function.

**The logging package has a lot of useful features:**

 •	Easy to see where and when (even what line no.) a logging call is being made from.
 
 •	You can log to files, sockets, pretty much anything, all at the same time
 
 •	You can differentiate your logging based on severity


# Using of logging module 

With the logging module imported, you can use something called a “logger” to log messages that you want to see. By default, there are 5 standard levels indicating the severity of events. Each has a corresponding method that can be used to log events at that level of severity. The defined levels, in order of increasing severity, are the following:

- **Debug** (logger.debug): Provide very detailed output. Used for diagnosing problems.

- **Info** (logger.info): Provides information on successful execution. Confirms if things are working as expected.

- **Warning** (logger.warn or logger.warning): Issue a warning regarding a problem that might occur in the future or a recoverable fault.

- **Error** (logger.error): Indicates a problem in the software as it is not executing as expected.

- **Critical** (logger.critical): Indicates a serious error that might stop the program from running.

