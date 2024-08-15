
# # # # #!/usr/bin/env python3
# # # # """Module for log stats"""


# # # # if __name__ == "__main__":
# # # #     """ Include mongob"""
# # # #     from pymongo import MongoClient
# # # #     client = MongoClient('mongodb://127.0.0.1:27017')

# # # #     # db = client["logs"]
# # # #     # col = db["nginx"]
# # # #     db = client.logs
# # # #     col = db.nginx

# # # #     str = "{} logs".format(col.count_documents({}))
# # # #     method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
# # # #     print(str)
# # # #     print("Methods:")

# # # #     for val in method:
# # # #         count = col.count_documents({'method': val})
# # # #         print("\tmethod {}: {}".format(val, count))

# # # #     status_count = col.count_documents(
# # # #         {'method': 'GET', "path": "/status"}
# # # #     )
# # # #     print("{} status check".format(status_count))

# # # #     distinct_values = col.aggregate([
# # # #         {
# # # #             '$group': {
# # # #                                     '_id': '$ip',
# # # #                                     'count': {'$sum': 1},
# # # #                                     },
# # # #         },
# # # #         {'$sort': {'count': -1}},
# # # #         {'$limit': 10}
# # # #     ])
# # # #     print("IPs:")
# # # #     for val in distinct_values:
# # # #         print("\t{}: {}".format(val.get('_id'), val.get("count")))

# # # #     client.close()



# # # # #!/usr/bin/env python3
# # # # """Module for log stats"""


# # # # if __name__ == "__main__":
# # # #     """ Include mongob"""
# # # #     from pymongo import MongoClient
# # # #     client = MongoClient('mongodb://127.0.0.1:27017')

# # # #     # db = client["logs"]
# # # #     # col = db["nginx"]
# # # #     db = client.logs
# # # #     col = db.nginx

# # # #     str = "{} logs".format(col.count_documents({}))
# # # #     method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
# # # #     print(str)
# # # #     print("Methods:")

# # # #     for val in method:
# # # #         count = col.count_documents({'method': val})
# # # #         print("\tmethod {}: {}".format(val, count))

# # # #     status_count = col.count_documents(
# # # #         {'method': 'GET', "path": "/status"}
# # # #     )
# # # #     print("{} status check".format(status_count))

# # # #     distinct_values = col.aggregate([
# # # #         {
# # # #             '$group': {
# # # #                                     '_id': '$ip',
# # # #                                     'count': {'$sum': 1},
# # # #                                     },
# # # #         },
# # # #         {'$sort': {'count': -1}},
# # # #         {'$limit': 10}
# # # #     ])
# # # #     print("IPs:")
# # # #     for val in distinct_values:
# # # #         print("\t{}: {}".format(val.get('_id'), val.get("count")))

# # # #     client.close()

# # # #!/usr/bin/env python3
# # # """Module for log stats"""

# # # from pymongo import MongoClient

# # # if __name__ == "__main__":
# # #     # Create MongoDB client
# # #     try:
# # #         client = MongoClient('mongodb://127.0.0.1:27017', serverSelectionTimeoutMS=5000)
# # #         db = client.logs
# # #         col = db.nginx
        
# # #         # Check connection to MongoDB
# # #         client.admin.command('ping')

# # #         # Log statistics
# # #         total_logs = "{} logs".format(col.count_documents({}))
# # #         print(total_logs)
# # #         print("Methods:")

# # #         methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
# # #         for method in methods:
# # #             count = col.count_documents({'method': method})
# # #             print("\tmethod {}: {}".format(method, count))

# # #         # Status check
# # #         status_count = col.count_documents({'method': 'GET', "path": "/status"})
# # #         print("{} status check".format(status_count))

# # #         # IP Aggregation and sorting by most frequent
# # #         distinct_values = col.aggregate([
# # #             {
# # #                 '$group': {
# # #                     '_id': '$ip',
# # #                     'count': {'$sum': 1},
# # #                 },
# # #             },
# # #             {'$sort': {'count': -1}},
# # #             {'$limit': 10}
# # #         ])
# # #         print("IPs:")
# # #         for val in distinct_values:
# # #             print("\t{}: {}".format(val.get('_id'), val.get("count")))

# # #     except Exception as e:
# # #         print(f"An error occurred: {e}")
# # #     finally:
# # #         # Close the client connection
# # #         client.close()

# # #!/usr/bin/env python3

