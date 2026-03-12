import traceback

try:
    import chromadb
    print("IMPORT_OK", getattr(chromadb, "__version__", "no-version"))
except Exception:
    traceback.print_exc()
    print("IMPORT_FAILED")
