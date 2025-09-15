# run.py
# import logging, sys
# from opentelemetry import trace
from application import create_app

# 🔹 OTEL log filter to enrich logs with trace/span context
# class OTELLogFilter(logging.Filter):
#     def filter(self, record):
#         span = trace.get_current_span()
#         ctx = span.get_span_context()
#         if ctx.is_valid:
#             record.trace_id = f"{ctx.trace_id:032x}"
#             record.span_id = f"{ctx.span_id:016x}"
#         else:
#             record.trace_id = "none"
#             record.span_id = "none"
#         record.service_name = "frontend"  # hardcoded service name for this container
#         return True

# def setup_logger():
#     logger = logging.getLogger("otel_logger")  # avoids clashing with root logger
#     if not logger.handlers:  # prevent duplicate handlers
#         logger.setLevel(logging.INFO)
#         handler = logging.StreamHandler(sys.stdout)
#         formatter = logging.Formatter(
#             "%(asctime)s [service=%(service_name)s] "
#             "[trace_id=%(trace_id)s span_id=%(span_id)s] %(message)s"
#         )
#         handler.setFormatter(formatter)
#         handler.addFilter(OTELLogFilter())
#         logger.addHandler(handler)
#     return logger

# # 🔹 Create app + logger
# logger = setup_logger()
app = create_app()

if __name__ == "__main__":
    # logger.info("🚀 Starting frontend Flask service...")
    app.run(host="0.0.0.0", port=5000, debug=True)


# run.py
# import logging
# import sys
# from application import create_app

# # --- Configure root logger once ---
# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)

# if not logger.handlers:
#     handler = logging.StreamHandler(sys.stdout)
#     formatter = logging.Formatter(
#         "%(asctime)s [service=frontend] [trace_id=%(trace_id)s span_id=%(span_id)s] %(message)s"
#     )
#     handler.setFormatter(formatter)
#     logger.addHandler(handler)

# logger.info("Starting the Flask application with OpenTelemetry logging")

# # --- Create and run app ---
# app = create_app()

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)

# import logging
# import sys
# from flask import Flask

# # Configure logging
# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s [service=%(service.name)s] [trace_id=%(trace_id)s span_id=%(span_id)s] %(message)s",
#     stream=sys.stdout
# )

# logger = logging.getLogger(__name__)
# logger.info("Starting the Flask application with OpenTelemetry logging")
# import logging
# import sys

# class SafeFormatter(logging.Formatter):
#     def format(self, record):
#         if not hasattr(record, "trace_id"):
#             record.trace_id = "none"
#         if not hasattr(record, "span_id"):
#             record.span_id = "none"
#         if not hasattr(record, "service.name"):
#             record.__dict__["service.name"] = "frontend"
#         return super().format(record)

# formatter = SafeFormatter(
#     "%(asctime)s [service=%(service.name)s] [trace_id=%(trace_id)s span_id=%(span_id)s] %(message)s"
# )

# handler = logging.StreamHandler(sys.stdout)
# handler.setFormatter(formatter)

# root = logging.getLogger()
# root.setLevel(logging.INFO)
# root.addHandler(handler)

# logger = logging.getLogger(__name__)

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# logger.info("Starting the Flask application with OpenTelemetry logging")
# from application import create_app

# app = create_app()

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)