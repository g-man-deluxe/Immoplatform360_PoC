import io

def erstelle_pdf(data):
    content = "\n".join([f"{k}: {v}" for k, v in data.items()])
    return io.BytesIO(content.encode("utf-8"))
