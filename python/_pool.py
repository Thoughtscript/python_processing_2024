import multiprocessing
import numbers

if __name__ == '__main__':

    try:
        # This must have at least the same number of arguments as example 
        # or you'll see: TypeError: async_call_back() takes 0 positional arguments but 1 was given
        #
        # It's intended to receive the arg outputs: https://bugs.python.org/issue29108
        def async_call_back(x):
            print("async_call_back!")

        def example(x):
            if isinstance(x, numbers.Number):
                print("================= BEGIN multiprocessing.Pool example() =================")
                for y in range(0, x):
                    print(y)
                print("================= END multiprocessing.Pool example() =================")

        # A concise try-catch block with scoped context
        # https://www.geeksforgeeks.org/with-statement-in-python/
        # will automatically handle Exceptions and close certain buffers.
        #
        # Define a Pool
        with multiprocessing.Pool(5) as p:
            # Call the above using parallel processing with a single input
            # https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.map
            # map() is blocking
            p.map(example, [10])
            p.map(example, [20, 30])

            res_map_async = p.map_async(example, [10], callback=async_call_back) # note no args=
            res_map_async.get()

            res_async = p.apply_async(example, args=(25,), callback=async_call_back)
            res_async.get(timeout=3)

    except Exception as ex:

        print('Exception: ' + str(ex))