# # """
# # This module contains a function that displays stats about Nginx logs stored
# # in MongoDB.
# # """

# # from pymongo import MongoClient


# # def display_log_stats():
# #     """
# #     Display statistics of different HTTP methods in the nginx logs.

# #     This function connects to a MongoDB database, retrieves the nginx logs
# #     collection, and prints the count of each HTTP method (GET, POST, PUT,
# #     PATCH, DELETE) present in the logs.
# #     """

# #     client = MongoClient()
# #     nginx = client.logs.nginx

# #     print(nginx.count_documents({}), "logs")
# #     print("Methods:")

# #     for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
# #         print(
# #             f"\tmethod {method}: {nginx.count_documents({'method': method})}"
# #         )

# #     print(f"{nginx.count_documents({'path': '/status'})} status check")


# # if __name__ == "__main__":
# #     display_log_stats()

# #!/usr/bin/env python3
# """Module for log stats"""


# # if __name__ == "__main__":
# #     """ Include mongob"""
# #     from pymongo import MongoClient
# #     client = MongoClient('mongodb://127.0.0.1:27017')

# #     # db = client["logs"]
# #     # col = db["nginx"]
# #     db = client.logs
# #     col = db.nginx

# #     str = "{} logs".format(col.count_documents({}))
# #     method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
# #     print(str)
# #     print("Methods:")

# #     for val in method:
# #         count = col.count_documents({'method': val})
# #         print("\tmethod {}: {}".format(val, count))

# #     status_count = col.count_documents(
# #         {'method': 'GET', "path": "/status"}
# #     )
# #     print("{} status check".format(status_count))

# #     distinct_values = col.aggregate([
# #         {
# #             '$group': {
# #                                     '_id': '$ip',
# #                                     'count': {'$sum': 1},
# #                                     },
# #         },
# #         {'$sort': {'count': -1}},
# #         {'$limit': 10}
# #     ])
# #     print("IPs:")
# #     for val in distinct_values:
# #         print("\t{}: {}".format(val.get('_id'), val.get("count")))

# #     client.close()

# #!/usr/bin/env python3

# """
# This module contains a function that displays stats about Nginx logs stored
# in MongoDB, including the top 10 IPs by occurrence.
# """

# from pymongo import MongoClient


# def display_log_stats():
#     """
#     Display statistics of different HTTP methods in the nginx logs, including
#     the top 10 IP addresses present in the logs.
#     """

#     client = MongoClient('mongodb://127.0.0.1:27017')
#     nginx = client.logs.nginx

#     # Display total number of logs
#     log_count = nginx.count_documents({})
#     print(f"{log_count} logs")

#     # Display count for each HTTP method
#     print("Methods:")
#     for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
#         method_count = nginx.count_documents({'method': method})
#         print(f"\tmethod {method}: {method_count}")

#     # Display count of GET requests to "/status" path
#     status_check_count = nginx.count_documents({'method': 'GET', 'path': '/status'})
#     print(f"{status_check_count} status check")

#     # Display the top 10 most present IPs in the logs
#     top_ips = nginx.aggregate([
#         {
#             '$group': {
#                 '_id': '$ip',
#                 'count': {'$sum': 1}
#             }
#         },
#         {'$sort': {'count': -1}},
#         {'$limit': 10}
#     ])

#     print("IPs:")
#     for ip in top_ips:
#         print(f"\t{ip['_id']}: {ip['count']}")

#     client.close()


# if __name__ == "__main__":
#     display_log_stats()



#!/usr/bin/env python3
"""Module for log stats"""


if __name__ == "__main__":
    """ Include mongob"""
    from pymongo import MongoClient
    client = MongoClient('mongodb://127.0.0.1:27017')

    # db = client["logs"]
    # col = db["nginx"]
    db = client.logs
    col = db.nginx

    str = "{} logs".format(col.count_documents({}))
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print(str)
    print("Methods:")

    for val in method:
        count = col.count_documents({'method': val})
        print("\tmethod {}: {}".format(val, count))

    status_count = col.count_documents(
        {'method': 'GET', "path": "/status"}
    )
    print("{} status check".format(status_count))

    distinct_values = col.aggregate([
        {
            '$group': {
                                    '_id': '$ip',
                                    'count': {'$sum': 1},
                                    },
        },
        {'$sort': {'count': -1}},
        {'$limit': 10}
    ])
    print("IPs:")
    for val in distinct_values:
        print("\t{}: {}".format(val.get('_id'), val.get("count")))

    client.close()