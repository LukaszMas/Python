# How-To Write Thread-Safe Singleton Class

Ref Guide at: [thread-safe singleton class][1]

1. Code of the Thread-Safe singleton class:
    - ```
      class Singleton:
      _instance = None
      _lock = threading.Lock()

      def __new__(cls, *args, **kwargs):
          if not cls._instance:
              with cls._lock:
                  if not cls._instance:
                      cls._instance = super(Singleton, cls).__new__(cls)
          return cls._instance
      ```

[1]: <https://medium.com/analytics-vidhya/how-to-create-a-thread-safe-singleton-class-in-python-822e1170a7f6> "medium.com"
